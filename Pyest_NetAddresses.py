from commands import getoutput
from client import NewClient
from os import environ

class Test_NetAddresses(object):
    """
    Unit tests for net_addresses related XML API
    """
    def test_NetAddress(self):
        """
        Test addNetAddress() XML API call
        """
        client = NewClient()
        remote_host_ip = environ["SIPPY_API_HOST"]
        iface = environ["SIPPY_REMOTE_API_IFACE"]
        ip = "192.168.254.254"

        # cleanup DB
        result = client.getNetAddresses({ "ip" : ip })
        if len(result['records']) > 0:
            client.deleteNetAddress({ 'i_net_address' : result['records'][0]["i_net_address"] })

        result = client.addNetAddress({
            "ip" : ip,
            "i_net" : 2,
            "name" : "Test Address",
            "netmask" : "/32",
            "node" : remote_host_ip,
            "active" : True,
            "iface" : iface,
            })
        assert result['result'] == 'OK'
        i_net_address = result['i_net_address']

        result = client.getNetAddresses({ "i_net_address" : i_net_address, 'i_environment' : None })
        assert result['result'] == 'OK'
        assert len(result['records']) == 1

        result = client.updateNetAddress({ "i_net_address" : i_net_address, 'ip' : "10.123.123.123", 'netmask' : "255.255.255.255" })
        assert result['result'] == 'OK'

        result = client.getNetAddresses({ "ip" : "10.123.123.123" })
        assert result['result'] == 'OK'
        assert len(result['records']) == 1

        result = client.deleteNetAddress({ 'i_net_address' : i_net_address })
        assert result['result'] == 'OK'


