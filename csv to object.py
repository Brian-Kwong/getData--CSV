import csv
from typing import List
from build_data import CountyDemographics,getData


# Gets a example object to reference off of
templateObject = getData()[0]
#Creates a blank list
list_of_counties = []

# Retrieves the attribute for the object in question
def getAttributes(obj:object)->List[str]:
	return [attribute for attribute in dir(obj) if not ("_" in attribute)]
# Sets attributes in a list for later use
attributeList = getAttributes(templateObject)

try:
	# Opens the csv file
	with open("CountyDemographicsFiltered.csv","r") as csvFile:
		data = csv.DictReader(csvFile)
		for dataLine in data:
			# Reads each row in the csv file
			# Remenber the previous program wrote the data in a dict key:value format so we just reverse that to retrieve the data
			for attribute in dataLine:
				# If the attribute is on the top level easy append the attribute to a sample object
				if attribute in attributeList:
					templateObject.__setattr__(attribute,dataLine[attribute])
				else:
					# Else the attribute is nested in a dict so we rebuild the dict one item at a time by overiding the sample object
					for attributes in attributeList:
						currentAttribute = templateObject.__getattribute__(attributes)
						if attribute in currentAttribute:
							currentAttribute[attribute] = dataLine[attribute]
			# Once the object is rebuilt we append it to a list
			list_of_counties.append((templateObject))
	# Print the final list when all rows have been read and converted back into a their respective object
	print(list_of_counties)
	# Writes the list to a .txt file for easy copy and paste
	# Python 'doesn't' have a default copy and paste module so did this instead
	with open("CountyDemographicsFiltered.txt","w") as file:
		file.write(str(list_of_counties))
	try:
		from pyperclip import copy
		copy(str(list_of_counties))
	except ModuleNotFoundError:
		pass
# What happens if the file cant be found and or read
except Exception as e:
	if type(e) == FileNotFoundError:
		print("Looks like 'CountyDemographicsFiltered.csv' can not be found or accessed.\nPlease make sure all other programs are not accessing it before trying again.")
	elif type(e) == (IndexError, ValueError):
		print("Looks like the file is empty and or corrupted \nPlease regenerate the file using : 'Generate py to csv.py' before trying again")
	else:
		str(e)