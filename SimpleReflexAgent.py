def simple_reflex_agent(percept):
    print('Perception Received: '+ str(percept))
    location = percept[0]
    status = percept[1]
    if status =='OFF':
        action = 'WAIT'
    elif location == 'RED':
        action = 'STOP'
    elif location =='GREEN':
        action = 'GO'
    return action

import random
Location = random.choice(['RED','GREEN'])
Condition = random.choice(['ON','OFF'])

while True:
    action= simple_reflex_agent((Location,Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd == 'no' or cmd != 'yes'): break
    if action == 'GO':
        Location = 'RED'
        Condition = random.choice(['ON','OFF'])
    elif action== 'STOP':
        Location = 'GREEN'
        Condition = random.choice(['ON','OFF'])
    else:
        Condition = 'ON'