
import pandas as pd
pd.set_option('display.width',5000)

import numpy as np
import csv


#Visualisation Libraries
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14
pd.set_option('display.max_columns', 5)

#Open CSV file containing - Singapore Government Procurement Record for 2015
#Source: data.gov.sg
filename = '/Users/xuanrong/mystuff/git/GovtProcurement/government-procurement/government-procurement-via-gebiz-2015.csv'
cols = ['Tender Number', 'Agency', 'Tender Description', 'Award Date', 'Tender Detail Status', 'Supplier Name', 'Total Awarded Amount']
gp = pd.read_csv(filename, header=0, names=cols)


#(FOR TESTING) Code to open test file (small set of original csv file)
#filename = '/Users/xuanrong/mystuff/git/GovtProcurement/test.csv'
#cols = ['Tender Number', 'Agency', 'Tender Description', 'Award Date', 'Tender Detail Status', 'Supplier Name', 'Total Awarded Amount']
#gp = pd.read_csv(filename, header=0, names=cols)

#Obtain Misc. Info about Dataset
#print gp.head()
#print gp.info()
#print gp.dtypes

# A. Visualisation of raw dataset
#   1. Total number of agencies involved
gp_agencies = gp['Agency'].nunique()
#print gp_agencies

#   2. The number of procurements conducted by each agency in 2015
gp_number = gp['Agency'].value_counts()
#print gp_number
#Create bar chart of top 10 agencies by procurement numbers
#gp.Agency.value_counts().head(10).plot(kind='bar')
#plt.savefig("Number_gp", format='pdf')


#   3. The total awarded amount by each agency in 2015
gp_amount = gp.groupby('Agency')['Total Awarded Amount'].sum().sort_values(ascending=False)
"""Convert awarded amounts into something more readable, e.g. 25 million, instead of 2.5e7"""
#print gp_amount
#print out chart


#   4. The average value each procurement by each agency in 2015
gp_average_amount = gp.groupby('Agency')['Total Awarded Amount'].mean().sort_values(ascending=False)
#print gp_average_amount

# 5. List out all procurements by specified agency in 2015
specified_agency = 'Infocommunications Development Authority of Singapore'
agency_gp_amount = gp[gp.Agency == specified_agency]['Total Awarded Amount'].sum()
print "%s procured goods and services worth a total of $%d in 2015." % (specified_agency, agency_gp_amount)
print gp[gp.Agency == specified_agency][['Tender Description','Supplier Name','Total Awarded Amount']]


# B. Cleaning of Dataset
#   1. Remove supposedly erroneous entries (e.g. expensive catering by DSTA)
