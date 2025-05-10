# Create final table
import pandas as pd
import wbgapi as wb


# Load the mapping files
map_codes = pd.read_csv('wb_data/map_codes.csv')
map_country_region = pd.read_csv('wb_data/map_country_region.csv')

# Load the data we need
get_wb_military = pd.read_csv('wb_data/get_wb_military.csv')

### Clean the output ###

wb.series.info(q='arm')

clean_military_data = get_wb_military.rename(
    columns={
        'economy':'country_iso3', 
        'time':'year',
        'MS.MIL.XPND.CD':'milex_usd',
        'MS.MIL.XPND.GD.ZS':'milex_pct',
        'MS.MIL.XPND.ZS':'milex_gov_exp_pct',
        'SP.POP.TOTL':'population'
        }
    )

# Join region
clean_military_data = clean_military_data.merge(
    map_country_region[['country_iso3', 'country_name', 'region_name_wb']], 
    how='left', left_on='country_iso3', right_on='country_iso3'
    )

clean_military_data.info()
df = clean_military_data

# Write to csv
clean_military_data.to_csv('wb_data/clean_military_data.csv')


