import os
import pytest
from client import NewClient
from fixtures import setupRoutingGroup, teardownRoutingGroup
from fixtures import setupAccount, teardownAccount
from helpers import checkResponseOK, checkLog


class TestAccountFundsMethods:

    @classmethod
    def setup_class(self):

        self.client = NewClient()
        self.rg_id = setupRoutingGroup(self.client)
        self.acc_id = setupAccount(self.client, self.rg_id)

    @classmethod
    def teardown_class(self):
        teardownAccount(self.client, self.acc_id)
        teardownRoutingGroup(self.client, self.rg_id)

    def test_AccountAddFunds(self):
        # TODO
        # get someone to explain the historic reason aroung
        # how we use negative signs for representing positive
        # amounts
#       self.setUp()

        balance_pre = self.client.getAccountInfo({'i_account': self.acc_id
                                                  })['balance']
        amnt_to_add = 66.66
        currency = 'USD'

        funds = {
            'i_account': self.acc_id,
            'i_customer': os.environ['SIPPY_CUSTOMER_ID'],
            'payment_notes': 'xmlapi test suite add funds',
            'amount': amnt_to_add,
            'currency': currency,
        }
        checkResponseOK(self.client.accountAddFunds(funds))

        balance_post = self.client.getAccountInfo({'i_account': self.acc_id
                                                   })['balance']

        assert balance_pre == balance_post + amnt_to_add

#       self.teardown()

        # check audit log for add funds event
        checkLog(self.client, 'add:i_account={0}:amount={1} {2}'.format(
            self.acc_id, amnt_to_add, currency), "FUNDS")

    def test_AccountDebit(self):

#       self.setUp()

        balance_pre = self.client.getAccountInfo({'i_account': self.acc_id
                                                  })['balance']
        amnt_to_debit = 33.33
        currency = 'USD'

        funds = {
            'i_account': self.acc_id,
            'i_customer': os.environ['SIPPY_CUSTOMER_ID'],
            'payment_notes': 'xmlapi test suite debit funds',
            'amount': amnt_to_debit,
            'currency': currency,
        }
        checkResponseOK(self.client.accountDebit(funds))

        balance_post = self.client.getAccountInfo({'i_account': self.acc_id
                                                   })['balance']

        print(balance_pre, balance_post, amnt_to_debit)
        assert round(balance_pre) == round(balance_post - amnt_to_debit)
        # check audit log for add funds event
        checkLog(self.client, 'debit:i_account={0}:amount={1} {2}'.format(self.acc_id, amnt_to_debit, currency), "FUNDS")

    def test_AccountCredit(self):


#       self.setUp()

        balance_pre = self.client.getAccountInfo({'i_account': self.acc_id
                                                  })['balance']
        amnt_to_credit = 13.33
        currency = 'USD'

        funds = {
            'i_account': self.acc_id,
            'i_customer': os.environ['SIPPY_CUSTOMER_ID'],
            'payment_notes': 'xmlapi test suite credit funds',
            'amount': amnt_to_credit,
            'currency': currency,
        }
        checkResponseOK(self.client.accountCredit(funds))

        balance_post = self.client.getAccountInfo({'i_account': self.acc_id
                                                   })['balance']

        print(balance_pre, balance_post, amnt_to_credit)
        assert round(balance_pre) == round(balance_post + amnt_to_credit)
        # check audit log for add funds event
        checkLog(self.client, 'credit:i_account={0}:amount={1} {2}'.format(self.acc_id, amnt_to_credit, currency), "FUNDS")

