# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .unified_agent_parser import UnifiedAgentParser
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnifiedAgentSyslogParser(UnifiedAgentParser):
    """
    Syslog Parser.
    """

    #: A constant which can be used with the message_format property of a UnifiedAgentSyslogParser.
    #: This constant has a value of "RFC3164"
    MESSAGE_FORMAT_RFC3164 = "RFC3164"

    #: A constant which can be used with the message_format property of a UnifiedAgentSyslogParser.
    #: This constant has a value of "RFC5424"
    MESSAGE_FORMAT_RFC5424 = "RFC5424"

    #: A constant which can be used with the message_format property of a UnifiedAgentSyslogParser.
    #: This constant has a value of "AUTO"
    MESSAGE_FORMAT_AUTO = "AUTO"

    #: A constant which can be used with the syslog_parser_type property of a UnifiedAgentSyslogParser.
    #: This constant has a value of "STRING"
    SYSLOG_PARSER_TYPE_STRING = "STRING"

    #: A constant which can be used with the syslog_parser_type property of a UnifiedAgentSyslogParser.
    #: This constant has a value of "REGEXP"
    SYSLOG_PARSER_TYPE_REGEXP = "REGEXP"

    def __init__(self, **kwargs):
        """
        Initializes a new UnifiedAgentSyslogParser object with values from keyword arguments. The default value of the :py:attr:`~oci.logging.models.UnifiedAgentSyslogParser.parser_type` attribute
        of this class is ``SYSLOG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_type:
            The value to assign to the parser_type property of this UnifiedAgentSyslogParser.
            Allowed values for this property are: "AUDITD", "JSON", "TSV", "CSV", "NONE", "SYSLOG", "APACHE2", "APACHE_ERROR", "MSGPACK", "REGEXP", "MULTILINE", "GROK", "MULTILINE_GROK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type parser_type: str

        :param field_time_key:
            The value to assign to the field_time_key property of this UnifiedAgentSyslogParser.
        :type field_time_key: str

        :param types:
            The value to assign to the types property of this UnifiedAgentSyslogParser.
        :type types: dict(str, str)

        :param null_value_pattern:
            The value to assign to the null_value_pattern property of this UnifiedAgentSyslogParser.
        :type null_value_pattern: str

        :param is_null_empty_string:
            The value to assign to the is_null_empty_string property of this UnifiedAgentSyslogParser.
        :type is_null_empty_string: bool

        :param is_estimate_current_event:
            The value to assign to the is_estimate_current_event property of this UnifiedAgentSyslogParser.
        :type is_estimate_current_event: bool

        :param is_keep_time_key:
            The value to assign to the is_keep_time_key property of this UnifiedAgentSyslogParser.
        :type is_keep_time_key: bool

        :param timeout_in_milliseconds:
            The value to assign to the timeout_in_milliseconds property of this UnifiedAgentSyslogParser.
        :type timeout_in_milliseconds: int

        :param time_format:
            The value to assign to the time_format property of this UnifiedAgentSyslogParser.
        :type time_format: str

        :param rfc5424_time_format:
            The value to assign to the rfc5424_time_format property of this UnifiedAgentSyslogParser.
        :type rfc5424_time_format: str

        :param message_format:
            The value to assign to the message_format property of this UnifiedAgentSyslogParser.
            Allowed values for this property are: "RFC3164", "RFC5424", "AUTO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type message_format: str

        :param is_with_priority:
            The value to assign to the is_with_priority property of this UnifiedAgentSyslogParser.
        :type is_with_priority: bool

        :param is_support_colonless_ident:
            The value to assign to the is_support_colonless_ident property of this UnifiedAgentSyslogParser.
        :type is_support_colonless_ident: bool

        :param syslog_parser_type:
            The value to assign to the syslog_parser_type property of this UnifiedAgentSyslogParser.
            Allowed values for this property are: "STRING", "REGEXP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type syslog_parser_type: str

        """
        self.swagger_types = {
            'parser_type': 'str',
            'field_time_key': 'str',
            'types': 'dict(str, str)',
            'null_value_pattern': 'str',
            'is_null_empty_string': 'bool',
            'is_estimate_current_event': 'bool',
            'is_keep_time_key': 'bool',
            'timeout_in_milliseconds': 'int',
            'time_format': 'str',
            'rfc5424_time_format': 'str',
            'message_format': 'str',
            'is_with_priority': 'bool',
            'is_support_colonless_ident': 'bool',
            'syslog_parser_type': 'str'
        }

        self.attribute_map = {
            'parser_type': 'parserType',
            'field_time_key': 'fieldTimeKey',
            'types': 'types',
            'null_value_pattern': 'nullValuePattern',
            'is_null_empty_string': 'isNullEmptyString',
            'is_estimate_current_event': 'isEstimateCurrentEvent',
            'is_keep_time_key': 'isKeepTimeKey',
            'timeout_in_milliseconds': 'timeoutInMilliseconds',
            'time_format': 'timeFormat',
            'rfc5424_time_format': 'rfc5424TimeFormat',
            'message_format': 'messageFormat',
            'is_with_priority': 'isWithPriority',
            'is_support_colonless_ident': 'isSupportColonlessIdent',
            'syslog_parser_type': 'syslogParserType'
        }

        self._parser_type = None
        self._field_time_key = None
        self._types = None
        self._null_value_pattern = None
        self._is_null_empty_string = None
        self._is_estimate_current_event = None
        self._is_keep_time_key = None
        self._timeout_in_milliseconds = None
        self._time_format = None
        self._rfc5424_time_format = None
        self._message_format = None
        self._is_with_priority = None
        self._is_support_colonless_ident = None
        self._syslog_parser_type = None
        self._parser_type = 'SYSLOG'

    @property
    def time_format(self):
        """
        Gets the time_format of this UnifiedAgentSyslogParser.

        :return: The time_format of this UnifiedAgentSyslogParser.
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """
        Sets the time_format of this UnifiedAgentSyslogParser.

        :param time_format: The time_format of this UnifiedAgentSyslogParser.
        :type: str
        """
        self._time_format = time_format

    @property
    def rfc5424_time_format(self):
        """
        Gets the rfc5424_time_format of this UnifiedAgentSyslogParser.

        :return: The rfc5424_time_format of this UnifiedAgentSyslogParser.
        :rtype: str
        """
        return self._rfc5424_time_format

    @rfc5424_time_format.setter
    def rfc5424_time_format(self, rfc5424_time_format):
        """
        Sets the rfc5424_time_format of this UnifiedAgentSyslogParser.

        :param rfc5424_time_format: The rfc5424_time_format of this UnifiedAgentSyslogParser.
        :type: str
        """
        self._rfc5424_time_format = rfc5424_time_format

    @property
    def message_format(self):
        """
        Gets the message_format of this UnifiedAgentSyslogParser.
        Allowed values for this property are: "RFC3164", "RFC5424", "AUTO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The message_format of this UnifiedAgentSyslogParser.
        :rtype: str
        """
        return self._message_format

    @message_format.setter
    def message_format(self, message_format):
        """
        Sets the message_format of this UnifiedAgentSyslogParser.

        :param message_format: The message_format of this UnifiedAgentSyslogParser.
        :type: str
        """
        allowed_values = ["RFC3164", "RFC5424", "AUTO"]
        if not value_allowed_none_or_none_sentinel(message_format, allowed_values):
            message_format = 'UNKNOWN_ENUM_VALUE'
        self._message_format = message_format

    @property
    def is_with_priority(self):
        """
        Gets the is_with_priority of this UnifiedAgentSyslogParser.

        :return: The is_with_priority of this UnifiedAgentSyslogParser.
        :rtype: bool
        """
        return self._is_with_priority

    @is_with_priority.setter
    def is_with_priority(self, is_with_priority):
        """
        Sets the is_with_priority of this UnifiedAgentSyslogParser.

        :param is_with_priority: The is_with_priority of this UnifiedAgentSyslogParser.
        :type: bool
        """
        self._is_with_priority = is_with_priority

    @property
    def is_support_colonless_ident(self):
        """
        Gets the is_support_colonless_ident of this UnifiedAgentSyslogParser.

        :return: The is_support_colonless_ident of this UnifiedAgentSyslogParser.
        :rtype: bool
        """
        return self._is_support_colonless_ident

    @is_support_colonless_ident.setter
    def is_support_colonless_ident(self, is_support_colonless_ident):
        """
        Sets the is_support_colonless_ident of this UnifiedAgentSyslogParser.

        :param is_support_colonless_ident: The is_support_colonless_ident of this UnifiedAgentSyslogParser.
        :type: bool
        """
        self._is_support_colonless_ident = is_support_colonless_ident

    @property
    def syslog_parser_type(self):
        """
        Gets the syslog_parser_type of this UnifiedAgentSyslogParser.
        Allowed values for this property are: "STRING", "REGEXP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The syslog_parser_type of this UnifiedAgentSyslogParser.
        :rtype: str
        """
        return self._syslog_parser_type

    @syslog_parser_type.setter
    def syslog_parser_type(self, syslog_parser_type):
        """
        Sets the syslog_parser_type of this UnifiedAgentSyslogParser.

        :param syslog_parser_type: The syslog_parser_type of this UnifiedAgentSyslogParser.
        :type: str
        """
        allowed_values = ["STRING", "REGEXP"]
        if not value_allowed_none_or_none_sentinel(syslog_parser_type, allowed_values):
            syslog_parser_type = 'UNKNOWN_ENUM_VALUE'
        self._syslog_parser_type = syslog_parser_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
