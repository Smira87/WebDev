import os
import random
from faker import Factory
from fakedata import prefixed_test_name


def addDestinationSet(client, data):
    fake = Factory.create("en")      
    destinationSet = {
        'name': prefixed_test_name(64),
        'currency': 'USD',
        'description': fake.text(max_nb_chars=256),
        'post_call_surcharge': round(random.uniform(0, 1), 2),
        'connect_fee': round(random.uniform(0, 1), 2),
        'free_seconds': random.randint(0, 20),
        'grace_period': random.randint(0, 20),
    }
    if data is not None:
        for i in data:
            destinationSet[i] = data[i]
    result = client.addDestinationSet(destinationSet)
    
    return result
        
def listDestinationSets(client, i_destination_set):

    result = client.listDestinationSets({'i_destination_set': i_destination_set})
    
    return result
    
# Delete destination set
    #TODO create method for Destination Set deletion
    #TODO create audit log entry for Destination Set deletion

