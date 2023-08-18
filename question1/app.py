from datetime import datetime
from flask import Flask
import os 
from utils import getData

app = Flask(__name__)
@app.route("/trains")
def getTrains():
    """
    Comment the fuhnctionality of the route
    """
    data = getData()
    print(len(data))
    
    # display data 
    # ignore next 30mins ( filter)
    now = datetime.now()
    filteredTrains=[]
    for train in data:
        time=train['departureTime']

        # update trains departure time
        # Accounting for delay given in minutes
        time["Minutes"]+=train['delayedBy']

        if(time['Minutes'] >=60 ):
            time['Minutes']-=60
            time['Hours']+=1

        train['updatedTime']=time

        # print(time["Hours"])
        # Accounting for next 30minutes
        # filteredTrains.append(train)
        if(time['Hours'] < now.hour):
            print(time['Hours'] < now.hour)
            continue
        elif (time['Hours'] - now.hour >= 1):
            filteredTrains.append(train)
        elif time['Minutes'] - now.minute < 30:
            continue
        else:
            filteredTrains.append(train)

    # sorting of trains

    print(filteredTrains)
    newList = sorted(filteredTrains, key=lambda x: (x['price']['sleeper'],-(x['seatsAvailable']['sleeper']+x['seatsAvailable']['AC']),x['updatedTime']['Hours'],x['updatedTime']['Minutes'],x['updatedTime']['Seconds']))
    return newList

    # sort according to asc price, desc order of tickets, desc departure time (include delay)
