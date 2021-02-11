
# !/usr/bin/env python
# ! -*- coding: utf-8 -*-

"""
   Copyright © Investing.com
   Licensed under Private License.
   See LICENSE file for more information.
"""

#################################################

# Project: Create BQ table of Active Deals from Salesforce
# This file does the following:
# - retrieve all filtered product lines in Salesforce
# - organize and save them as a BQ table: sf_active_deals

#################################################


# Libraries

import json


# Define Settings class

class Settings:

    @staticmethod
    def get_salesforce_credentials():

        # Retrieve login parameters from config file
        with open('/Users/quentinbracq/Desktop/pycharmprojects/credentials/config.json') as credentials:
            credentials = json.load(credentials)

        # Get environment variables
        return {
            'username': credentials['salesforce']['username'],
            'password': credentials['salesforce']['password'],
            'security_token': credentials['salesforce']['security_token'],
        }
