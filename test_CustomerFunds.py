from client import NewClient
from fakedata import Customer
from helpers import checkResponseOK, checkLog
from fixtures import setupRoutingGroup, teardownRoutingGroup

client = NewClient()


class TestCustomerMethods:
    def test_customer_methods(self):

        # Create a Customer
        self.rg_id = setupRoutingGroup(client)
        customer = Customer(self.rg_id)
        customer_name = customer['name']
        result = client.createCustomer(customer)
        customer_id = result['i_customer']
        assert result['result'] == 'OK'
        assert result['i_customer'] != None

        checkLog(client, "customers:i_customer={}".format(customer_id), "A")

        # listCustomers() - does not work as no name_pattern parameter is supported
        #result = client.listCustomers({'name_pattern': customer_name, 'i_wholesaler': 1})
        #eq_(len(result['customers']), 1, "listCustomers(): Expected one customer record only")

        # get newly created customer
        result = client.getCustomerInfo({
            'i_customer': customer_id,
            'i_wholesaler': 1
        })
        assert result['result'] == 'OK'
        result['customer'].update({'i_wholesaler': 1}) # trusted mode support
        newCustomer = result['customer']

        # Debit funds from Customers balance
        debitResult = client.customerDebit({
            'i_wholesaler': 1,
            'i_customer': customer_id,
            'amount': 50.12,
            'currency': 'USD'
        })
        checkResponseOK(debitResult)
        balance = client.getCustomerInfo({
            'i_customer': customer_id,
            'i_wholesaler': 1
        })['customer']['balance']
        assert balance == -49.88
        checkLog(client,
                 "debit:i_customer={}:amount=50.12 USD".format(customer_id),
                 "FUNDS")

        # Add funds to Customers balance
        creditResult = client.customerAddFunds({
            'i_wholesaler': 1,
            'i_customer': customer_id,
            'amount': 20.12,
            'currency': 'USD'
        })
        checkResponseOK(creditResult)
        balance = client.getCustomerInfo({
            'i_customer': customer_id,
            'i_wholesaler': 1
        })['customer']['balance']
        assert balance == -70.00
        checkLog(client, "add:i_customer={}:amount=20.12 USD".format(customer_id),
                 "FUNDS")

        # Add funds to Customers balance
        creditResult = client.customerCredit({
            'i_wholesaler': 1,
            'i_customer': customer_id,
            'amount': 22.12,
            'currency': 'USD'
        })
        checkResponseOK(creditResult)
        balance = client.getCustomerInfo({
            'i_customer': customer_id,
            'i_wholesaler': 1
        })['customer']['balance']
        assert balance == -92.12
        checkLog(client,
                 "credit:i_customer={}:amount=22.12 USD".format(customer_id),
                 "FUNDS")

        # Delete Customer
        result = client.deleteCustomer({
            'i_customer': customer_id,
            'i_wholesaler': 1
        })
        checkResponseOK(result)
        checkLog(client, "customers:i_customer={}".format(customer_id), "D")

        # Delete Routing Group
        teardownRoutingGroup(client, self.rg_id)

