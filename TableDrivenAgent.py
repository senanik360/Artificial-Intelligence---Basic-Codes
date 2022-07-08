table={('RED','ON'):'STOP',
       ('RED','OFF'):'WAIT',
       ('GREEN','ON'):'GO',
       ('GREEN','OFF'):'WAIT'}

percepts=[]  # to store percept sequence
def table_driven_agent(percept):
    print('Perception Received: '+ str(percept))
    percepts.append(percept) # updating percept history
    action = lookup(percept,table) # searching for action
    return action

def lookup(percept,table):
    return table[percept]

# lets simulate the agent
import random
Location = random.choice(['RED','GREEN'])
Condition = random.choice(['ON','OFF'])

while True: # to perceieve environment repeatedly
    action = table_driven_agent((Location, Condition))
    print('Action Performed: '+ action)
    cmd = input('Get Perception (yes/no): ')
    if(cmd != 'yes'): break
    if action == 'GO':
        Location = 'RED'
        Condition = random.choice(['ON','OFF'])
    elif action == 'STOP':
        Location = 'GREEN'
        Condition = random.choice(['ON','OFF'])
    else:
        Condition = 'ON'