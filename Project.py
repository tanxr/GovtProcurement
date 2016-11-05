import pandas as pd
filename = 'government-procurement-via-gebiz'

cols = ['Tender Number', 'Agency', 'Tender Description', 'Award Date', 'Tender Detail Status', 'Supplier Name', 'Total Awarded Amount']
gp = pd.read_csv(filename, index_col='datetime', parse_dates=True)


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url, header=0, names=drink_cols, na_filter=False)
