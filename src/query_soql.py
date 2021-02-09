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


# Define function get_query

def get_query():

    return """
    
    SELECT
    Opportunity.StageName,
    Name,
    Account_Name__c,
    Brand__c,
    Geo_Targeting__c,
    Model__c,
    Lead_Type__c,
    Quantity__c,
    Daily_Quantity_Capping__c,
    Net_Sales_Price__c,
    Opportunity_Currency__c,
    Include_English_Editions__c,
    Risk_Warning_Status__c,
    URL__c,
    Affiliate_ID__c,
    Offer_ID__c,
    Button_CTA__c,
    Postback_Status__c,
    Item_Start_Date__c,
    Item_End_Date__c,
    IO_Number__c,
    Line_Number__c,
    RevOps_Status__c,
    Remnant_Ops_Status__c,
    Opportunity_ID__c
    FROM OpportunityLineItem
    WHERE (
    (Name LIKE '%Affiliation%' OR Name LIKE '%Promotion%') AND
    (NOT Name LIKE '%Comparison Tables%') AND 
    (NOT Account_Name__c LIKE '%Test%') AND
    (NOT Name LIKE 'CN backfill internal promotion%') AND 
    (NOT Name LIKE '%Comparison%') AND
    (Opportunity.StageName LIKE 'Closed Won') AND
    (NOT RevOps_Status__c LIKE 'Inventory Released'))
    
    """
