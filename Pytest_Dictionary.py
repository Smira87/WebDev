from client import NewClient
from copy import copy

class TestDictionary:

    # setup function
    @classmethod
    def setup_class(self):
        self.i_customer = 1
        self.client = NewClient()
        self.request = { 'i_customer': self.i_customer }
        #self.request = { }

    #
    def test_languages_web(self):
        request = copy(self.request)
        request['name'] = 'languages'
        request['type'] = 'web'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    #
    def test_languages_ivr(self):
        request = copy(self.request)
        request['name'] = 'languages'
        request['type'] = 'ivr'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    #
    def test_export_types(self):
        request = copy(self.request)
        request['name'] = 'export_types'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    #
    def test_currencies(self):
        request = copy(self.request)
        request['name'] = 'currencies'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    #
    def test_timezones(self):
        request = copy(self.request)
        request['name'] = 'timezones'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    def test_media_relays(self):
        request = copy(self.request)
        request['name'] = 'media_relays'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    def test_media_relay_types(self):
        request = copy(self.request)
        request['name'] = 'media_relay_types'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

    def test_qmon_actions(self):
        request = copy(self.request)
        request['name'] = 'qmon_actions'

        result = self.client.getDictionary(request)
        print result
        assert result['result'] == 'OK'
        assert len(result['dictionary']) > 0

