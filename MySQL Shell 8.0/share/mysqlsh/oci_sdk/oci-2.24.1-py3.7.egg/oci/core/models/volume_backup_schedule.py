# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeBackupSchedule(object):
    """
    Defines the backup frequency and retention period for a volume backup policy. For more information,
    see `Policy-Based Backups`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm
    """

    #: A constant which can be used with the backup_type property of a VolumeBackupSchedule.
    #: This constant has a value of "FULL"
    BACKUP_TYPE_FULL = "FULL"

    #: A constant which can be used with the backup_type property of a VolumeBackupSchedule.
    #: This constant has a value of "INCREMENTAL"
    BACKUP_TYPE_INCREMENTAL = "INCREMENTAL"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_HOUR"
    PERIOD_ONE_HOUR = "ONE_HOUR"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_DAY"
    PERIOD_ONE_DAY = "ONE_DAY"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_WEEK"
    PERIOD_ONE_WEEK = "ONE_WEEK"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_MONTH"
    PERIOD_ONE_MONTH = "ONE_MONTH"

    #: A constant which can be used with the period property of a VolumeBackupSchedule.
    #: This constant has a value of "ONE_YEAR"
    PERIOD_ONE_YEAR = "ONE_YEAR"

    #: A constant which can be used with the offset_type property of a VolumeBackupSchedule.
    #: This constant has a value of "STRUCTURED"
    OFFSET_TYPE_STRUCTURED = "STRUCTURED"

    #: A constant which can be used with the offset_type property of a VolumeBackupSchedule.
    #: This constant has a value of "NUMERIC_SECONDS"
    OFFSET_TYPE_NUMERIC_SECONDS = "NUMERIC_SECONDS"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    #: A constant which can be used with the day_of_week property of a VolumeBackupSchedule.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "JANUARY"
    MONTH_JANUARY = "JANUARY"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "FEBRUARY"
    MONTH_FEBRUARY = "FEBRUARY"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "MARCH"
    MONTH_MARCH = "MARCH"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "APRIL"
    MONTH_APRIL = "APRIL"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "MAY"
    MONTH_MAY = "MAY"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "JUNE"
    MONTH_JUNE = "JUNE"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "JULY"
    MONTH_JULY = "JULY"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "AUGUST"
    MONTH_AUGUST = "AUGUST"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "SEPTEMBER"
    MONTH_SEPTEMBER = "SEPTEMBER"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "OCTOBER"
    MONTH_OCTOBER = "OCTOBER"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "NOVEMBER"
    MONTH_NOVEMBER = "NOVEMBER"

    #: A constant which can be used with the month property of a VolumeBackupSchedule.
    #: This constant has a value of "DECEMBER"
    MONTH_DECEMBER = "DECEMBER"

    #: A constant which can be used with the time_zone property of a VolumeBackupSchedule.
    #: This constant has a value of "UTC"
    TIME_ZONE_UTC = "UTC"

    #: A constant which can be used with the time_zone property of a VolumeBackupSchedule.
    #: This constant has a value of "REGIONAL_DATA_CENTER_TIME"
    TIME_ZONE_REGIONAL_DATA_CENTER_TIME = "REGIONAL_DATA_CENTER_TIME"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeBackupSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_type:
            The value to assign to the backup_type property of this VolumeBackupSchedule.
            Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_type: str

        :param offset_seconds:
            The value to assign to the offset_seconds property of this VolumeBackupSchedule.
        :type offset_seconds: int

        :param period:
            The value to assign to the period property of this VolumeBackupSchedule.
            Allowed values for this property are: "ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type period: str

        :param offset_type:
            The value to assign to the offset_type property of this VolumeBackupSchedule.
            Allowed values for this property are: "STRUCTURED", "NUMERIC_SECONDS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type offset_type: str

        :param hour_of_day:
            The value to assign to the hour_of_day property of this VolumeBackupSchedule.
        :type hour_of_day: int

        :param day_of_week:
            The value to assign to the day_of_week property of this VolumeBackupSchedule.
            Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type day_of_week: str

        :param day_of_month:
            The value to assign to the day_of_month property of this VolumeBackupSchedule.
        :type day_of_month: int

        :param month:
            The value to assign to the month property of this VolumeBackupSchedule.
            Allowed values for this property are: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type month: str

        :param retention_seconds:
            The value to assign to the retention_seconds property of this VolumeBackupSchedule.
        :type retention_seconds: int

        :param time_zone:
            The value to assign to the time_zone property of this VolumeBackupSchedule.
            Allowed values for this property are: "UTC", "REGIONAL_DATA_CENTER_TIME", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type time_zone: str

        """
        self.swagger_types = {
            'backup_type': 'str',
            'offset_seconds': 'int',
            'period': 'str',
            'offset_type': 'str',
            'hour_of_day': 'int',
            'day_of_week': 'str',
            'day_of_month': 'int',
            'month': 'str',
            'retention_seconds': 'int',
            'time_zone': 'str'
        }

        self.attribute_map = {
            'backup_type': 'backupType',
            'offset_seconds': 'offsetSeconds',
            'period': 'period',
            'offset_type': 'offsetType',
            'hour_of_day': 'hourOfDay',
            'day_of_week': 'dayOfWeek',
            'day_of_month': 'dayOfMonth',
            'month': 'month',
            'retention_seconds': 'retentionSeconds',
            'time_zone': 'timeZone'
        }

        self._backup_type = None
        self._offset_seconds = None
        self._period = None
        self._offset_type = None
        self._hour_of_day = None
        self._day_of_week = None
        self._day_of_month = None
        self._month = None
        self._retention_seconds = None
        self._time_zone = None

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this VolumeBackupSchedule.
        The type of volume backup to create.

        Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_type of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this VolumeBackupSchedule.
        The type of volume backup to create.


        :param backup_type: The backup_type of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(backup_type, allowed_values):
            backup_type = 'UNKNOWN_ENUM_VALUE'
        self._backup_type = backup_type

    @property
    def offset_seconds(self):
        """
        Gets the offset_seconds of this VolumeBackupSchedule.
        The number of seconds that the volume backup start time should be shifted from the default interval boundaries specified by the period. The volume backup start time is the frequency start time plus the offset.


        :return: The offset_seconds of this VolumeBackupSchedule.
        :rtype: int
        """
        return self._offset_seconds

    @offset_seconds.setter
    def offset_seconds(self, offset_seconds):
        """
        Sets the offset_seconds of this VolumeBackupSchedule.
        The number of seconds that the volume backup start time should be shifted from the default interval boundaries specified by the period. The volume backup start time is the frequency start time plus the offset.


        :param offset_seconds: The offset_seconds of this VolumeBackupSchedule.
        :type: int
        """
        self._offset_seconds = offset_seconds

    @property
    def period(self):
        """
        **[Required]** Gets the period of this VolumeBackupSchedule.
        The volume backup frequency.

        Allowed values for this property are: "ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The period of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this VolumeBackupSchedule.
        The volume backup frequency.


        :param period: The period of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH", "ONE_YEAR"]
        if not value_allowed_none_or_none_sentinel(period, allowed_values):
            period = 'UNKNOWN_ENUM_VALUE'
        self._period = period

    @property
    def offset_type(self):
        """
        Gets the offset_type of this VolumeBackupSchedule.
        Indicates how the offset is defined. If value is `STRUCTURED`, then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used and `offsetSeconds` will be ignored in requests and users should ignore its value from the responses.

        `hourOfDay` is applicable for periods `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`.

        `dayOfWeek` is applicable for period `ONE_WEEK`.

        `dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`.

        'month' is applicable for period 'ONE_YEAR'.

        They will be ignored in the requests for inapplicable periods.

        If value is `NUMERIC_SECONDS`, then `offsetSeconds` will be used for both requests and responses and the structured fields will be ignored in the requests and users should ignore their values from the responses.

        For clients using older versions of Apis and not sending `offsetType` in their requests, the behaviour is just like `NUMERIC_SECONDS`.

        Allowed values for this property are: "STRUCTURED", "NUMERIC_SECONDS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The offset_type of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._offset_type

    @offset_type.setter
    def offset_type(self, offset_type):
        """
        Sets the offset_type of this VolumeBackupSchedule.
        Indicates how the offset is defined. If value is `STRUCTURED`, then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used and `offsetSeconds` will be ignored in requests and users should ignore its value from the responses.

        `hourOfDay` is applicable for periods `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`.

        `dayOfWeek` is applicable for period `ONE_WEEK`.

        `dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`.

        'month' is applicable for period 'ONE_YEAR'.

        They will be ignored in the requests for inapplicable periods.

        If value is `NUMERIC_SECONDS`, then `offsetSeconds` will be used for both requests and responses and the structured fields will be ignored in the requests and users should ignore their values from the responses.

        For clients using older versions of Apis and not sending `offsetType` in their requests, the behaviour is just like `NUMERIC_SECONDS`.


        :param offset_type: The offset_type of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["STRUCTURED", "NUMERIC_SECONDS"]
        if not value_allowed_none_or_none_sentinel(offset_type, allowed_values):
            offset_type = 'UNKNOWN_ENUM_VALUE'
        self._offset_type = offset_type

    @property
    def hour_of_day(self):
        """
        Gets the hour_of_day of this VolumeBackupSchedule.
        The hour of the day to schedule the volume backup.


        :return: The hour_of_day of this VolumeBackupSchedule.
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        """
        Sets the hour_of_day of this VolumeBackupSchedule.
        The hour of the day to schedule the volume backup.


        :param hour_of_day: The hour_of_day of this VolumeBackupSchedule.
        :type: int
        """
        self._hour_of_day = hour_of_day

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this VolumeBackupSchedule.
        The day of the week to schedule the volume backup.

        Allowed values for this property are: "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The day_of_week of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this VolumeBackupSchedule.
        The day of the week to schedule the volume backup.


        :param day_of_week: The day_of_week of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            day_of_week = 'UNKNOWN_ENUM_VALUE'
        self._day_of_week = day_of_week

    @property
    def day_of_month(self):
        """
        Gets the day_of_month of this VolumeBackupSchedule.
        The day of the month to schedule the volume backup.


        :return: The day_of_month of this VolumeBackupSchedule.
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """
        Sets the day_of_month of this VolumeBackupSchedule.
        The day of the month to schedule the volume backup.


        :param day_of_month: The day_of_month of this VolumeBackupSchedule.
        :type: int
        """
        self._day_of_month = day_of_month

    @property
    def month(self):
        """
        Gets the month of this VolumeBackupSchedule.
        The month of the year to schedule the volume backup.

        Allowed values for this property are: "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The month of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """
        Sets the month of this VolumeBackupSchedule.
        The month of the year to schedule the volume backup.


        :param month: The month of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        if not value_allowed_none_or_none_sentinel(month, allowed_values):
            month = 'UNKNOWN_ENUM_VALUE'
        self._month = month

    @property
    def retention_seconds(self):
        """
        **[Required]** Gets the retention_seconds of this VolumeBackupSchedule.
        How long, in seconds, to keep the volume backups created by this schedule.


        :return: The retention_seconds of this VolumeBackupSchedule.
        :rtype: int
        """
        return self._retention_seconds

    @retention_seconds.setter
    def retention_seconds(self, retention_seconds):
        """
        Sets the retention_seconds of this VolumeBackupSchedule.
        How long, in seconds, to keep the volume backups created by this schedule.


        :param retention_seconds: The retention_seconds of this VolumeBackupSchedule.
        :type: int
        """
        self._retention_seconds = retention_seconds

    @property
    def time_zone(self):
        """
        Gets the time_zone of this VolumeBackupSchedule.
        Specifies what time zone is the schedule in

        Allowed values for this property are: "UTC", "REGIONAL_DATA_CENTER_TIME", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The time_zone of this VolumeBackupSchedule.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this VolumeBackupSchedule.
        Specifies what time zone is the schedule in


        :param time_zone: The time_zone of this VolumeBackupSchedule.
        :type: str
        """
        allowed_values = ["UTC", "REGIONAL_DATA_CENTER_TIME"]
        if not value_allowed_none_or_none_sentinel(time_zone, allowed_values):
            time_zone = 'UNKNOWN_ENUM_VALUE'
        self._time_zone = time_zone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other