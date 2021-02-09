
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

from src.settings import Settings
from src.salesforce_class import Salesforce


# Define SalesforceMethods class

class SalesforceMethods:

    def __init__(self):

        # Declare settings
        self.cfg = Settings()

        # Declare library
        self.sf = Salesforce(self.cfg.get_salesforce_credentials())
