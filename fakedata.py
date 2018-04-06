import os
import random
from faker import Factory


test_data_prefix = "TEST_DATA_"


def prefixed_test_name(maxlen, locale="en"):
    test_data_prefix = "TEST_DATA_"
    fake = Factory.create(locale)
    maxlen = maxlen - len(test_data_prefix)
    return test_data_prefix + fake.text(max_nb_chars=maxlen)


def Vendor(locale="en"):
    fake = Factory.create(locale)

    vendor = {
        'i_customer': 1, #trusted_mode   
        'name': "TEST_DATA_" + fake.company(),
        'web_login': fake.user_name()[:32],
        'web_password': fake.password(length=12,
                                      special_chars=True,
                                      digits=True,
                                      upper_case=True,
                                      lower_case=True) + 'a1A',
        #      'i_time_zone': fake.timezone(),
        'i_time_zone': 370, # let it be UTC, according to time_zones table in DB
        'balance': 100,
        #  'base_currency': fake.currency_code(),
        'base_currency': 'USD',
        #      'i_lang': fake.(),
        'i_lang': 'en',
        'company_name': fake.company(),
        'salutation': fake.prefix(),
        'first_name': fake.first_name()[:32],
        'mid_init': 'P',
        'last_name': fake.last_name()[:32],
        'street_addr': fake.street_address(),
        'state': fake.state(),
        'postal_code': fake.postcode(),
        'city': fake.city()[:32],
        'country': fake.country()[:32],
        'contact': fake.name(),
        'phone': fake.phone_number(),
        'fax': fake.phone_number(),
        'alt_phone': fake.phone_number(),
        'alt_contact': fake.phone_number(),
        'email': fake.safe_email(),
        'cc': fake.safe_email(),
        'bcc': fake.safe_email(),
        'round_up': True,
        'decimal_precision': 7,
        'cost_round_up': True
    }

    return vendor


def fake_ip_address(ipv, locale="en"):
    fake = Factory.create(locale)
    if ipv == 4:
        return fake.ipv4()
    return fake.ipv6()


def VendorConnection(vendor_id, ipv=4, locale="en"):
    fake = Factory.create(locale)

    connection = {
        'i_customer': 1, #trusted_mode
        'i_vendor': vendor_id,
        'name': prefixed_test_name(256),
        'destination': fake_ip_address(ipv),
        'i_media_relay': 1,  # TODO: where do we get this from?
        'i_media_relay_type': 1,
        'username': fake.user_name()[:32],
        'password': fake.password()[:32],
        'translation_rule': 's/^/1/',
        'cli_translation_rule': 's/^/1/',
        'capacity': 5,  # Max Concurrent Connections
        'enforce_capacity': False,
        'huntstop_scodes': '403,404',  # Comma delimited SIP codes
        'blocked': False,
        'timeout_100': 10,
        'i_protocol': 1,
        'qmon_asr_enabled': True,
        'qmon_acd_enabled': True,
        'qmon_stat_window': 300,
        'qmon_asr_threshold': 50,
        'qmon_acd_threshold': 3,
        'qmon_retry_interval': 60,
        'qmon_retry_batch': 15,
        'qmon_action': 'make_last_in_routing',
        'qmon_notification_enabled': False,
        'asserted_id_translation': 's/^/1/',
        'use_asserted_id': False,
        'outbound_ip': os.environ["SIPPY_API_HOST"],
        'single_outbound_port': True,
        'ignore_lrn': False,
        'outbound_proxy': fake_ip_address(ipv),
        'max_cps': 5,
        'accept_redirects': True,
        'redirect_depth_limit': 2,
        'from_domain': fake.domain_name()
    }

    return connection


