from client import NewClient
from fixtures import setupRoutingGroup, teardownRoutingGroup
from helpers import checkLog, checkResponseOK
from fakedata import Customer

class TestCreateCustomer:

    @classmethod
    def setup_class(self):
        self.client = NewClient()
        self.rg_id = setupRoutingGroup(self.client)


    @classmethod
    def teardown_class(self):
        teardownRoutingGroup(self.client, self.rg_id)



        #FIXME impossible to delete routing group without customer deletion

    def test_Create_Delete(self):
        customer = Customer(self.rg_id)
        result = self.client.createCustomer(customer)
        assert result['result'] == 'OK'
        assert result['i_customer'] != None
        customer_id = result['i_customer']

        #TODO create API method to retrieve customer`s information
        checkLog(self.client, 'customers:i_customer={0}'.format(customer_id), "A")

        # Delete Customer
        result = self.client.deleteCustomer({
            'i_customer': customer_id,
            'i_wholesaler': 1
        })
        checkResponseOK(result)
        checkLog(self.client, "customers:i_customer={}".format(customer_id), "D")

        # Delete Routing Group
#        teardownRoutingGroup(self.client, self.routing_group_id)

    #TODO create API method to delete customer
