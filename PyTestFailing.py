from client import NewClient
from nose.tools import eq_
from helpers import checkResponseOK
from fakedata import VendorConnection


class TestsThatFailButShouldNot:

    client = NewClient()
    """
    Tests that should pass, but don't. This suite should preferable be empty!
    """

    def test_listVendorWithNoParams(self):
        """
        SS-1092 FIXED! calling xmlapi methods with no params fails, when all params are optional
        listVendors() params are all supposed to be optional, but this test
        throws an error.

        Fault: <Fault 1: "<type 'exceptions.TypeError'>:__execute() takes exactly 4 arguments (3 given)">

        """
        result = self.client.listVendors({'i_customer': 1})
        assert result['result']=='OK'

    def test_getAuditLogsWithNoParams(self):
        """
        SS-626 FIXED! call fails when no args are given.
        The getAuditLogs() docs say that all params are optional,
        but it fails if we do not provide a star_date param.
        """
        logs = self.client.getAuditLogs()
        return logs

    def test_addVendorWithLongWebLogin(self):
        """
        See https://sippysoft.atlassian.net/browse/SS-1093
        web_login is limited to 32. This method should return an error
        but the error could inform the customer what fields length is being
        exceeded.
        Instead of an error like:
            Fault: <Fault 490: 'ERROR:  value too long for type character varying(32)\n'>
        something like:
            Fault: <Fault ???: 'Error: max length for web_login is 32 characters'

        """
        vendor = {
            'name': "2TEST_DATAdasdasd",
            'web_login': 'daaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasddgafghasdgfdsfasAAAAAAAAAAA',
            'web_password': 'sooper_D00per_password',
            'i_time_zone': 1,
            'base_currency': 'USD',
            'i_customer': 1,
        }
        self.client.addVendor(vendor)
