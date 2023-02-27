"""

"""

import typing
import time , csv

class Preprocessing():

    def __init__(self) -> None:
        pass


    def Load(filePath : str):

        eventTitle = []
        event = []
        numberEvent = 0
        
        with open(filePath , mode = "r") as f:
            row = csv.reader(f)

            if numberEvent == 0 :

                eventTitle.extend(list(row))

                numberEvent +=1
            else:

                event.append(row)

