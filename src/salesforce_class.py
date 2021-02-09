
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

from simple_salesforce import Salesforce as Sf


# Define Salesforce class

class Salesforce:

    # Try to init the client
    def __init__(self, credentials):

        # Generate internal configuration
        self.cfg = {
            'credentials': credentials
        }

        self.client = Sf(**self.cfg['credentials'])
