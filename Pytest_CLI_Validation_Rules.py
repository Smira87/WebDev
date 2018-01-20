#!/usr/local/bin/python
from client import NewClient


client = NewClient()

class Test_CLI_Validation_Rules:

    def test_CLIValidationRules(self):

        # Number should match the rule
        test_number = "18545423923"
        test_rule = "(?=^1?[2-9][0-9][0-9][2-9][0-9]{6}$)(?=(?!^1?8(55|66|77|88|00)))"
        result = client.checkMatchRule({'rule': test_rule, 'number': test_number})
        assert result['result'] == 'OK'
        assert result['match'] == True

        # Number should not match the rule
        test_number = "18775423923"
        test_rule = "(?=^1?[2-9][0-9][0-9][2-9][0-9]{6}$)(?=(?!^1?8(55|66|77|88|00)))"
        result = client.checkMatchRule({'rule': test_rule, 'number': test_number})
        assert result['result'] == 'OK'

