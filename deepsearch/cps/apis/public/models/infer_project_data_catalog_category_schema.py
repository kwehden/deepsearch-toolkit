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


class InferProjectDataCatalogCategorySchema(object):
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
        'sample_size': 'int'
    }

    attribute_map = {
        'sample_size': 'sample_size'
    }

    def __init__(self, sample_size=None, local_vars_configuration=None):  # noqa: E501
        """InferProjectDataCatalogCategorySchema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sample_size = None
        self.discriminator = None

        if sample_size is not None:
            self.sample_size = sample_size

    @property
    def sample_size(self):
        """Gets the sample_size of this InferProjectDataCatalogCategorySchema.  # noqa: E501


        :return: The sample_size of this InferProjectDataCatalogCategorySchema.  # noqa: E501
        :rtype: int
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        """Sets the sample_size of this InferProjectDataCatalogCategorySchema.


        :param sample_size: The sample_size of this InferProjectDataCatalogCategorySchema.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                sample_size is not None and sample_size > 1000):  # noqa: E501
            raise ValueError("Invalid value for `sample_size`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sample_size is not None and sample_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `sample_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._sample_size = sample_size

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
        if not isinstance(other, InferProjectDataCatalogCategorySchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InferProjectDataCatalogCategorySchema):
            return True

        return self.to_dict() != other.to_dict()