def Account(locale="en", routing_group_id=None):
    fake = Factory.create(locale)
    username = fake.user_name()[:64]
    print(os.environ['SIPPY_BILLING_PLAN_ID'])
    account = {
        'i_customer': 1, #trusted_mode
        'username': username,
        'voip_password': fake.password(length=10,
                                       special_chars=True,
                                       digits=True,
                                       upper_case=True,
                                       lower_case=True) + '1Aa',
        'web_password': fake.password(length=10,
                                      special_chars=True,
                                      digits=True,
                                      upper_case=True,
                                      lower_case=True) + '1Aa',
        'authname': username,
        # Limited to 128 chars, see SS-1109
        'description': 'TEST_DATA' + fake.text(max_nb_chars=119),
        'i_routing_group': routing_group_id,
        'max_sessions': 2,
        'max_credit_time': 3600,
        'translation_rule': '',
        'cli_translation_rule': '',
        'credit_limit': 100,
        'i_billing_plan': int(os.environ['SIPPY_BILLING_PLAN_ID']),  # FIXME: relies on pre-existing switch state.
        'i_time_zone': 370, # let it be UTC, according to time_zones table in DB
        'balance': 100,
        'cpe_number': None,
        'vm_enabled': 1,
        'vm_password': '123',
        'blocked': 0,
        'i_lang': 'en',
        'payment_currency': "USD",
        'payment_method': 1,  # FIXME: poor API UX
        'i_export_type': 1,  # FIXME: poor API UX
        'lifetime': -1,  # FIXME: poor API UX
        'preferred_codec': None,  # FIXME: poor API UX
        'use_preferred_codec_only': 0,
        'reg_allowed': 1,
        'welcome_call_ivr': 0,
        'on_payment_action': None,  # FIXME: poor API UX
        'min_payment_amount': 10,
        'trust_cli': 1,
        'disallow_loops': 0,
        'vm_notify_emails': fake.safe_email(),
        'vm_forward_emails': fake.safe_email(),
        'vm_del_after_fwd': 1,
        'company_name': fake.company(),
        'salutation': fake.prefix(),
        'first_name': fake.first_name()[:32],
        'last_name': fake.last_name()[:32],
        'mid_init': 'M',
        'street_addr': fake.street_address(),
        'state': fake.state(),
        'postal_code': fake.postcode(),
        'country': fake.country()[:32],
        'contact': fake.name(),
        'phone': fake.phone_number(),
        'fax': fake.phone_number(),
        'alt_phone': fake.phone_number(),
        'alt_contact': fake.phone_number(),
        'email': fake.safe_email(),
        'cc': fake.safe_email(),
        'bcc': fake.safe_email(),
        'city': fake.safe_email()[:32],
        'i_media_relay_type': 1,  # FIXME: poor API UX
        'i_password_policy': 1  # FIXME: poor API UX
    }
    return account


def RoutingGroup(locale="en"):
    fake = Factory.create(locale)
    ONNET_SCOPE_CUSTOMER_ONLY = 3
    rg = {
        'i_customer': 1, #trusted_mode
        'policy': 'least_cost',
        'name': prefixed_test_name(64),
        'description': fake.text(max_nb_chars=256),
        'i_media_relay': 1,  # TODO: where do we get this from?
        'disable_onnet_routing': False,
        'onnet_i_connection' : None,
        'disable_onnet_voicemail': False,
        'onnet_voicemail_i_connection' : None,
        'onnet_scope': ONNET_SCOPE_CUSTOMER_ONLY,
        'lrn_enabled': True,
        'lrn_translation_rule': '',
        'timeout_2xx': 250,
    }
    return rg


def DestinationSet(locale="en"):
    fake = Factory.create(locale)
    destinationSet = {
        'i_customer': 1, #trusted_mode
	'name': prefixed_test_name(64),
	'currency': 'USD',
	'description': fake.text(max_nb_chars=256),
	'post_call_surcharge': round(random.uniform(0, 1), 2),
	'connect_fee': round(random.uniform(0, 1), 2),
	'free_seconds': random.randint(0, 20),
	'grace_period': random.randint(0, 20),
    }
    return destinationSet

