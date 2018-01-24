#!/usr/local/bin/python
from client import NewClient
from helpers import checkResponseOK, compareDictKeyValues, checkLog
from fakedata import DestinationSet, DestinationSetRoute



class TestDestinationSetRoutes:


    @classmethod
    def setup_class(self):
        self.client = NewClient()
        ds = self.client.addDestinationSet(DestinationSet())
        self.ds_id = ds['i_destination_set']




        # TODO API method to delete Destination set


    def test_Destination_Sets_Routes(self):

        # Add route to the destination set
        fakeDSR = DestinationSetRoute()
        fakeDSR['i_destination_set'] = self.ds_id
        result = self.client.addRouteToDestinationSet(fakeDSR)
        assert result['result'] == 'OK'
        resource = "routes:i_destination_set=" + str(self.ds_id) + ",prefix="+ str(fakeDSR['prefix'])

        checkLog(self.client, resource, "A")

        # Update route in the destination set
        anotherFakeDSR = DestinationSetRoute();
        anotherFakeDSR['new_prefix'] = anotherFakeDSR['prefix']
        anotherFakeDSR['prefix'] = str(fakeDSR['prefix'])
        anotherFakeDSR['i_destination_set'] = self.ds_id
        result = self.client.updateRouteInDestinationSet(anotherFakeDSR)
        assert result['result'] == 'OK'

        checkLog(self.client, resource, "U")

