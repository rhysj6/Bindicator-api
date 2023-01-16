
import json
import datetime

from swagger_server.models import BinDay
from swagger_server.models import CachedResponse

cache = {}

def getResponse(uprn):
    cacheItem = cache.get(uprn)
    if cacheItem is None:
        return None
    if cacheItem.expiry < datetime.datetime.now():
        return None

    # Clears the cache if there's too many items
    if len(cache) > 100:
        cache.clear()

    # Change the response.is_cached value to true
    response = cacheItem.response
    response.is_cached = True

    return response


def setResponse(uprn, response):
    #Create a new cache item and add it to the cache
    cacheItem = CachedResponse()
    cacheItem.uprn = uprn
    cacheItem.response = response
    cacheItem.expiry = datetime.datetime.now() + datetime.timedelta(hours=3)

    cache[uprn] = cacheItem
