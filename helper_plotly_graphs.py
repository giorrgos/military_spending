
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd



df = pd.read_csv('wb_data/clean_military_data.csv')

# Filter the 
max_year = df['year'].max()

# KPI 1
kpi_total_milex_max_year = go.Figure(go.Indicator(
        mode="number",
        value=df[df['year'] == max_year]['milex_usd'].sum()/1000000000,
        title={"text": f"Total Military Expenditure for {max_year} in ($b)"}
    ))
kpi_total_milex_max_year.show()

# KPI 2
kpi_avg_milex_gdp_pct_max_year = go.Figure(go.Indicator(
        mode="number",
        value=df[df['year'] == max_year]['milex_pct'].mean(),
        number={'suffix': '%', 'valueformat': '.1f'},
        title={"text": f"Average Military Expenditure as % of GDP for {max_year} in ($b)"}
    ))
kpi_avg_milex_gdp_pct_max_year.show()

# KPI 3
kpi_avg_milex_gov_exp_pct_max_year = go.Figure(go.Indicator(
        mode="number",
        value=df[df['year'] == max_year]['milex_gov_exp_pct'].mean(),
        number={'suffix': '%', 'valueformat': '.1f'},
        title={"text": f"Average Military Expenditure as % of Gov Exp for {max_year} in ($b)"}
    ))
kpi_avg_milex_gov_exp_pct_max_year.show()


# Line chart
# Divide "milex_pct" by 100
line_chart = px.line(
    df,
    x="year",
    y="milex_pct",
    color="country_name",
    labels={"milex_pct": "Militery Expenditure (% of GDP)", "year": "Year"},
    title="Milex Percentage Over Time by Country"
)

# Add markers for the years and update the y-axis format
line_chart.update_traces(mode='lines+markers')

# Update the x-axis to display without decimal points and format the y-axis
line_chart.update_layout(
    xaxis_tickformat='d',  # 'd' format for integer values
    xaxis_tickvals=df['year'].unique()  # show ticks only for the unique years in the dataset
    )

line_chart.show()

df.info()