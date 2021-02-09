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

import pandas as pd
import google.cloud.bigquery as bigquery
from src.salesforcemethods_class import SalesforceMethods
from src.gcp_bigquery import save_to_bq


# Define function get_country_codes

def get_country_codes(df):

    # Instantiate client
    client = bigquery.Client(project='madrid-investing')

    # Build query sql
    query_sql = """select * from `madrid-investing.DATA_LAKE_MODELING_US.countries`"""

    # Get results
    __res = client.query(query_sql).result()

    # Convert to dataframe
    __df = __res.to_dataframe()

    # Merge with df
    return df.merge(__df,
                    how='left',
                    left_on='Geo_Targeting',
                    right_on='country_name')


# Define function gcp_function

def gcp_function(query_soql):

    # Instantiate SalesforceMethods object
    __sfc = SalesforceMethods()

    # Query Salesforce
    __res = __sfc.sf.client.query_all(query=query_soql)

    # Save records in a dataframe
    df = pd.DataFrame(__res['records'])

    # Drop irrelevant columns
    df.drop(columns=['attributes', 'Opportunity'], inplace=True)

    # Clean column names
    df.columns = [__c.split('__c')[0] for __c in df.columns]

    # Add column product
    df['Product'] = df['Name'].apply(lambda x: 'POPUP' if 'promotion' in x.lower() else 'TNB')

    # Add country data
    df = get_country_codes(df)

    # Save to BigQuery
    save_to_bq(
        df,
        project='madrid-investing',
        dataset='DATA_LAKE_MODELING_US',
        filename='__testq'  # 'sf_active_deals'
    )
