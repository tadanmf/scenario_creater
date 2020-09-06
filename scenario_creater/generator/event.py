import random
from scenario_creater.generator.resource import crime

category = ['범죄']

def select():
    this_event = {}
    event = random.choice(category)
    this_event['무슨 일이 일어났나요?'] = event
    if event == '범죄':
        this_event['어떤 범죄인가요?'] = random.choice(crime.category)
        this_event['어떤 역할을 했나요?'] = random.choice(crime.role)
    return this_event
