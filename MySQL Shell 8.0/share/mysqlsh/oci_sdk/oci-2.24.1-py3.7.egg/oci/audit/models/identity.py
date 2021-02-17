# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Identity(object):
    """
    A container object for identity attributes.

    Example:

    -----
    {
    \"principalName\": \"ExampleName\",
    \"principalId\": \"ocid1.user.oc1..<unique_ID>\",
    \"authType\": \"natv\",
    \"callerName\": null,
    \"callerId\": null,
    \"tenantId\": \"ocid1.tenancy.oc1..<unique_ID>\",
    \"ipAddress\": \"172.24.80.88\",
    \"credentials\": null,
    \"userAgent\": \"Jersey/2.23 (HttpUrlConnection 1.8.0_212)\",
    \"consoleSessionId\": null
    }
    -----
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Identity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param principal_name:
            The value to assign to the principal_name property of this Identity.
        :type principal_name: str

        :param principal_id:
            The value to assign to the principal_id property of this Identity.
        :type principal_id: str

        :param auth_type:
            The value to assign to the auth_type property of this Identity.
        :type auth_type: str

        :param caller_name:
            The value to assign to the caller_name property of this Identity.
        :type caller_name: str

        :param caller_id:
            The value to assign to the caller_id property of this Identity.
        :type caller_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this Identity.
        :type tenant_id: str

        :param ip_address:
            The value to assign to the ip_address property of this Identity.
        :type ip_address: str

        :param credentials:
            The value to assign to the credentials property of this Identity.
        :type credentials: str

        :param user_agent:
            The value to assign to the user_agent property of this Identity.
        :type user_agent: str

        :param console_session_id:
            The value to assign to the console_session_id property of this Identity.
        :type console_session_id: str

        """
        self.swagger_types = {
            'principal_name': 'str',
            'principal_id': 'str',
            'auth_type': 'str',
            'caller_name': 'str',
            'caller_id': 'str',
            'tenant_id': 'str',
            'ip_address': 'str',
            'credentials': 'str',
            'user_agent': 'str',
            'console_session_id': 'str'
        }

        self.attribute_map = {
            'principal_name': 'principalName',
            'principal_id': 'principalId',
            'auth_type': 'authType',
            'caller_name': 'callerName',
            'caller_id': 'callerId',
            'tenant_id': 'tenantId',
            'ip_address': 'ipAddress',
            'credentials': 'credentials',
            'user_agent': 'userAgent',
            'console_session_id': 'consoleSessionId'
        }

        self._principal_name = None
        self._principal_id = None
        self._auth_type = None
        self._caller_name = None
        self._caller_id = None
        self._tenant_id = None
        self._ip_address = None
        self._credentials = None
        self._user_agent = None
        self._console_session_id = None

    @property
    def principal_name(self):
        """
        Gets the principal_name of this Identity.
        The name of the user or service. This value is the friendly name associated with `principalId`.

        Example: `ExampleName`


        :return: The principal_name of this Identity.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """
        Sets the principal_name of this Identity.
        The name of the user or service. This value is the friendly name associated with `principalId`.

        Example: `ExampleName`


        :param principal_name: The principal_name of this Identity.
        :type: str
        """
        self._principal_name = principal_name

    @property
    def principal_id(self):
        """
        Gets the principal_id of this Identity.
        The `OCID`__ of the principal.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The principal_id of this Identity.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        """
        Sets the principal_id of this Identity.
        The `OCID`__ of the principal.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param principal_id: The principal_id of this Identity.
        :type: str
        """
        self._principal_id = principal_id

    @property
    def auth_type(self):
        """
        Gets the auth_type of this Identity.
        The type of authentication used.

        Example: `natv`


        :return: The auth_type of this Identity.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """
        Sets the auth_type of this Identity.
        The type of authentication used.

        Example: `natv`


        :param auth_type: The auth_type of this Identity.
        :type: str
        """
        self._auth_type = auth_type

    @property
    def caller_name(self):
        """
        Gets the caller_name of this Identity.
        The name of the user or service. This value is the friendly name associated with `callerId`.


        :return: The caller_name of this Identity.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name):
        """
        Sets the caller_name of this Identity.
        The name of the user or service. This value is the friendly name associated with `callerId`.


        :param caller_name: The caller_name of this Identity.
        :type: str
        """
        self._caller_name = caller_name

    @property
    def caller_id(self):
        """
        Gets the caller_id of this Identity.
        The `OCID`__ of the caller. The caller that made a
        request on behalf of the prinicpal.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The caller_id of this Identity.
        :rtype: str
        """
        return self._caller_id

    @caller_id.setter
    def caller_id(self, caller_id):
        """
        Sets the caller_id of this Identity.
        The `OCID`__ of the caller. The caller that made a
        request on behalf of the prinicpal.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param caller_id: The caller_id of this Identity.
        :type: str
        """
        self._caller_id = caller_id

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this Identity.
        The `OCID`__ of the tenant.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenant_id of this Identity.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this Identity.
        The `OCID`__ of the tenant.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenant_id: The tenant_id of this Identity.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Identity.
        The IP address of the source of the request.

        Example: `172.24.80.88`


        :return: The ip_address of this Identity.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Identity.
        The IP address of the source of the request.

        Example: `172.24.80.88`


        :param ip_address: The ip_address of this Identity.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def credentials(self):
        """
        Gets the credentials of this Identity.
        The credential ID of the user. This value is extracted from the HTTP 'Authorization' request
        header. It consists of the tenantId, userId, and user fingerprint, all delimited by a slash (/).


        :return: The credentials of this Identity.
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this Identity.
        The credential ID of the user. This value is extracted from the HTTP 'Authorization' request
        header. It consists of the tenantId, userId, and user fingerprint, all delimited by a slash (/).


        :param credentials: The credentials of this Identity.
        :type: str
        """
        self._credentials = credentials

    @property
    def user_agent(self):
        """
        Gets the user_agent of this Identity.
        The user agent of the client that made the request.

        Example: `Jersey/2.23 (HttpUrlConnection 1.8.0_212)`


        :return: The user_agent of this Identity.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this Identity.
        The user agent of the client that made the request.

        Example: `Jersey/2.23 (HttpUrlConnection 1.8.0_212)`


        :param user_agent: The user_agent of this Identity.
        :type: str
        """
        self._user_agent = user_agent

    @property
    def console_session_id(self):
        """
        Gets the console_session_id of this Identity.
        This value identifies any Console session associated with this request.


        :return: The console_session_id of this Identity.
        :rtype: str
        """
        return self._console_session_id

    @console_session_id.setter
    def console_session_id(self, console_session_id):
        """
        Sets the console_session_id of this Identity.
        This value identifies any Console session associated with this request.


        :param console_session_id: The console_session_id of this Identity.
        :type: str
        """
        self._console_session_id = console_session_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other