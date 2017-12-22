from fakedata import Account
from client import NewClient
from helpers import checkResponseOK, compareDictKeyValues, checkLog
from fixtures import setupRoutingGroup, teardownRoutingGroup


class Pyest_AccountMethods:


    @classmethod
    def setup_class(self):
        self.client = NewClient()
        self.rg_id = setupRoutingGroup(self.client)


    @classmethod
    def teardown_class(self):
        teardownRoutingGroup(self.client, self.rg_id)



    def test_CreateGetUpdateDeleteAccount(self):
        client = NewClient()
        acc = Account(routing_group_id=self.rg_id)
        # Create
        response = client.createAccount(acc)
        checkResponseOK(response)
        acc_id = response['i_account']
        # check audit log for delete event
        checkLog(client, 'accounts:i_account={0}'.format(acc_id), "A")
        # Update
        newAcc = Account(routing_group_id=self.rg_id)
        newAcc['i_account'] = acc_id
        response = client.updateAccount(newAcc)
        checkResponseOK(response)

        updatedAcc = client.getAccountInfo({'i_account': acc_id})

        # flip sign of balance value, for some historic reason balance
        # values get flipped. Should be investigated and explained.
        newAcc['balance'] = newAcc['balance'] * -1

        compareDictKeyValues(
            newAcc,
            updatedAcc,
            excludekeys=['voip_password', 'web_password', 'vm_password'])
        # check audit log for update event
        checkLog(client, 'accounts:i_account={0}'.format(acc_id), "U")
        # Delete
        response = client.deleteAccount({'i_account': acc_id, 'i_customer': 1})
        # check audit log for delete event
        checkLog(client, 'accounts:i_account={0}'.format(acc_id), "D")

