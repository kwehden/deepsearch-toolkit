# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsearch.cps.apis.public.api_client import ApiClient
from deepsearch.cps.apis.public.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UploadsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_project_scratch_file(self, proj_key, filename, **kwargs):  # noqa: E501
        """create_project_scratch_file  # noqa: E501

        Create file pointers for temporary storage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_scratch_file(proj_key, filename, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str filename: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TemporaryUploadFileResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_project_scratch_file_with_http_info(proj_key, filename, **kwargs)  # noqa: E501

    def create_project_scratch_file_with_http_info(self, proj_key, filename, **kwargs):  # noqa: E501
        """create_project_scratch_file  # noqa: E501

        Create file pointers for temporary storage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_project_scratch_file_with_http_info(proj_key, filename, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str filename: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TemporaryUploadFileResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'filename'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_project_scratch_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `create_project_scratch_file`")  # noqa: E501
        # verify the required parameter 'filename' is set
        if self.api_client.client_side_validation and ('filename' not in local_var_params or  # noqa: E501
                                                        local_var_params['filename'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `filename` when calling `create_project_scratch_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501
        if 'filename' in local_var_params:
            path_params['filename'] = local_var_params['filename']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/scratch/files/upload/{filename}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TemporaryUploadFileResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_project_scratch_files(self, proj_key, **kwargs):  # noqa: E501
        """list_project_scratch_files  # noqa: E501

        Get temporary files uploaded to a project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_scratch_files(proj_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str scratch_ids:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[UploadedFile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_project_scratch_files_with_http_info(proj_key, **kwargs)  # noqa: E501

    def list_project_scratch_files_with_http_info(self, proj_key, **kwargs):  # noqa: E501
        """list_project_scratch_files  # noqa: E501

        Get temporary files uploaded to a project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_project_scratch_files_with_http_info(proj_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param str scratch_ids:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[UploadedFile], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'scratch_ids'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_project_scratch_files" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `list_project_scratch_files`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []
        if 'scratch_ids' in local_var_params and local_var_params['scratch_ids'] is not None:  # noqa: E501
            query_params.append(('scratch_ids', local_var_params['scratch_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/scratch/files', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UploadedFile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_project_scratch_file(self, proj_key, file, **kwargs):  # noqa: E501
        """upload_project_scratch_file  # noqa: E501

        Upload a file to temporary storage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_project_scratch_file(proj_key, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param file file: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UploadedFileResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_project_scratch_file_with_http_info(proj_key, file, **kwargs)  # noqa: E501

    def upload_project_scratch_file_with_http_info(self, proj_key, file, **kwargs):  # noqa: E501
        """upload_project_scratch_file  # noqa: E501

        Upload a file to temporary storage  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_project_scratch_file_with_http_info(proj_key, file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str proj_key: (required)
        :param file file: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UploadedFileResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'proj_key',
            'file'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_project_scratch_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'proj_key' is set
        if self.api_client.client_side_validation and ('proj_key' not in local_var_params or  # noqa: E501
                                                        local_var_params['proj_key'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `proj_key` when calling `upload_project_scratch_file`")  # noqa: E501
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in local_var_params or  # noqa: E501
                                                        local_var_params['file'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file` when calling `upload_project_scratch_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'proj_key' in local_var_params:
            path_params['proj_key'] = local_var_params['proj_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/project/{proj_key}/scratch/files', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UploadedFileResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)