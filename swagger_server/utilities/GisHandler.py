"""
This class is responsible for handling the GIS API and returning the data in a format that is usable by the rest of the application.
It also handles the sorting of bin days
"""

import requests
import json
import datetime

from swagger_server.models import BinDay
import swagger_server.Constants.BinTypes as BinTypes
import swagger_server.Constants.ServiceCodes as ServiceCodes

# Standard constants
templateURL = "https://mapping.dorsetcouncil.gov.uk/GIService/GIService.svc/localinfoservice?service=$SERVICE_NAME$&uprn=$UPRN$"
servicePlaceHolder = "$SERVICE_NAME$"
uprnPlaceHolder = "$UPRN$"


def makeRequest(url):
    response = requests.get(url)
    return response.json()


def filterForDate(responseJson):
    values = responseJson["Values"]
    # Checks if the values is None and returns None if it is
    if values is None:
        return None

    dateString = values[0]["DateNextVisit"]
    # Get the date from the string with the format of e.g. Tuesday 24 January 2023
    date = datetime.datetime.strptime(dateString, "%A %d %B %Y")
    return date

def getBinDates(uprn):
    baseURL = templateURL.replace(uprnPlaceHolder, str(uprn))

    refuse = filterForDate(makeRequest(baseURL.replace(servicePlaceHolder, ServiceCodes.REFUSE)))
    recycling = filterForDate(makeRequest(baseURL.replace(servicePlaceHolder, ServiceCodes.RECYCLING)))
    gardenWaste = filterForDate(makeRequest(baseURL.replace(servicePlaceHolder, ServiceCodes.GARDEN_WASTE)))
    foodWaste = filterForDate(makeRequest(baseURL.replace(servicePlaceHolder, ServiceCodes.FOOD_WASTE)))

    # Create a dictionary with the service as the key and the date as the value
    binDays = {
        BinTypes.REFUSE: refuse,
        BinTypes.RECYCLING: recycling,
        BinTypes.GARDEN_WASTE: gardenWaste,
        BinTypes.FOOD_WASTE: foodWaste
    }
    #Remove None values from the dictionary
    binDays = {key: value for key, value in binDays.items() if value is not None}

    # Sort the dictionary by the date
    sortedBinDays = sorted(binDays.items(), key=lambda x: x[1])

    #Create a new dictionary with the dates as strings in the format of e.g. 24/01/2023
    stringBinDays = {key: value.strftime("%d/%m/%Y") for key, value in sortedBinDays}
    return stringBinDays

def checkAlert(binDayObj):
    # Check if the collection_date is within 2 days of the current date
    binDayObj.alert = (datetime.datetime.strptime(binDayObj.collection_date, "%d/%m/%Y") - datetime.datetime.now()).days <= 2
    return binDayObj

def handleBoolProperties(binDayObj):
    # Set the boolean properties to false
    binDayObj.has_refuse = False
    binDayObj.has_recycling = False
    binDayObj.has_garden_waste = False
    binDayObj.has_food_waste = False
    # Runs through the bins property and sets the boolean properties to true if the bin is in the list
    for service in binDayObj.bins:
        if service == BinTypes.REFUSE:
            binDayObj.has_refuse = True
        elif service == BinTypes.RECYCLING:
            binDayObj.has_recycling = True
        elif service == BinTypes.GARDEN_WASTE:
            binDayObj.has_garden_waste = True
        elif service == BinTypes.FOOD_WASTE:
            binDayObj.has_food_waste = True

def getBinDays(uprn):

    binDates = getBinDates(uprn)
    # Create a bin day object
    binDay = BinDay()
    # Get the soonest bin day date based on the sorted dictionary
    binDay.collection_date = binDates[list(binDates.keys())[0]]
    # Create a list of bins that are due on the next collection day and sets it to the bins property
    binDay.bins = [key for key, value in binDates.items() if value == binDay.collection_date]
    # Check if the collection date is within 2 days of the current date
    checkAlert(binDay)
    # Set the boolean properties based on the bins property
    handleBoolProperties(binDay)
    # Sets the is_cached property to false
    binDay.is_cached = False
    # Return the bin day object
    return binDay
