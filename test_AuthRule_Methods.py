import os
from client import NewClient
from fixtures import setupRoutingGroup, teardownRoutingGroup
from fixtures import setupAccount, teardownAccount
from helpers import checkResponseOK, compareDictKeyValues, checkLog


class TestAuthRuleMethods:

    @classmethod
    def setup_class(self):
        self.client = NewClient()
        self.rg_id = setupRoutingGroup(self.client)
        self.acc_id = setupAccount(self.client, self.rg_id)

    @classmethod
    def teardown_class(self):
        teardownAccount(self.client, self.acc_id)
        teardownRoutingGroup(self.client, self.rg_id)

    def test_AddUpdateListDeleteAuthRules(self):
        authRule = {
            'i_account': self.acc_id,
            'i_customer': int(os.environ['SIPPY_CUSTOMER_ID']),
            'i_protocol': 1,  # TODO
            'cld_translation_rule': 's/^/1/',
            'cli_translation_rule': 's/^1/+1/',
            'remote_ip': '192.168.1.1',
            'incoming_cli': '123*',
            'incoming_cld': '123*',
            'i_tariff': int(os.environ['SIPPY_TARIFF_ID']),
            'i_routing_group': self.rg_id
        }
        resp = self.client.addAuthRule(authRule)
        checkResponseOK(resp)
        auth_id = resp['i_authentication']

        resource_str = 'authentications:i_authentication={}:i_account={}'.format(
            auth_id, self.acc_id)

        checkLog(self.client, resource=resource_str, action="A")

        resp = self.client.listAuthRules({
            'i_authentication': auth_id,
            'i_customer': int(os.environ['SIPPY_CUSTOMER_ID']),
        })
        authRuleGot = [a for a in resp['authrules']
                       if a['i_authentication'] == auth_id][0]

        compareDictKeyValues(authRule,
                             authRuleGot,
                             excludekeys=['i_customer','i_protocol','i_tariff','i_routing_group'],
                             debug=True)

        authRuleUpdate = {
            'i_authentication': auth_id,
            'i_account': self.acc_id,
            'i_customer': int(os.environ['SIPPY_CUSTOMER_ID']),
            'i_protocol': 2,  # TODO
            'cld_translation_rule': '',
            'cli_translation_rule': 's/^353/+353/',
            'remote_ip': '192.168.1.2',
            'incoming_cli': '124*',
            'incoming_cld': '124*',
            'i_tariff': int(os.environ['SIPPY_TARIFF_ID']),
            'i_routing_group': self.rg_id
        }
        checkResponseOK(self.client.updateAuthRule(authRuleUpdate))

        checkLog(self.client, resource=resource_str, action="U")

        authRuleGot = self.client.listAuthRules({
            'i_authentication': auth_id,
            'i_customer': os.environ['SIPPY_CUSTOMER_ID'],
        })['authrules'][0]

        compareDictKeyValues(authRuleUpdate,
                             authRuleGot,
                             excludekeys=['i_customer','i_protocol','i_tariff','i_routing_group'],
                             debug=True)

        authDelResponse = self.client.delAuthRule({
            'i_authentication': auth_id,
            'i_account': self.acc_id,
            'i_customer': os.environ['SIPPY_CUSTOMER_ID'],
        })
        # Failing test, see https://sippysoft.atlassian.net/browse/SS-1784
        checkResponseOK(authDelResponse)
        checkLog(self.client, resource=resource_str, action="D")
