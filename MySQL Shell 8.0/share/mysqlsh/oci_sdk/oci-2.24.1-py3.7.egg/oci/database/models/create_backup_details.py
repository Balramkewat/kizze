# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackupDetails(object):
    """
    Details for creating a database backup.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_id:
            The value to assign to the database_id property of this CreateBackupDetails.
        :type database_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateBackupDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'database_id': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'database_id': 'databaseId',
            'display_name': 'displayName'
        }

        self._database_id = None
        self._display_name = None

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this CreateBackupDetails.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this CreateBackupDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreateBackupDetails.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this CreateBackupDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateBackupDetails.
        The user-friendly name for the backup. The name does not have to be unique.


        :return: The display_name of this CreateBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBackupDetails.
        The user-friendly name for the backup. The name does not have to be unique.


        :param display_name: The display_name of this CreateBackupDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other