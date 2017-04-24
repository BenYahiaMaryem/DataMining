from random import randint
import random
import json
data = []
for i in range(1, 10001):
    #print(randint(35, 41))

    data.append({'temperature': float("{0:.1f}".format(random.uniform(35, 41))), 'heartbeat': randint(30, 160), 'humidity': randint(30, 60), 'sick': 0})
    if( ( data[i-1]['temperature']<36.5 or data[i-1]['temperature']>37.5 or data[i-1]['heartbeat']<120 or data[i-1]['humidity']<45 or data[i-1]['humidity']>55) ):
        data[i-1]['sick']=1
print(len(data))

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
