# Get Military Data from World Bank
import pandas as pd
import wbgapi as wb

map_codes = pd.read_csv('wb_data/map_codes.csv')

# GET the data from the World Bank
get_wb_military = wb.data.DataFrame( 
    series = list(map_codes['wb_series_code']),
    economy = ['CAN', 'USA'],   
    time = range(2018, 2021),   
    numericTimeKeys = True, 
    columns='series'
    )
get_wb_military.head()
get_wb_military.info()

get_wb_military.to_csv('wb_data/get_wb_military.csv')

