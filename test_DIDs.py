#!/usr/local/bin/python
from client import NewClient
from fakedata import DID
from helpers import checkResponseOK, compareDictKeyValues, checkLog

class Test_DID:

    @classmethod
    def setup_class(self):
        self.client = NewClient()

    def test_DID(self):
        did = DID()
        result = self.client.addDID(did)
        assert result['result'] == 'OK'
        assert result['i_did'] != None
        did_id = result['i_did']
        checkLog(self.client, 'dids:i_did={0}'.format(did_id), "A")
        # Delete
        response = self.client.deleteDID({'i_did': did_id, 'i_customer': 1})
        checkLog(self.client, 'dids:i_did={0}'.format(did_id), "D")
