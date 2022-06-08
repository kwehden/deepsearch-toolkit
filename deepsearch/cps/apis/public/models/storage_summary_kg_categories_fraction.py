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


class StorageSummaryKGCategoriesFraction(object):
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
        'color': 'str',
        'name': 'str',
        'percentage': 'float',
        'size_bytes_db': 'float',
        'size_converted_db': 'str'
    }

    attribute_map = {
        'color': 'color',
        'name': 'name',
        'percentage': 'percentage',
        'size_bytes_db': 'size_bytes_db',
        'size_converted_db': 'size_converted_db'
    }

    def __init__(self, color=None, name=None, percentage=None, size_bytes_db=None, size_converted_db=None, local_vars_configuration=None):  # noqa: E501
        """StorageSummaryKGCategoriesFraction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._color = None
        self._name = None
        self._percentage = None
        self._size_bytes_db = None
        self._size_converted_db = None
        self.discriminator = None

        if color is not None:
            self.color = color
        self.name = name
        self.percentage = percentage
        self.size_bytes_db = size_bytes_db
        self.size_converted_db = size_converted_db

    @property
    def color(self):
        """Gets the color of this StorageSummaryKGCategoriesFraction.  # noqa: E501


        :return: The color of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this StorageSummaryKGCategoriesFraction.


        :param color: The color of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def name(self):
        """Gets the name of this StorageSummaryKGCategoriesFraction.  # noqa: E501


        :return: The name of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageSummaryKGCategoriesFraction.


        :param name: The name of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def percentage(self):
        """Gets the percentage of this StorageSummaryKGCategoriesFraction.  # noqa: E501


        :return: The percentage of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this StorageSummaryKGCategoriesFraction.


        :param percentage: The percentage of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and percentage is None:  # noqa: E501
            raise ValueError("Invalid value for `percentage`, must not be `None`")  # noqa: E501

        self._percentage = percentage

    @property
    def size_bytes_db(self):
        """Gets the size_bytes_db of this StorageSummaryKGCategoriesFraction.  # noqa: E501


        :return: The size_bytes_db of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :rtype: float
        """
        return self._size_bytes_db

    @size_bytes_db.setter
    def size_bytes_db(self, size_bytes_db):
        """Sets the size_bytes_db of this StorageSummaryKGCategoriesFraction.


        :param size_bytes_db: The size_bytes_db of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and size_bytes_db is None:  # noqa: E501
            raise ValueError("Invalid value for `size_bytes_db`, must not be `None`")  # noqa: E501

        self._size_bytes_db = size_bytes_db

    @property
    def size_converted_db(self):
        """Gets the size_converted_db of this StorageSummaryKGCategoriesFraction.  # noqa: E501


        :return: The size_converted_db of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :rtype: str
        """
        return self._size_converted_db

    @size_converted_db.setter
    def size_converted_db(self, size_converted_db):
        """Sets the size_converted_db of this StorageSummaryKGCategoriesFraction.


        :param size_converted_db: The size_converted_db of this StorageSummaryKGCategoriesFraction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and size_converted_db is None:  # noqa: E501
            raise ValueError("Invalid value for `size_converted_db`, must not be `None`")  # noqa: E501

        self._size_converted_db = size_converted_db

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
        if not isinstance(other, StorageSummaryKGCategoriesFraction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageSummaryKGCategoriesFraction):
            return True

        return self.to_dict() != other.to_dict()