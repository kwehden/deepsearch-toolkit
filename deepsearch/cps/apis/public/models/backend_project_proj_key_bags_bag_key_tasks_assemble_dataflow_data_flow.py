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


class BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow(object):
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
        'df_tpl_key': 'str',
        'proj_key': 'str',
        'public': 'bool',
        'raw_data_flow': 'BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlowRawDataFlow'
    }

    attribute_map = {
        'df_tpl_key': 'df_tpl_key',
        'proj_key': 'proj_key',
        'public': 'public',
        'raw_data_flow': 'raw_data_flow'
    }

    def __init__(self, df_tpl_key=None, proj_key=None, public=None, raw_data_flow=None, local_vars_configuration=None):  # noqa: E501
        """BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._df_tpl_key = None
        self._proj_key = None
        self._public = None
        self._raw_data_flow = None
        self.discriminator = None

        if df_tpl_key is not None:
            self.df_tpl_key = df_tpl_key
        if proj_key is not None:
            self.proj_key = proj_key
        if public is not None:
            self.public = public
        if raw_data_flow is not None:
            self.raw_data_flow = raw_data_flow

    @property
    def df_tpl_key(self):
        """Gets the df_tpl_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501

        If set, the data flow with this key will be used.  # noqa: E501

        :return: The df_tpl_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: str
        """
        return self._df_tpl_key

    @df_tpl_key.setter
    def df_tpl_key(self, df_tpl_key):
        """Sets the df_tpl_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.

        If set, the data flow with this key will be used.  # noqa: E501

        :param df_tpl_key: The df_tpl_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: str
        """

        self._df_tpl_key = df_tpl_key

    @property
    def proj_key(self):
        """Gets the proj_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501

        If set, allows for cross-project data flows to be used.  # noqa: E501

        :return: The proj_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.

        If set, allows for cross-project data flows to be used.  # noqa: E501

        :param proj_key: The proj_key of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: str
        """

        self._proj_key = proj_key

    @property
    def public(self):
        """Gets the public of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501

        Must be set if the data flow template is public  # noqa: E501

        :return: The public of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.

        Must be set if the data flow template is public  # noqa: E501

        :param public: The public of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def raw_data_flow(self):
        """Gets the raw_data_flow of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501


        :return: The raw_data_flow of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlowRawDataFlow
        """
        return self._raw_data_flow

    @raw_data_flow.setter
    def raw_data_flow(self, raw_data_flow):
        """Sets the raw_data_flow of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.


        :param raw_data_flow: The raw_data_flow of this BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlowRawDataFlow
        """

        self._raw_data_flow = raw_data_flow

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
        if not isinstance(other, BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackendProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow):
            return True

        return self.to_dict() != other.to_dict()