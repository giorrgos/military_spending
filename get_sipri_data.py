# Get Military Data from World Bank
from operator import index
import pandas as pd
import wbgapi as wb

# Info about the available data
help(wb)
wb.source.info()
all_series = wb.series.info()
print(all_series)

# Find World Bank codes of interest
wb.series.info(q='military')
wb.series.info(q='arm')

# Create a dictionary for mapping purposes later
tmp_dict = {
    'wb_series_code': ['MS.MIL.XPND.CD', 'MS.MIL.XPND.GD.ZS', 'MS.MIL.XPND.ZS',
                       'MS.MIL.MPRT.KD', 'MS.MIL.XPRT.KD', 'MS.MIL.TOTL.P1', 'MS.MIL.TOTL.TF.ZS'],
    'wb_series_name': ['Military expenditure (current USD)','Military expenditure (% of GDP)', 
                       'Military expenditure (% of general government expenditure)',
                       'Arms imports (SIPRI trend indicator values)', 'Arms exports (SIPRI trend indicator values)',
                       'Armed forces personnel, total', 'Armed forces personnel (% of total labor force)'],
    'wb_indicator':   ['milex_usd', 'milex_pct_gdp', 'milex_pct_gov_exp',
                       'arms_imports', 'arms_exports', 'armed_forces_total', 'armed_forces_pct_labour']    
        }
type(tmp_dict)

# Convert dictionary into a dataframe for easier mapping
map_codes = pd.DataFrame(tmp_dict)
map_codes.head()
list(map_codes['wb_series_code'])
list(map_codes['wb_indicator'])

# Remove temp_dict from memory
del tmp_dict

# GET the data from the World Bank
get_wb_military = wb.data.DataFrame( 
    series = list(map_codes['wb_series_code']),
    economy = ['CAN', 'USA'],   
    time = range(2018, 2021),   
    numericTimeKeys = True, 
    labels = True
    )
get_wb_military.head()
get_wb_military.info()
# bring index (country_code) as a column
get_wb_military.reset_index(inplace=True)
get_wb_military.head()
get_wb_military.info()

# Map the code_friendly names and drop series code & description
get_wb_military = get_wb_military.merge(map_codes, how='left', left_on='series', right_on='wb_series_code')
get_wb_military.head()
get_wb_military = get_wb_military.drop(columns=['Series', 'wb_series_name', 'wb_series_code'])
get_wb_military = get_wb_military.rename(columns={'economy':'country_iso3', 'Country':'country_name'})
get_wb_military.head()

# Data transformation - have series as columns
# Pivot Longer (aka melt) - make year into a column 
military_long = get_wb_military.melt(
    id_vars=['country_iso3', 'country_name', 'wb_indicator'],
    value_vars=[2018, 2019, 2020],
    var_name='year',
    value_name='value' 
)
military_long.head()

# Pivot wider (aka pivot) - make series into columns
military_data = military_long.pivot(
    index=['country_iso3', 'country_name', 'year'],
    columns='wb_indicator',
    values='value'
)
military_data.head()



# Write to csv
military_data.to_csv('wb_data/military_data.csv')

