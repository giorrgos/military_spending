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
        'MS.MIL.MPRT.KD':'arms_imports',
        'MS.MIL.TOTL.P1':'armed_forces_total',
        'MS.MIL.TOTL.TF.ZS':'armed_forces_pct_labour',
        'MS.MIL.XPND.CD':'milex_usd',
        'MS.MIL.XPND.GD.ZS':'milex_pct_gdp',
        'MS.MIL.XPND.ZS':'milex_pct_gov_exp',
        'MS.MIL.XPRT.KD':'arms_exports'
        })


# Join region
clean_military_data = clean_military_data.merge(
    map_country_region[['country_iso3', 'country_name', 'wb_region_name']], 
    how='left', left_on='country_iso3', right_on='country_iso3'
    )



# Write to csv
clean_military_data.to_csv('wb_data/clean_military_data.csv')
