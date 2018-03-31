## Introduction

This test suite provides integration tests for the Sippy XMLAP xmlapi
methods. It should only interact with the xmlapi directly, and never
access the switch under test in any other way. (No direct connections to
DB!)

The test suite provides useful examples of how to use the xmlapi for
developers that wish to integrate and build new systems on top of the
Sippy Platform. For now, it is private, closed source, but we may open it
up to partners or public at some point.

Integration tests should cover the happy path. Testing low-level
validation is not a goal of this test suite, and belongs in the internal
XMLAPI unit tests.

## Set up

Use the [nose](https://nose.readthedocs.org/en/latest/) to run the tests.
```
(cd /usr/ports/devel/py-nose; sudo make clean install)
```
Install pytest.
```
sudo pkg install py27-pytest
```

Use virtualenv to set up an isolated python environment on your system.

```
virtualenv env
source ./env/bin/activate
```

Create some folder into your env and upload there files from Download section https://bitbucket.org/sippysoft/sippy_xmlapi_tests/downloads/ 
And upload the files from this repositorium to the same folder.

make export as follows:

```
export PATH=/usr/local/bin:$PATH
```

Install dependencies listed in `requirements.txt` using pip.

```
(cd /usr/ports/devel/py-pip/; sudo make clean install)
sudo pip install -r requirements.txt 
```

The test suite expects the following environment variables to be set:

You must set the following environment variables:

```
export SIPPY_API_USER='XMLAPI_USERNAME'
export SIPPY_API_PASS='XMLAPI_PASSWORD'
export SIPPY_API_HOST='IP_OR_HOSTNAME_OF_XMLAPI_UNDER_TEST'
export SIPPY_TARIFF_ID='VALID_TARIFF_ID'
export SIPPY_BILLING_PLAN_ID='VALID_SERVICE_PLAN_ID'
export SIPPY_CUSTOMER_ID='1'
export SIPPY_REMOTE_API_IFACE='VALID_INTERFACE_FROM_REMOTE_BOX_UNDER_TEST'
```

`SIPPY_TARIFF_ID` and `SIPPY_CUSTOMER_ID` need to reference the id's of
a tariff and service plan that is set up ahead of time. This is required
until api methods are created to manage Tariff (SS-662) and Service Plan
(SS-622) resources.

SIPPY_REMOTE_API_IFACE has to be referenced with the interface from the remote
server, as there is no working xmlapi method so far to fetch the list of interfaces
from remote server - see SS-2187 for more details

In order to try trusted authentication, 
the IP address of the client needs to be added to the `trusted_hosts`
table in the root (env 1) sippy database.

`insert into trusted_hosts (ip) VALUES ('YOUR IP ADDRESS HERE');`

Note, that with the IP of the client in `trusted_hosts` password authentication
would NOT be tried at all.


## Running the Test Suite

Running with nose
```
nosetests
```

Test particular file:
```
nosetests /usr/home/ssp-root/sippy_xmlapi_tests/Test_NetAddresses.py
```

Test particular method from particular file:
```
nosetests Test_NetAddresses:Test_NetAddresses.test_NetAddress
```

Running with pytest
```
pytest 
```
Test particular file:
```
pytest -v /usr/home/ssp-root/sippy_xmlapi_tests/Pytest_NetAddresses.py

-v is for Verbose
```
## Exit the testing environment
```
deactivate
```

## Known issues:
Destination sets are not deleted on exit because no deleteDestinationSet method exists (SS-2038 for more details)
The destination sets need to be remove manually once the tests are over:

```
#!sql

sippy=> select count(*) from destination_sets where name like 'TEST_DATA_%';
 count
-------
    89
(1 row)

sippy=> delete from destination_sets where name like 'TEST_DATA_%';
DELETE 89
```


## Todo / Ideas


- Switch from nose to pytest.
- Differentiate between trusted mode and authenticated mode
- Write guidelines for writing/structuring tests
- Hook up to run automatically form jenkins.
- Measure round trip time for each xmlapi method
- Make test sip calls to generate CDRs, to allow proper testing of CDR related
  methods


## Contributing

- All python code should be formatted to PEP-8 standards using
  [yapf](https://github.com/google/yapf).
- Do not import/use any internal sippy code in this test suite.
