# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class TokenServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def check_token_creation_possible(self, space_id, transaction_id, **kwargs):
        """Check If Token Creation Is Possible

        This operation checks if the given transaction can be used to create a token out of it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_token_creation_possible(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The id of the transaction for which we want to check if the token can be created or not. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.check_token_creation_possible_with_http_info(space_id, transaction_id, **kwargs)
        else:
            (data) = self.check_token_creation_possible_with_http_info(space_id, transaction_id, **kwargs)
            return data

    def check_token_creation_possible_with_http_info(self, space_id, transaction_id, **kwargs):
        """Check If Token Creation Is Possible

        This operation checks if the given transaction can be used to create a token out of it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_token_creation_possible_with_http_info(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The id of the transaction for which we want to check if the token can be created or not. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_token_creation_possible" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `check_token_creation_possible`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `check_token_creation_possible`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/check-token-creation-possible', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def count(self, space_id, **kwargs):
        """Count

        Counts the number of items in the database as restricted by the given filter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQueryFilter filter: The filter which restricts the entities which are used to calculate the count.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.count_with_http_info(space_id, **kwargs)
        else:
            (data) = self.count_with_http_info(space_id, **kwargs)
            return data

    def count_with_http_info(self, space_id, **kwargs):
        """Count

        Counts the number of items in the database as restricted by the given filter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_with_http_info(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQueryFilter filter: The filter which restricts the entities which are used to calculate the count.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'filter']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `count`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filter' in params:
            body_params = params['filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/count', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, space_id, entity, **kwargs):
        """Create

        Creates the entity with the given properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(space_id, entity, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TokenCreate entity: The token object with the properties which should be created. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.create_with_http_info(space_id, entity, **kwargs)
        else:
            (data) = self.create_with_http_info(space_id, entity, **kwargs)
            return data

    def create_with_http_info(self, space_id, entity, **kwargs):
        """Create

        Creates the entity with the given properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(space_id, entity, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TokenCreate entity: The token object with the properties which should be created. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'entity']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `create`")
        # verify the required parameter 'entity' is set
        if ('entity' not in params or
                params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `create`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'entity' in params:
            body_params = params['entity']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_token_based_on_transaction(self, space_id, transaction_id, **kwargs):
        """Create Token Based On Transaction

        This operation creates a token for the given transaction and fills it with the stored payment information of the transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_based_on_transaction(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The id of the transaction for which we want to create the token. (required)
        :return: TokenVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.create_token_based_on_transaction_with_http_info(space_id, transaction_id, **kwargs)
        else:
            (data) = self.create_token_based_on_transaction_with_http_info(space_id, transaction_id, **kwargs)
            return data

    def create_token_based_on_transaction_with_http_info(self, space_id, transaction_id, **kwargs):
        """Create Token Based On Transaction

        This operation creates a token for the given transaction and fills it with the stored payment information of the transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_based_on_transaction_with_http_info(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The id of the transaction for which we want to create the token. (required)
        :return: TokenVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_token_based_on_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `create_token_based_on_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `create_token_based_on_transaction`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/create-token-based-on-transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenVersion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_transaction_for_token_update(self, space_id, token_id, **kwargs):
        """Create Transaction for Token Update

        This operation creates a transaction which allows the updating of the provided token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_transaction_for_token_update(space_id, token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int token_id: The id of the token which should be updated. (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.create_transaction_for_token_update_with_http_info(space_id, token_id, **kwargs)
        else:
            (data) = self.create_transaction_for_token_update_with_http_info(space_id, token_id, **kwargs)
            return data

    def create_transaction_for_token_update_with_http_info(self, space_id, token_id, **kwargs):
        """Create Transaction for Token Update

        This operation creates a transaction which allows the updating of the provided token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_transaction_for_token_update_with_http_info(space_id, token_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int token_id: The id of the token which should be updated. (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'token_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_transaction_for_token_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `create_transaction_for_token_update`")
        # verify the required parameter 'token_id' is set
        if ('token_id' not in params or
                params['token_id'] is None):
            raise ValueError("Missing the required parameter `token_id` when calling `create_transaction_for_token_update`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'token_id' in params:
            query_params.append(('tokenId', params['token_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/createTransactionForTokenUpdate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transaction',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, space_id, id, **kwargs):
        """Delete

        Deletes the entity with the given id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.delete_with_http_info(space_id, id, **kwargs)
        else:
            (data) = self.delete_with_http_info(space_id, id, **kwargs)
            return data

    def delete_with_http_info(self, space_id, id, **kwargs):
        """Delete

        Deletes the entity with the given id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `delete`")
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'id' in params:
            body_params = params['id']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_transaction(self, space_id, transaction_id, **kwargs):
        """Process Transaction

        This operation processes the given transaction by using the token associated with the transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_transaction(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The id of the transaction for which we want to check if the token can be created or not. (required)
        :return: Charge
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.process_transaction_with_http_info(space_id, transaction_id, **kwargs)
        else:
            (data) = self.process_transaction_with_http_info(space_id, transaction_id, **kwargs)
            return data

    def process_transaction_with_http_info(self, space_id, transaction_id, **kwargs):
        """Process Transaction

        This operation processes the given transaction by using the token associated with the transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_transaction_with_http_info(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The id of the transaction for which we want to check if the token can be created or not. (required)
        :return: Charge
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `process_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `process_transaction`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/process-transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Charge',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, space_id, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the token which should be returned. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.read_with_http_info(space_id, id, **kwargs)
        else:
            (data) = self.read_with_http_info(space_id, id, **kwargs)
            return data

    def read_with_http_info(self, space_id, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the token which should be returned. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `read`")
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `read`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'id' in params:
            query_params.append(('id', params['id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/read', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, space_id, query, **kwargs):
        """Search

        Searches for the entities as specified by the given query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(space_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQuery query: The query restricts the tokens which are returned by the search. (required)
        :return: list[Token]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.search_with_http_info(space_id, query, **kwargs)
        else:
            (data) = self.search_with_http_info(space_id, query, **kwargs)
            return data

    def search_with_http_info(self, space_id, query, **kwargs):
        """Search

        Searches for the entities as specified by the given query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(space_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQuery query: The query restricts the tokens which are returned by the search. (required)
        :return: list[Token]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'query']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `search`")
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Token]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, space_id, entity, **kwargs):
        """Update

        This updates the entity with the given properties. Only those properties which should be updated can be provided. The 'id' and 'version' are required to identify the entity.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(space_id, entity, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TokenUpdate entity: The object with all the properties which should be updated. The id and the version are required properties. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_with_http_info(space_id, entity, **kwargs)
        else:
            (data) = self.update_with_http_info(space_id, entity, **kwargs)
            return data

    def update_with_http_info(self, space_id, entity, **kwargs):
        """Update

        This updates the entity with the given properties. Only those properties which should be updated can be provided. The 'id' and 'version' are required to identify the entity.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(space_id, entity, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TokenUpdate entity: The object with all the properties which should be updated. The id and the version are required properties. (required)
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'entity']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update`")
        # verify the required parameter 'entity' is set
        if ('entity' not in params or
                params['entity'] is None):
            raise ValueError("Missing the required parameter `entity` when calling `update`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'entity' in params:
            body_params = params['entity']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/token/update', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
