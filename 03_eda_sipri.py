# EDA for the sipri dataset

import pandas as pd
import pandas_profiling
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
%matplotlib inline

# Suppress scientific notation (show up to 3 decimals)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Read the data
military_data = pd.read_csv('wb_data\military_data.csv')

# Understand the dataset
military_data.head()
military_data.dtypes
military_data.info()

# Descriptive statistscs 
military_data.describe(include=[float]) # numeric
military_data.describe(include=[object]) # categorical
military_data['country_iso3'].value_counts()  # categories

# Descriptive by group
military_data.groupby('country_name').describe(include=[float]) 
military_data.groupby('country_name').describe(include=[object]) 

# Null values
military_data.isna().sum()


# Profile the data with pandas_profiling 
profile = pandas_profiling.ProfileReport(military_data)
profile
profile.to_notebook_iframe()
profile.to_file('wb_data/data_profiling.html')


# Plotting with plotly
# Line chart (by year)
px.line(data_frame=military_data, x='year', y='milex_usd', color='country_name')

# Pie charts for min and max year
military_max_year = military_data[military_data.year==max(military_data.year)]
military_min_year = military_data[military_data.year==min(military_data.year)]

px.pie(data_frame=military_max_year, names='country_name', values='milex_usd')
