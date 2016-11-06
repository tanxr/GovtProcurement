
import pandas as pd
import numpy as np
import csv

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

#Visualisation of data
# 1. Total number of agencies involved
gp_agencies = gp['Agency'].nunique()
#print gp_agencies

# 2. The number of procurements conducted by each agency in 2015
gp_number = gp['Agency'].value_counts()
#print gp_number

# 3. The total awarded amount by each agency in 2015
gp_amount = gp.groupby('Agency')['Total Awarded Amount'].sum().sort_values(ascending=False)
"""Convert awarded amounts into something more readable, e.g. "millions""""
#print gp_amount

# 4. The average value each procurement by each agency in 2015
gp_average_amount = gp.groupby('Agency')['Total Awarded Amount'].mean().sort_values(ascending=False)
#print gp_average_amount
