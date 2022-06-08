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


class DictionaryImportResult(object):
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
        'dictionary': 'Dictionary',
        'import_task': 'Task'
    }

    attribute_map = {
        'dictionary': 'dictionary',
        'import_task': 'import_task'
    }

    def __init__(self, dictionary=None, import_task=None, local_vars_configuration=None):  # noqa: E501
        """DictionaryImportResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dictionary = None
        self._import_task = None
        self.discriminator = None

        if dictionary is not None:
            self.dictionary = dictionary
        if import_task is not None:
            self.import_task = import_task

    @property
    def dictionary(self):
        """Gets the dictionary of this DictionaryImportResult.  # noqa: E501


        :return: The dictionary of this DictionaryImportResult.  # noqa: E501
        :rtype: Dictionary
        """
        return self._dictionary

    @dictionary.setter
    def dictionary(self, dictionary):
        """Sets the dictionary of this DictionaryImportResult.


        :param dictionary: The dictionary of this DictionaryImportResult.  # noqa: E501
        :type: Dictionary
        """

        self._dictionary = dictionary

    @property
    def import_task(self):
        """Gets the import_task of this DictionaryImportResult.  # noqa: E501


        :return: The import_task of this DictionaryImportResult.  # noqa: E501
        :rtype: Task
        """
        return self._import_task

    @import_task.setter
    def import_task(self, import_task):
        """Sets the import_task of this DictionaryImportResult.


        :param import_task: The import_task of this DictionaryImportResult.  # noqa: E501
        :type: Task
        """

        self._import_task = import_task

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
        if not isinstance(other, DictionaryImportResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryImportResult):
            return True

        return self.to_dict() != other.to_dict()