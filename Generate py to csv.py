import csv
from typing import List
from build_data import CountyDemographics,getData
import time
import random 

def buildHeader()->List[str]:
    '''
    Builds the header using the attributes from the object
    '''
    attribute_list = [attribute for attribute in dir(getData()[0]) if not ("_" in attribute)]
    dictKey = []
    for attribute in attribute_list:
        if type(getData()[0].__getattribute__(attribute)) == dict:
            for key in getData()[0].__getattribute__(attribute):
                dictKey.append(key) 
        else:
            dictKey.append(attribute)
    return dictKey

# Creates a list of the header names -> List[str]
dictKey = buildHeader()

def buildDataAsDict(obj:object)-> dict:
    '''
    Gets a instance of that object and converts it to a dict format for Python to write to a csv file
    '''
    # Creates empty dict
    dictObject = {}
    # Goes through each attribute of that object gets its value and stores it in a key:value pair in a dict
    for attribute in [attribute for attribute in dir(obj) if not ("_" in attribute)]:
        value = getattr(obj,attribute)
        # If that attribute is a dict will go into the dict and retrieve each key:value pair then add that to a new dict
        if type(value) == dict:
            for key in value:
                
                dictObject[key] = float(value[key])
        else:
            dictObject[attribute] = value
    # Returns the dict
    return dictObject


try:
    numberOFCounties = int(input("How many counties would you like? : "))
    s_time=time.time()
    with open("CountyDemographicsFiltered.csv","w",newline="") as csv_file:
        '''
        Function that writes to the csv file
        '''
        # Writer object
        write = csv.DictWriter(csv_file,dictKey,"",dialect="excel")
        # Writes the header of the Excel file
        write.writeheader()
        # for each object in the sample (randomly generated) of getData List of objects coverts them to a dict then writes that to a excel row 
        for countyDemographics in random.sample(getData(),numberOFCounties):
            write.writerow(buildDataAsDict(countyDemographics))
    print(f'CSV Generated with {numberOFCounties} counties in {round(time.time()-s_time,2)} seconds\nExit Code 0')
except ValueError:
    # What happens if the user entry != number 
    # Throw a readable error and quits the application
    print("Input != Number Please Quit() and Try Again \nExit Code 1")
except PermissionError:
   # Python can not read or write to any file if another program has it open
   # Permission Denied Error
   print(f"Looks like another application (Most likely Microsoft Excel) currently has the file 'CountyDemographicsFiltered.csv' open.\nPlease close all programs associated with the file before trying again\nExit Code: 1")
finally:
    # Tells the user how many rows were generated and then quits application
    input("Press Any Key to Quit")
