import pytest
from client import NewClient
from copy import copy

class TestBalances:

    @classmethod
    def setup_class(self):
        self.i_customer = 1
        self.client = NewClient()
        self.request = { 'i_customer': self.i_customer }

    def test_getBalancesTotals(self):
        request = copy(self.request)
        request["i_balances"] = [ 1, 2, 3 ]
        result = self.client.getBalancesTotals(request)
        assert result['result'] == 'OK'

