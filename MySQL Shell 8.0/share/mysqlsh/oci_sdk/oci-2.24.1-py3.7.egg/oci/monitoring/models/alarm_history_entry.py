# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmHistoryEntry(object):
    """
    An alarm history entry indicating a description of the entry and the time that the entry occurred.
    If the entry corresponds to a state transition, such as OK to Firing, then the entry also includes a transition timestamp.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmHistoryEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param summary:
            The value to assign to the summary property of this AlarmHistoryEntry.
        :type summary: str

        :param timestamp:
            The value to assign to the timestamp property of this AlarmHistoryEntry.
        :type timestamp: datetime

        :param timestamp_triggered:
            The value to assign to the timestamp_triggered property of this AlarmHistoryEntry.
        :type timestamp_triggered: datetime

        """
        self.swagger_types = {
            'summary': 'str',
            'timestamp': 'datetime',
            'timestamp_triggered': 'datetime'
        }

        self.attribute_map = {
            'summary': 'summary',
            'timestamp': 'timestamp',
            'timestamp_triggered': 'timestampTriggered'
        }

        self._summary = None
        self._timestamp = None
        self._timestamp_triggered = None

    @property
    def summary(self):
        """
        **[Required]** Gets the summary of this AlarmHistoryEntry.
        Description for this alarm history entry. Avoid entering confidential information.

        Example 1 - alarm state history entry: `The alarm state is FIRING`

        Example 2 - alarm state transition history entry: `State transitioned from OK to Firing`


        :return: The summary of this AlarmHistoryEntry.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this AlarmHistoryEntry.
        Description for this alarm history entry. Avoid entering confidential information.

        Example 1 - alarm state history entry: `The alarm state is FIRING`

        Example 2 - alarm state transition history entry: `State transitioned from OK to Firing`


        :param summary: The summary of this AlarmHistoryEntry.
        :type: str
        """
        self._summary = summary

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this AlarmHistoryEntry.
        Timestamp for this alarm history entry. Format defined by RFC3339.

        Example: `2019-02-01T01:02:29.600Z`


        :return: The timestamp of this AlarmHistoryEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AlarmHistoryEntry.
        Timestamp for this alarm history entry. Format defined by RFC3339.

        Example: `2019-02-01T01:02:29.600Z`


        :param timestamp: The timestamp of this AlarmHistoryEntry.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def timestamp_triggered(self):
        """
        Gets the timestamp_triggered of this AlarmHistoryEntry.
        Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing.
        Available for state transition entries only. Note: A three-minute lag for this value accounts for any late-arriving metrics.

        Example: `2019-02-01T0:59:00.789Z`


        :return: The timestamp_triggered of this AlarmHistoryEntry.
        :rtype: datetime
        """
        return self._timestamp_triggered

    @timestamp_triggered.setter
    def timestamp_triggered(self, timestamp_triggered):
        """
        Sets the timestamp_triggered of this AlarmHistoryEntry.
        Timestamp for the transition of the alarm state. For example, the time when the alarm transitioned from OK to Firing.
        Available for state transition entries only. Note: A three-minute lag for this value accounts for any late-arriving metrics.

        Example: `2019-02-01T0:59:00.789Z`


        :param timestamp_triggered: The timestamp_triggered of this AlarmHistoryEntry.
        :type: datetime
        """
        self._timestamp_triggered = timestamp_triggered

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other