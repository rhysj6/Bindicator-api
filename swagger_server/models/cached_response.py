# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.bin_day import BinDay  # noqa: F401,E501
from swagger_server import util


class CachedResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, response: BinDay=None, uprn: str=None, expiry_date_time: datetime=None):  # noqa: E501
        """CachedResponse - a model defined in Swagger

        :param response: The response of this CachedResponse.  # noqa: E501
        :type response: BinDay
        :param uprn: The uprn of this CachedResponse.  # noqa: E501
        :type uprn: str
        :param expiry_date_time: The expiry_date_time of this CachedResponse.  # noqa: E501
        :type expiry_date_time: datetime
        """
        self.swagger_types = {
            'response': BinDay,
            'uprn': str,
            'expiry_date_time': datetime
        }

        self.attribute_map = {
            'response': 'response',
            'uprn': 'uprn',
            'expiry_date_time': 'expiryDateTime'
        }
        self._response = response
        self._uprn = uprn
        self._expiry_date_time = expiry_date_time

    @classmethod
    def from_dict(cls, dikt) -> 'CachedResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The cachedResponse of this CachedResponse.  # noqa: E501
        :rtype: CachedResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def response(self) -> BinDay:
        """Gets the response of this CachedResponse.


        :return: The response of this CachedResponse.
        :rtype: BinDay
        """
        return self._response

    @response.setter
    def response(self, response: BinDay):
        """Sets the response of this CachedResponse.


        :param response: The response of this CachedResponse.
        :type response: BinDay
        """

        self._response = response

    @property
    def uprn(self) -> str:
        """Gets the uprn of this CachedResponse.

        This is the uprn from the request  # noqa: E501

        :return: The uprn of this CachedResponse.
        :rtype: str
        """
        return self._uprn

    @uprn.setter
    def uprn(self, uprn: str):
        """Sets the uprn of this CachedResponse.

        This is the uprn from the request  # noqa: E501

        :param uprn: The uprn of this CachedResponse.
        :type uprn: str
        """

        self._uprn = uprn

    @property
    def expiry_date_time(self) -> datetime:
        """Gets the expiry_date_time of this CachedResponse.

        This is the date-time for when the cached response should be discarded and a new request made  # noqa: E501

        :return: The expiry_date_time of this CachedResponse.
        :rtype: datetime
        """
        return self._expiry_date_time

    @expiry_date_time.setter
    def expiry_date_time(self, expiry_date_time: datetime):
        """Sets the expiry_date_time of this CachedResponse.

        This is the date-time for when the cached response should be discarded and a new request made  # noqa: E501

        :param expiry_date_time: The expiry_date_time of this CachedResponse.
        :type expiry_date_time: datetime
        """

        self._expiry_date_time = expiry_date_time
