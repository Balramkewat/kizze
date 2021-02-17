# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceSummaryReport(object):
    """
    SourceSummaryReport
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SourceSummaryReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param non_oob_count:
            The value to assign to the non_oob_count property of this SourceSummaryReport.
        :type non_oob_count: int

        :param auto_association_source_count:
            The value to assign to the auto_association_source_count property of this SourceSummaryReport.
        :type auto_association_source_count: int

        :param oob_count:
            The value to assign to the oob_count property of this SourceSummaryReport.
        :type oob_count: int

        """
        self.swagger_types = {
            'non_oob_count': 'int',
            'auto_association_source_count': 'int',
            'oob_count': 'int'
        }

        self.attribute_map = {
            'non_oob_count': 'nonOobCount',
            'auto_association_source_count': 'autoAssociationSourceCount',
            'oob_count': 'oobCount'
        }

        self._non_oob_count = None
        self._auto_association_source_count = None
        self._oob_count = None

    @property
    def non_oob_count(self):
        """
        Gets the non_oob_count of this SourceSummaryReport.
        non out-of-the-box count


        :return: The non_oob_count of this SourceSummaryReport.
        :rtype: int
        """
        return self._non_oob_count

    @non_oob_count.setter
    def non_oob_count(self, non_oob_count):
        """
        Sets the non_oob_count of this SourceSummaryReport.
        non out-of-the-box count


        :param non_oob_count: The non_oob_count of this SourceSummaryReport.
        :type: int
        """
        self._non_oob_count = non_oob_count

    @property
    def auto_association_source_count(self):
        """
        Gets the auto_association_source_count of this SourceSummaryReport.
        count of sources set to auto-associate


        :return: The auto_association_source_count of this SourceSummaryReport.
        :rtype: int
        """
        return self._auto_association_source_count

    @auto_association_source_count.setter
    def auto_association_source_count(self, auto_association_source_count):
        """
        Sets the auto_association_source_count of this SourceSummaryReport.
        count of sources set to auto-associate


        :param auto_association_source_count: The auto_association_source_count of this SourceSummaryReport.
        :type: int
        """
        self._auto_association_source_count = auto_association_source_count

    @property
    def oob_count(self):
        """
        Gets the oob_count of this SourceSummaryReport.
        out-of-the-box count


        :return: The oob_count of this SourceSummaryReport.
        :rtype: int
        """
        return self._oob_count

    @oob_count.setter
    def oob_count(self, oob_count):
        """
        Sets the oob_count of this SourceSummaryReport.
        out-of-the-box count


        :param oob_count: The oob_count of this SourceSummaryReport.
        :type: int
        """
        self._oob_count = oob_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
