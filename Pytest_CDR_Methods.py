from client import NewClient



class TestCDRMethods:
    # TODO: Add coverage for all CDR related methods.
    client = NewClient()
    params = {
            'limit': 1,
            'i_customer': 1
             }

    def test_getAccountCDRs(self):
        result = self.client.getAccountCDRs(self.params)
        assert result['result'] == 'OK'
        if not result['cdrs']:
            print "Test failed - no calls found for last hour or Record_SDP is disabled for environment. Place the call and try again"
        assert result['cdrs'] != None

    def test_getCDRSDP(self):
        # getAccountCDRs part
        result = self.client.getAccountCDRs(self.params)

        assert result['result'] ==  'OK'
        assert result['cdrs'] != None

        # getCDRSDP part
        i_call=result['cdrs'][0]['i_call']
        result = self.client.getCDRSDP({'i_call': i_call, 'i_customer': 1})
        assert result['result'] == 'OK'
        assert result['records'] != None

