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

from src.query_soql import get_query
from src.gcp_function import gcp_function


if __name__ == '__main__':

    # Get query soql
    query_soql = get_query()

    # Execute gcp function
    gcp_function(query_soql)
