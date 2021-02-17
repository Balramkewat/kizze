# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    Many of the API requests you use to create and configure load balancing do not take effect immediately.
    In these cases, the request spawns an asynchronous work flow to fulfill the request. WorkRequest objects provide visibility
    for in-progress work flows.
    For more information about work requests, see `Viewing the State of a Work Request`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/viewingworkrequest.htm
    """

    #: A constant which can be used with the lifecycle_state property of a WorkRequest.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a WorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a WorkRequest.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a WorkRequest.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequest.
        :type id: str

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this WorkRequest.
        :type load_balancer_id: str

        :param type:
            The value to assign to the type property of this WorkRequest.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequest.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param message:
            The value to assign to the message property of this WorkRequest.
        :type message: str

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequest.
        :type time_accepted: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequest.
        :type time_finished: datetime

        :param error_details:
            The value to assign to the error_details property of this WorkRequest.
        :type error_details: list[WorkRequestError]

        """
        self.swagger_types = {
            'id': 'str',
            'load_balancer_id': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'message': 'str',
            'time_accepted': 'datetime',
            'time_finished': 'datetime',
            'error_details': 'list[WorkRequestError]'
        }

        self.attribute_map = {
            'id': 'id',
            'load_balancer_id': 'loadBalancerId',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'message': 'message',
            'time_accepted': 'timeAccepted',
            'time_finished': 'timeFinished',
            'error_details': 'errorDetails'
        }

        self._id = None
        self._load_balancer_id = None
        self._type = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._message = None
        self._time_accepted = None
        self._time_finished = None
        self._error_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The `OCID`__ of the work request.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The `OCID`__ of the work request.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this WorkRequest.
        The `OCID`__ of the load balancer with which the work request
        is associated.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this WorkRequest.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this WorkRequest.
        The `OCID`__ of the load balancer with which the work request
        is associated.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this WorkRequest.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this WorkRequest.
        The type of action the work request represents.

        Example: `CreateListener`


        :return: The type of this WorkRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkRequest.
        The type of action the work request represents.

        Example: `CreateListener`


        :param type: The type of this WorkRequest.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WorkRequest.
        The `OCID`__ of the compartment containing the load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The `OCID`__ of the compartment containing the load balancer.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this WorkRequest.
        The current state of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WorkRequest.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WorkRequest.
        The current state of the work request.


        :param lifecycle_state: The lifecycle_state of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequest.
        A collection of data, related to the load balancer provisioning process, that helps with debugging in the event of failure.
        Possible data elements include:

        - workflow name
        - event ID
        - work request ID
        - load balancer ID
        - workflow completion message


        :return: The message of this WorkRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequest.
        A collection of data, related to the load balancer provisioning process, that helps with debugging in the event of failure.
        Possible data elements include:

        - workflow name
        - event ID
        - work request ID
        - load balancer ID
        - workflow completion message


        :param message: The message of this WorkRequest.
        :type: str
        """
        self._message = message

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequest.
        The date and time the work request was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time the work request was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The date and time the work request was completed, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the work request was completed, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_finished: The time_finished of this WorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def error_details(self):
        """
        **[Required]** Gets the error_details of this WorkRequest.

        :return: The error_details of this WorkRequest.
        :rtype: list[WorkRequestError]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this WorkRequest.

        :param error_details: The error_details of this WorkRequest.
        :type: list[WorkRequestError]
        """
        self._error_details = error_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
