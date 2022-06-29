# -*- coding: utf-8 -*-

"""
apimaticcalculator

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimaticcalculator.api_helper import APIHelper
from apimaticcalculator.configuration import Server
from apimaticcalculator.controllers.base_controller import BaseController


class SimpleCalculatorController(BaseController):

    """A Controller to access Endpoints in the apimaticcalculator API."""
    def __init__(self, config):
        super(SimpleCalculatorController, self).__init__(config)

    def get_calculate(self,
                      options=dict()):
        """Does a GET request to /{operation}.

        Calculates the expression using the specified operation.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    operation -- OperationTypeEnum -- The operator to apply on
                        the variables
                    x -- float -- The LHS value
                    y -- float -- The RHS value

        Returns:
            float: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/{operation}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'operation': {'value': options.get('operation', None), 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'x': options.get('x', None),
            'y': options.get('y', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = float(_response.text)

        return decoded