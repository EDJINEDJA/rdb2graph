"""
utils has as goal to put in place a set of utils functions useful to transform relational database into graph
In utils, we can found function such as Load that allow us to load the log file  
"""

import typing
import time , csv
import pandas as pd 
import os

class Preprocessing():

    def __init__(self) -> None:
        pass

    def DatasetPreparation(inputPath : str , outputPath : str, fileName :str, outputFileName : str):
        csvLog = pd.read_csv(filepath_or_buffer= os.path.realpath(inputPath + fileName), keep_default_na=True) #Load log from csv
        csvLog.drop_duplicates(keep='first', inplace=True) #remove duplicates from the dataset
        csvLog = csvLog.reset_index(drop=True , inplace=True) #renew the index to close gaps of removed duplicates 

        header = csvLog.columns
        
        #Creat a dict instance eg: {"event":"", "time" : ""}
        columnNewcolumn = {}
        for item in header:
            columnNewcolumn[item]=""
        
        #Replace "" by the right column name
        for item in header :
            firstWord = "Choose the appropriate column name using the  Multidimentional process mining methode"
            print(f"Column : {item}")
            response = input(f"{firstWord} \n {len(firstWord)}*'-' \n Choose the appropriate number \n 1 - Activity \n 2 - Timestamp , \n 3 - Actor")

            if response == 1:
                columnNewcolumn[item] = "Activity"
            elif response == 2:
                columnNewcolumn[item] = "Timestamp"
            elif response == 3:
                columnNewcolumn[item] = "Actor"
            else :
                list_word = header.split(' ')
                singleWord = "_".join(list_word)
                columnNewcolumn[item] = singleWord.capitalize()
        
        #Convert dict into list
        newHeader = list(columnNewcolumn.values())

        #Rename columns with white spaces and columns that refer to time, actors and activities.
        csvLog = csvLog.rename(columns=newHeader)








    def Load(self, filePath : str):

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

        log = pd.DataFrame(event,columns= eventTitle)
    
        return  eventTitle , log

