# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.public.configuration import Configuration


class MongoS3CoordinatesWithCollectionList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'mongo': 'MongoCoordinates',
        's3': 'S3Coordinates',
        'collections': 'list[str]'
    }

    attribute_map = {
        'mongo': 'mongo',
        's3': 's3',
        'collections': 'collections'
    }

    def __init__(self, mongo=None, s3=None, collections=None, local_vars_configuration=None):  # noqa: E501
        """MongoS3CoordinatesWithCollectionList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mongo = None
        self._s3 = None
        self._collections = None
        self.discriminator = None

        if mongo is not None:
            self.mongo = mongo
        if s3 is not None:
            self.s3 = s3
        if collections is not None:
            self.collections = collections

    @property
    def mongo(self):
        """Gets the mongo of this MongoS3CoordinatesWithCollectionList.  # noqa: E501


        :return: The mongo of this MongoS3CoordinatesWithCollectionList.  # noqa: E501
        :rtype: MongoCoordinates
        """
        return self._mongo

    @mongo.setter
    def mongo(self, mongo):
        """Sets the mongo of this MongoS3CoordinatesWithCollectionList.


        :param mongo: The mongo of this MongoS3CoordinatesWithCollectionList.  # noqa: E501
        :type: MongoCoordinates
        """

        self._mongo = mongo

    @property
    def s3(self):
        """Gets the s3 of this MongoS3CoordinatesWithCollectionList.  # noqa: E501


        :return: The s3 of this MongoS3CoordinatesWithCollectionList.  # noqa: E501
        :rtype: S3Coordinates
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this MongoS3CoordinatesWithCollectionList.


        :param s3: The s3 of this MongoS3CoordinatesWithCollectionList.  # noqa: E501
        :type: S3Coordinates
        """

        self._s3 = s3

    @property
    def collections(self):
        """Gets the collections of this MongoS3CoordinatesWithCollectionList.  # noqa: E501


        :return: The collections of this MongoS3CoordinatesWithCollectionList.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this MongoS3CoordinatesWithCollectionList.


        :param collections: The collections of this MongoS3CoordinatesWithCollectionList.  # noqa: E501
        :type: list[str]
        """

        self._collections = collections

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MongoS3CoordinatesWithCollectionList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MongoS3CoordinatesWithCollectionList):
            return True

        return self.to_dict() != other.to_dict()