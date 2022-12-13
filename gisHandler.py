from datetime import datetime

import requests
import constants
from dateutil.parser import parse

# A function that takes a UPRN and returns a JSON object containing the data from the GIS service
def getGISData(uprn):
    data_list = [
        serviceCall(uprn, constants.BINS_RECYCLING),
        serviceCall(uprn, constants.BINS_FOOD),
        serviceCall(uprn, constants.BINS_GARDEN),
        serviceCall(uprn, constants.BINS_REFUSE)
    ]
    return data_list


# Makes the api call for a specific service and uprn
# Returns a JSON object
# Example: serviceCall("100010000000", "recycling")
def serviceCall(uprn, service):
    # Build the URL
    url = constants.TEMPLATE_URL.replace("$UPRN$", uprn)
    url = url.replace("$SERVICE_NAME$", service)
    # Get the data
    response = requests.get(url)
    json = response.json()
    values = json[constants.VALUES]
    # Special handling for garden waste (where values can be null)
    if service == constants.BINS_GARDEN:
        try:
            rtn = values[0]
        except Exception as e:
            print(e)
            print(type(e))
            rtn = {
                constants.DATE_NEXT_VISIT: "Tuesday 21 December 3999",
                constants.SERVICE: constants.BINS_GARDEN
            }
    else:
        rtn = values[0]
    return rtn


# A function that takes a list of JSON objects and returns a list of JSON objects with the next date and service name for each service
def getNextDates(data_list):
    # Create a list to store the next dates
    next_dates = []
    # Loop through the data
    for data in data_list:
        print(data)
        # Get the next date
        next_date = data[constants.DATE_NEXT_VISIT]
        # Get the service name
        service_name = data[constants.SERVICE]
        # Add the next date and service name to the list
        next_dates.append({
            constants.NEXT_DATE: next_date,
            constants.SERVICE_NAME: service_name
        })
    # Return the list
    return next_dates


# Function that takes a list from getNextDates and finds which day is next and returns a JSON object with the date, bin, and friendly text
# params: next_dates - a list of JSON objects from getNextDates
# returns: a JSON object with the date, bin, and booleans for each bin
def getNextBins(next_dates):
    # Default values
    has_refuse = False
    has_food = False
    has_garden = False
    has_recycling = False

    for next_date in next_dates:
        # Convert the next date to a datetime object
        dateString = next_date[constants.NEXT_DATE]
        date = parse(dateString)
        #Reinsert the date into the next_date object using new key
        next_date[constants.DATE] = date


    # Sort the list by date
    sorted_list = sorted(next_dates, key=lambda k: k[constants.DATE])
    # Get the first item in the list
    next_bin = sorted_list[0]
    # Get the date
    date = next_bin[constants.DATE]
    # Get the service name
    service_name = next_bin[constants.SERVICE_NAME]

    for bin_result in sorted_list:
        if bin_result[constants.DATE] == next_bin[constants.DATE]:
            if bin_result[constants.SERVICE_NAME] == constants.BINS_RECYCLING:
                has_recycling = True
            elif bin_result[constants.SERVICE_NAME] == constants.BINS_FOOD:
                has_food = True
            elif bin_result[constants.SERVICE_NAME] == constants.BINS_GARDEN:
                has_garden = True
            elif bin_result[constants.SERVICE_NAME] == constants.BINS_REFUSE:
                has_refuse = True

    rtn = {
        constants.DATE: date,
        constants.SERVICE_NAME: service_name,
        constants.HAS_RECYCLING: has_recycling,
        constants.HAS_FOOD: has_food,
        constants.HAS_GARDEN: has_garden,
        constants.HAS_REFUSE: has_refuse
    }

    # Return the list
    return rtn
