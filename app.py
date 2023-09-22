import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# https://blog.streamlit.io/how-to-build-a-real-time-live-dashboard-with-streamlit/

# Load data
df = pd.read_csv('wb_data/clean_military_data.csv')

max_year = df['year'].max()

# Dashboard config
st.set_page_config(
    page_title="Military Expenditure",
    page_icon="helper\mili_spending.jpg",
    layout="wide"
)


# Use a get_data() function so it is properly cached
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(df)


# Create the UI

# Page title
st.title("Military Expenditure Analysis")

st.sidebar.multiselect("Select Year:", pd.unique(df["year"]))
st.sidebar.multiselect("Select Country:", pd.unique(df["country_name"]))
st.sidebar.multiselect("Select Country iso3:", pd.unique(df["country_iso3"]))
st.sidebar.multiselect("Select Region:", pd.unique(df["region_name_wb"]))

kpi_total_milex_max_year, kpi_avg_milex_gdp_pct_max_year, kpi_avg_milex_gov_exp_pct_max_year = st.columns(3)

# KPI 1
kpi_total_milex_max_year.metric( 
    label=f"Total Military Expenditure for {max_year} in ($b)",
    value=round(df[df['year'] == max_year]['milex_usd'].sum()/1000000000, 1)
) 


# KPI 2
kpi_avg_milex_gdp_pct_max_year.metric(
      label=f"Average Military Expenditure as % of GDP for {max_year} in ($b)",
      value=df[df['year'] == max_year]['milex_pct'].mean()
)

# KPI 3
kpi_avg_milex_gov_exp_pct_max_year.metric(
    label=f"Average Military Expenditure as % of Gov Exp for {max_year} in ($b)",
    value=df[df['year'] == max_year]['milex_gov_exp_pct'].mean(),
)
