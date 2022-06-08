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


class RunDataFlowTemplateOptions1(object):
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
        'data_flow': 'ProjectProjKeyKgcRawDataflowTemplatesActionsRunDataFlow',
        'log_task': 'bool',
        'variable_values': 'dict(str, object)'
    }

    attribute_map = {
        'data_flow': 'data_flow',
        'log_task': 'log_task',
        'variable_values': 'variable_values'
    }

    def __init__(self, data_flow=None, log_task=True, variable_values=None, local_vars_configuration=None):  # noqa: E501
        """RunDataFlowTemplateOptions1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_flow = None
        self._log_task = None
        self._variable_values = None
        self.discriminator = None

        self.data_flow = data_flow
        self.log_task = log_task
        self.variable_values = variable_values

    @property
    def data_flow(self):
        """Gets the data_flow of this RunDataFlowTemplateOptions1.  # noqa: E501


        :return: The data_flow of this RunDataFlowTemplateOptions1.  # noqa: E501
        :rtype: ProjectProjKeyKgcRawDataflowTemplatesActionsRunDataFlow
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """Sets the data_flow of this RunDataFlowTemplateOptions1.


        :param data_flow: The data_flow of this RunDataFlowTemplateOptions1.  # noqa: E501
        :type: ProjectProjKeyKgcRawDataflowTemplatesActionsRunDataFlow
        """
        if self.local_vars_configuration.client_side_validation and data_flow is None:  # noqa: E501
            raise ValueError("Invalid value for `data_flow`, must not be `None`")  # noqa: E501

        self._data_flow = data_flow

    @property
    def log_task(self):
        """Gets the log_task of this RunDataFlowTemplateOptions1.  # noqa: E501


        :return: The log_task of this RunDataFlowTemplateOptions1.  # noqa: E501
        :rtype: bool
        """
        return self._log_task

    @log_task.setter
    def log_task(self, log_task):
        """Sets the log_task of this RunDataFlowTemplateOptions1.


        :param log_task: The log_task of this RunDataFlowTemplateOptions1.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and log_task is None:  # noqa: E501
            raise ValueError("Invalid value for `log_task`, must not be `None`")  # noqa: E501

        self._log_task = log_task

    @property
    def variable_values(self):
        """Gets the variable_values of this RunDataFlowTemplateOptions1.  # noqa: E501


        :return: The variable_values of this RunDataFlowTemplateOptions1.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._variable_values

    @variable_values.setter
    def variable_values(self, variable_values):
        """Sets the variable_values of this RunDataFlowTemplateOptions1.


        :param variable_values: The variable_values of this RunDataFlowTemplateOptions1.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and variable_values is None:  # noqa: E501
            raise ValueError("Invalid value for `variable_values`, must not be `None`")  # noqa: E501

        self._variable_values = variable_values

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
        if not isinstance(other, RunDataFlowTemplateOptions1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunDataFlowTemplateOptions1):
            return True

        return self.to_dict() != other.to_dict()