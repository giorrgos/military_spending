import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load data
df = pd.read_csv('wb_data/clean_military_data.csv')

# Dashboard config
st.set_page_config(
    page_title="Military Expenditure",
    page_icon="helper/mili_spending.jpg",
    layout="wide"
)

# Page title
st.title("Military Expenditure Analysis")

# Sidebar Filters
start_year, end_year = st.sidebar.slider("Select Year Range:", min(pd.unique(df["year"])), max(pd.unique(df["year"])), (min(pd.unique(df["year"])), max(pd.unique(df["year"]))))
selected_years = list(range(start_year, end_year + 1))
selected_countries = st.sidebar.multiselect("Select Country:", pd.unique(df["country_name"]), default=pd.unique(df["country_name"]))

# Filter data based on sidebar selections
filtered_df = df[df["year"].isin(selected_years) & 
                 df["country_name"].isin(selected_countries)]

# Define the max year after the selections
max_year = filtered_df['year'].max()

# UI
kpi_total_milex_max_year, kpi_avg_milex_gdp_pct_max_year, kpi_avg_milex_gov_exp_pct_max_year = st.columns(3)

# KPI 1
if not filtered_df.empty:
    kpi_total_milex_max_year.metric( 
        label=f"Total Military Expenditure for {max_year} in ($b)",
        value=round(filtered_df[filtered_df['year'] == max_year]['milex_usd'].sum()/1000000000, 1)
    ) 
else:
    kpi_total_milex_max_year.metric(label=f"Total Military Expenditure for {max_year} in ($b)", value=0)


# Doughnut Chart
country_milex_data = filtered_df[filtered_df['year'] == max_year].groupby("country_name")["milex_usd"].sum().reset_index()
country_milex_data = country_milex_data.sort_values(by="milex_usd", ascending=False)

fig = go.Figure(data=[go.Pie(labels=country_milex_data["country_name"], 
                             values=country_milex_data["milex_usd"],
                             hole=.3)])  # Setting hole=.3 makes it a doughnut chart
fig.update_layout(title_text=f"Country-wise Military Expenditure for {max_year}")

kpi_total_milex_max_year.plotly_chart(fig)


# KPI 2
if not filtered_df.empty:
    kpi_avg_milex_gdp_pct_max_year.metric(
          label=f"Average Military Expenditure as % of GDP for {max_year} in ($b)",
          value="{:.1f}%".format(filtered_df[filtered_df['year'] == max_year]['milex_pct'].mean())
    )
else:
    kpi_avg_milex_gdp_pct_max_year.metric(label=f"Average Military Expenditure as % of GDP for {max_year} in ($b)", value=0)

# Column chart 2
avg_milex_gdp_data = filtered_df[filtered_df['year'] == max_year].groupby("country_name")["milex_pct"].mean().reset_index()
avg_milex_gdp_data = avg_milex_gdp_data.sort_values(by="milex_pct", ascending=True)
fig2 = px.bar(avg_milex_gdp_data, y="country_name", x="milex_pct", orientation='h', title=f"Average Military Expenditure as % of GDP by Country for {max_year}")
fig2.update_layout(showlegend=False)  # Turn off legend as it's redundant for a single series column chart
kpi_avg_milex_gdp_pct_max_year.plotly_chart(fig2)

# KPI 3
if not filtered_df.empty:
    kpi_avg_milex_gov_exp_pct_max_year.metric(
        label=f"Average Military Expenditure as % of Gov Exp for {max_year}",
        value="{:.1f}%".format(filtered_df[filtered_df['year'] == max_year]['milex_gov_exp_pct'].mean())
    )
else:
    kpi_avg_milex_gov_exp_pct_max_year.metric(label=f"Average Military Expenditure as % of Gov Exp for {max_year}", value=0)

# Column chart 3
avg_milex_gov_exp_data = filtered_df[filtered_df['year'] == max_year].groupby("country_name")["milex_gov_exp_pct"].mean().reset_index()
avg_milex_gov_exp_data = avg_milex_gov_exp_data.sort_values(by="milex_gov_exp_pct", ascending=True)
fig3 = px.bar(avg_milex_gov_exp_data, y="country_name", x="milex_gov_exp_pct", orientation='h', title=f"Average Military Expenditure as % of Gov Exp by Country for {max_year}")
fig3.update_layout(showlegend=False)  # Turn off legend as it's redundant for a single series column chart
kpi_avg_milex_gov_exp_pct_max_year.plotly_chart(fig3)




