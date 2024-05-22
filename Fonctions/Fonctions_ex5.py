#ex5 :
from datetime import datetime
import time

def horloge () :
    while True:
        current_time = datetime.now()
        print("Il est :", current_time.strftime("%H:%M:%S"))
        time.sleep(1) 

horloge()