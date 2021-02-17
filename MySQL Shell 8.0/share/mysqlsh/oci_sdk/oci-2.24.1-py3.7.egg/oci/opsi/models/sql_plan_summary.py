# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlPlanSummary(object):
    """
    SQL Plan details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlPlanSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_hash:
            The value to assign to the plan_hash property of this SqlPlanSummary.
        :type plan_hash: int

        :param plan_content:
            The value to assign to the plan_content property of this SqlPlanSummary.
        :type plan_content: str

        """
        self.swagger_types = {
            'plan_hash': 'int',
            'plan_content': 'str'
        }

        self.attribute_map = {
            'plan_hash': 'planHash',
            'plan_content': 'planContent'
        }

        self._plan_hash = None
        self._plan_content = None

    @property
    def plan_hash(self):
        """
        **[Required]** Gets the plan_hash of this SqlPlanSummary.
        Plan hash value for the SQL Execution Plan


        :return: The plan_hash of this SqlPlanSummary.
        :rtype: int
        """
        return self._plan_hash

    @plan_hash.setter
    def plan_hash(self, plan_hash):
        """
        Sets the plan_hash of this SqlPlanSummary.
        Plan hash value for the SQL Execution Plan


        :param plan_hash: The plan_hash of this SqlPlanSummary.
        :type: int
        """
        self._plan_hash = plan_hash

    @property
    def plan_content(self):
        """
        **[Required]** Gets the plan_content of this SqlPlanSummary.
        Plan XML Content


        :return: The plan_content of this SqlPlanSummary.
        :rtype: str
        """
        return self._plan_content

    @plan_content.setter
    def plan_content(self, plan_content):
        """
        Sets the plan_content of this SqlPlanSummary.
        Plan XML Content


        :param plan_content: The plan_content of this SqlPlanSummary.
        :type: str
        """
        self._plan_content = plan_content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
