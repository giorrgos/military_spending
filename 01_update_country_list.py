# Create a country list
import pandas as pd
import wbgapi as wb

# Info about the available country data
wb.economy.info()
wb.region.info()

# Get a dataframe with all countries (excluding aggregates)
country_tmp = wb.economy.DataFrame(skipAggs=True).reset_index()
country_tmp.head()
country_tmp = country_tmp.rename(
    columns={
    'id':'country_iso3',
    'name':'country_name',
    'region':'wb_region_code',
    'adminregion':'admin_region_code',
    'lendingType':'lending_type',
    'incomeLevel':'income_level',
    'capitalCity':'capital_city'
    })
country_tmp.info()

# Get a list with region names and convert to dataframe
region_series = wb.region.Series()
region_series.head()

# Convert region_series into a dataframe
region_df = region_series.to_frame().reset_index()
region_df = region_df.rename(columns={'index':'wb_region_code', 'RegionName':'wb_region_name'})
type(region_df)
region_df.head()
region_df.info()

# Add region name to country data
country = country_tmp.merge(region_df, how='left', left_on='wb_region_code', right_on='wb_region_code')
country = country.drop(columns='aggregate')
country.head()
# Save results as master country table
country.to_csv('wb_data/map_country_region.csv', index=False)
