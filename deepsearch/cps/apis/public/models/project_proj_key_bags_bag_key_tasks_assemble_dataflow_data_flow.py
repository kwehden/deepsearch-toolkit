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


class ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow(object):
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
        'render_options': 'ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlowRenderOptions',
        'template': 'str',
        'variables': 'object'
    }

    attribute_map = {
        'render_options': 'render_options',
        'template': 'template',
        'variables': 'variables'
    }

    def __init__(self, render_options=None, template=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._render_options = None
        self._template = None
        self._variables = None
        self.discriminator = None

        if render_options is not None:
            self.render_options = render_options
        if template is not None:
            self.template = template
        if variables is not None:
            self.variables = variables

    @property
    def render_options(self):
        """Gets the render_options of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501


        :return: The render_options of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlowRenderOptions
        """
        return self._render_options

    @render_options.setter
    def render_options(self, render_options):
        """Sets the render_options of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.


        :param render_options: The render_options of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlowRenderOptions
        """

        self._render_options = render_options

    @property
    def template(self):
        """Gets the template of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501


        :return: The template of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.


        :param template: The template of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def variables(self):
        """Gets the variables of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501


        :return: The variables of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :rtype: object
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.


        :param variables: The variables of this ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow.  # noqa: E501
        :type: object
        """

        self._variables = variables

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
        if not isinstance(other, ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectProjKeyBagsBagKeyTasksAssembleDataflowDataFlow):
            return True

        return self.to_dict() != other.to_dict()