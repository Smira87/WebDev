#!/usr/local/bin/python
from client import NewClient
from helpers import checkLog
import pytest
import sys
sys.path.append("API_methods")
from API_Destination_Sets import addDestinationSet, listDestinationSets
from fakedata import DestinationSet

client = NewClient()

class TestDestinationSets:

    def test_Destination_Sets(self):
	
	# Create a Destination Set
        createdDS = DestinationSet()
        creation_result = client.addDestinationSet(createdDS)
        print creation_result
        assert creation_result['result'] == 'OK'
        destinationSetID = creation_result['i_destination_set']
        assert creation_result['i_destination_set'] != None

        checkLog(client, "destination_sets:i_destination_set={}".format(destinationSetID), "A")

        # Obtain a Destination Set
	obtain_result = client.listDestinationSets({'i_destination_set': destinationSetID, 'i_customer': 1})
	assert len(obtain_result['list'])==1
        obtain_result['list'][0].update({'i_customer': 1})
        obtainedDS = obtain_result['list'][0]
        
        #print obtainedDS, createdDS, obtain_result,destinationSetID,self.client
        # Compare with the created one	
	for i in createdDS:
	    if i == "currency":
	       	assert createdDS[i] == obtainedDS['iso_4217']
                continue
            assert createdDS[i] == obtainedDS[i]
        
