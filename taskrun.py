#importing required modules

from datetime import datetime
from sched import scheduler
import time
from time import time
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


def myjob():
    print("Hello World", datetime.now())

def myjob2():
    print("this is another job named job2", datetime.now())

#scheduler 1 added here
scheduler = BlockingScheduler()
# scheduler = BackgroundScheduler()
scheduler.add_job(func=myjob, trigger='interval', seconds=5, id = 'my custom task')


#This is the 2nd sceduler 
scheduler.add_job(func=myjob2, trigger='interval', seconds = 6, id = 'my custom task 2')
scheduler.start()
time.sleep(2)
scheduler.start()






