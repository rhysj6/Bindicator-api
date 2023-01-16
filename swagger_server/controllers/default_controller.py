import connexion
import six

from swagger_server.models.bin_day import BinDay  # noqa: E501
from swagger_server.utilities import GisHandler
from swagger_server.utilities import CachingHandler


def bin_day_get(uprn, cache=True):  # noqa: E501
    print("Getting bin days for UPRN: " + str(uprn))
    print("Cache: " + str(cache))
    if cache:
        response = CachingHandler.getResponse(uprn)
        if response is not None:
            return response

    response = GisHandler.getBinDays(uprn)
    CachingHandler.setResponse(uprn, response)
    return response
