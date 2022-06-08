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


class ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords(object):
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
        'databases': 'object',
        'node_collection': 'ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoordsNodeCollection'
    }

    attribute_map = {
        'databases': 'databases',
        'node_collection': 'node_collection'
    }

    def __init__(self, databases=None, node_collection=None, local_vars_configuration=None):  # noqa: E501
        """ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._databases = None
        self._node_collection = None
        self.discriminator = None

        self.databases = databases
        self.node_collection = node_collection

    @property
    def databases(self):
        """Gets the databases of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.  # noqa: E501


        :return: The databases of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.  # noqa: E501
        :rtype: object
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.


        :param databases: The databases of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and databases is None:  # noqa: E501
            raise ValueError("Invalid value for `databases`, must not be `None`")  # noqa: E501

        self._databases = databases

    @property
    def node_collection(self):
        """Gets the node_collection of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.  # noqa: E501


        :return: The node_collection of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.  # noqa: E501
        :rtype: ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoordsNodeCollection
        """
        return self._node_collection

    @node_collection.setter
    def node_collection(self, node_collection):
        """Sets the node_collection of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.


        :param node_collection: The node_collection of this ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords.  # noqa: E501
        :type: ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoordsNodeCollection
        """
        if self.local_vars_configuration.client_side_validation and node_collection is None:  # noqa: E501
            raise ValueError("Invalid value for `node_collection`, must not be `None`")  # noqa: E501

        self._node_collection = node_collection

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
        if not isinstance(other, ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectProjKeyBagsBagKeyTasksExportDatasetInfoCoords):
            return True

        return self.to_dict() != other.to_dict()