def DestinationSetRoute(locale="en"):
    fake = Factory.create(locale)
    dsr = {
        'i_customer': 1, #trusted_mode
	'prefix': str(random.randint(0, 999999)),
	'preference': random.randint(0, 10),
	'timeout': random.randint(1, 10),
	'price_1': round(random.uniform(0, 10), 2),
	'price_n': round(random.uniform(0, 10), 2),
	'interval_1': random.randint(0, 100),
	'interval_n': random.randint(1, 100),
	'timeout_1xx': random.randint(1, 100),
	'forbidden': random.choice([True, False]),
    }
    return dsr

def DID(locale="en"):
    fake = Factory.create(locale)
    did = {
	'i_customer': 1, #trusted_mode
	'did': str(random.randint(0, 9999999999999999999)),
	'incoming_did': str(random.randint(0, 999999999999999999999)),
	'cli_translation_rule': "s/^[+]//",
	'description': fake.text(max_nb_chars=128),
	'translation_rule': "s/^9/8/",
	#'i_ivr_application': ,
	#'i_account': ,
	#'i_dids_charging_group': ,
	#'i_vendor': ,
	#'i_connection': ,
	#'buying_i_dids_charging_group': ,
    }
    return did

def Customer(routing_group_id, locale="en"):
    fake = Factory.create(locale)
    customer = {
        'i_wholesaler': 1, #trusted_mode
        'name': test_data_prefix + fake.text(32-19),
        'web_password': fake.password(length=10,
                                      special_chars=True,
                                      digits=True,
                                      upper_case=True,
                                      lower_case=True) + '1Aa',
        'i_tariff': int(os.environ['SIPPY_TARIFF_ID']), #FIXME predefined state
        'i_routing_group': routing_group_id,
        'balance': 100,
        'web_login': 'ss1871kenny',
        'credit_limit': 2000,
        'accounts_mgmt': 7,
        'customers_mgmt': 7,
        'system_mgmt': 1,
        'accounts_matching_rule': '1',
        'mail_from': fake.safe_email(),
        'payment_currency': 'USD',
        'payment_method': 1,
        'min_payment_amount': 2.2,
        'api_access': 1,
        'api_password': fake.password(length=10,
                                      special_chars=True,
                                      digits=True,
                                      upper_case=True,
                                      lower_case=True) + '1Aa',
        'api_mgmt': 1,
        'tariffs_mgmt': 7,
        'max_depth': 9,
        'use_own_tariff': 1,
        'vouchers_mgmt': 7,
        'description': fake.text(max_nb_chars=128),
        'callshop_enabled': True,
        'overcommit_protection': True,
        'overcommit_limit': 0.000000001,
        'did_pool_enabled': True,
        'ivr_apps_enabled': True,
        'asr_acd_enabled': True,
        'debit_credit_cards_enabled': True,
        'conferencing_enabled': True,
        'share_payment_processors': True,
        'dncl_enabled': True,
        'i_time_zone': 370, # let it be UTC, according to time_zones table in DB
        'i_lang': 'ru',
        'i_export_type': 1, # we might need to rework it using getDictionary API call
        'start_page': 3, # 1 = 'My Cdrs', 3 = 'Call Records (CDRs)', 4 = 'My Preferences'
        'css': '<head> <style> body {background-color: lightgreen;} </style> </head>',
        'dns_alias': fake.domain_name(),
        'company_name': fake.company(),
        'salutation': fake.prefix(),
        'first_name': fake.first_name()[:32],
        'last_name': fake.last_name()[:32],
        'mid_init': 'M',
        'street_addr': fake.street_address(),
        'state': fake.state(),
        'postal_code': fake.postcode(),
        'country': fake.country()[:32],
        'contact': fake.name(),
        'phone': fake.phone_number(),
        'fax': fake.phone_number(),
        'alt_phone': fake.phone_number(),
        'alt_contact': fake.phone_number(),
        'email': fake.safe_email(),
        'cc': fake.safe_email(),
        'bcc': fake.safe_email(),
        'city': fake.safe_email()[:32],
        'i_password_policy': 1  # FIXME: poor API UX
    }
    return customer
