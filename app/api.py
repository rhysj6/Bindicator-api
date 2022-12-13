# Fast api imports
from fastapi import FastAPI

# Other imports

# Internal imports
import gisHandler

# Create the app
app = FastAPI()


# Create a route for the root
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/summary/{uprn}")
async def getSummary(uprn: str):
    return uprn
    # return gisHandler.getNextBins(
    #     gisHandler.getNextDates(
    #         gisHandler.getGISData(uprn)))
