# GIS API URL
TEMPLATE_URL = "https://mapping.dorsetcouncil.gov.uk/GIService/GIService.svc/localinfoservice?service=$SERVICE_NAME$&uprn=$UPRN$"

# Service codes for the GIS API
BINS_RECYCLING = "recyclingday"
BINS_REFUSE = "refuseday"
BINS_FOOD = "foodwasteday"
BINS_GARDEN = "gardenwasteday"

# Constants for parsing data from the GIS API
DATE_NEXT_VISIT = "DateNextVisit"
VALUES = "Values"
SERVICE = "Type"

#Constants for internal application use
NEXT_DATE = "next_date"
SERVICE_NAME = "service_name"

#Constant for api response
DATE = "date"
FRIENDLY_TEXT = "friendly_text"
HAS_REFUSE = "refuse"
HAS_FOOD = "food"
HAS_GARDEN = "garden"
HAS_RECYCLING = "recycling"
