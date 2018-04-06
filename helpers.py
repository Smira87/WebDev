from nose.tools import eq_
from datetime import datetime, timedelta
from pytz.reference import UTC


def checkResponseOK(response):
    """Cheks if the xmlrpc response is OK"""
    eq_(response['result'], 'OK')


def compareDictKeyValues(originalDict, newDict, excludekeys=[], debug=False):
    """Compare the values of all keys in originalDict with keys in
    newDict"""
    errString = "['{0}']={1} != ['{0}']={2}"
    if debug:
        print("originalDict: {}".format(originalDict))
        print("newDict: {}".format(newDict))
    for k in originalDict:
        if debug:
            print(newDict.get(k), originalDict.get(k), errString.format(k, newDict.get(k),
                                                              originalDict.get(k)))
        if k not in excludekeys:  # ignore this key
            eq_(newDict[k], originalDict[k], errString.format(k, newDict[k],
                                                              originalDict[k]))


def getLogs(client, resource=None, action=None):
    # TODO(Jev): tidy this mess up
    fmt = "%H:%M:%S.000 GMT %a %b %d %Y"
    start = (datetime.now(UTC) - timedelta(minutes=1)).strftime(fmt)
    end = (datetime.now(UTC) + timedelta(minutes=1)).strftime(fmt)
    #  end_str = end.strftime("%H:%M:%S.000 GMT %a %b %d %Y")

    req = {'start_date': start, 'end_date': end, 'i_customer': 1}
    if resource is not None:
        req['resource'] = resource

    if action is not None:
        req['action'] = action

    logs = client.getAuditLogs(req)
    return logs


def checkLog(client, resource, action):
    logs = getLogs(client, resource=resource, action=action)
    checkResponseOK(logs)
    count = len(logs['records'])
    err_msg = "Expected one audit log message with action {0} on resource {1}, got {2}"
    eq_(count, 1, err_msg.format(action, resource, count))
