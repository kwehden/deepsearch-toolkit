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


class BackendFlavour(object):
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
        'kg_amqp': 'str',
        'kg_legacy_api': 'str'
    }

    attribute_map = {
        'kg_amqp': 'kg_amqp',
        'kg_legacy_api': 'kg_legacy_api'
    }

    def __init__(self, kg_amqp=None, kg_legacy_api=None, local_vars_configuration=None):  # noqa: E501
        """BackendFlavour - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._kg_amqp = None
        self._kg_legacy_api = None
        self.discriminator = None

        if kg_amqp is not None:
            self.kg_amqp = kg_amqp
        if kg_legacy_api is not None:
            self.kg_legacy_api = kg_legacy_api

    @property
    def kg_amqp(self):
        """Gets the kg_amqp of this BackendFlavour.  # noqa: E501


        :return: The kg_amqp of this BackendFlavour.  # noqa: E501
        :rtype: str
        """
        return self._kg_amqp

    @kg_amqp.setter
    def kg_amqp(self, kg_amqp):
        """Sets the kg_amqp of this BackendFlavour.


        :param kg_amqp: The kg_amqp of this BackendFlavour.  # noqa: E501
        :type: str
        """

        self._kg_amqp = kg_amqp

    @property
    def kg_legacy_api(self):
        """Gets the kg_legacy_api of this BackendFlavour.  # noqa: E501


        :return: The kg_legacy_api of this BackendFlavour.  # noqa: E501
        :rtype: str
        """
        return self._kg_legacy_api

    @kg_legacy_api.setter
    def kg_legacy_api(self, kg_legacy_api):
        """Sets the kg_legacy_api of this BackendFlavour.


        :param kg_legacy_api: The kg_legacy_api of this BackendFlavour.  # noqa: E501
        :type: str
        """

        self._kg_legacy_api = kg_legacy_api

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
        if not isinstance(other, BackendFlavour):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackendFlavour):
            return True

        return self.to_dict() != other.to_dict()