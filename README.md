<h1 align="center">
  Business Operations Dashboard
</p>

<img src="https://github.com/quentinb28/business-operations-dashboard/blob/main/images/business-operations-dashboard.gif" width=100%>

<p align="center">
 <img src="https://img.shields.io/badge/salesforce-v2018-pink.svg" />
 <img src="https://img.shields.io/badge/soql-v18.0-orange.svg" />
 <img src="https://img.shields.io/badge/python-v3.7-yellow.svg" />
 <img src="https://img.shields.io/badge/tableau-v2019-informational.svg" />
</p>

## Table of Contents

1. [Situation](#Situation)
2. [Techniques](#Techniques)
3. [Action](#Action)
4. [Results](#Results)
5. [Contributing](#Contributing)
6. [Licensing](#Licensing)

## 1. Situation

Investing.com is a financial platform and news website; one of the top three global financial websites in the world. It offers market quotes,information about stocks, futures, options, analysis, commodities, and an economic calendar. Most of the revenue is generated through advertising; Premium and Remnant. The Remnant business models are CPL / CPA / Networks. This implies closing many deals (Countries * Clients) on a regular basis. This may result in cumbersome processes for the team.

## 2. Task

The process was, as follows:

* Extract the relevant data from the Salesforce API.
* Transform the data to make it more readable.
* Load the transformed data as a BigQuery table.

The technique was to extract the relevant data from Salesforce using Python and SOQL and then display that information in an easy-to-read Tableau dashboard. 

## 3. Action

Firstly, the deals data was collected from the Salesforce API using a combination of Python and SOQL (Salesforce Object Query Language). Then the data was cleaned and some substrings were extracted from names for dynamic display purposes. Finally the data was saved to BigQuery as a table and a Tableau dashboard was built from it in an more manageable way.

## 4. Results

This solution enables us to make operations more efficient and to improve the communication between the Business Team and the Operation Team.

## 5. Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

Please keep in mind that some of these projects might not be relevant anymore,
as our processes constantly evolve.

## 6. Licensing

Copyright © Investing.com . All rights reserved.
