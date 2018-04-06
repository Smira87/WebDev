import os
from fakedata import Account, RoutingGroup


def setupAccount(client, routing_group_id):
    acc = Account(routing_group_id=routing_group_id)
    return client.createAccount(acc)['i_account']


def teardownAccount(client, account_id, customer_id=1):
    return client.deleteAccount(
        {'i_account': account_id,
         'i_customer': customer_id})


def setupRoutingGroup(client):
    """Returns id of routing group"""
    rg = RoutingGroup()
    newRd = client.addRoutingGroup(rg)
    return newRd['i_routing_group']


def teardownRoutingGroup(client, rg_id):
    return client.delRoutingGroup({'i_customer':
                                   int(os.environ['SIPPY_CUSTOMER_ID']),
                                   'i_routing_group': rg_id})
