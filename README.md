# Military Spending Analysis

A data analysis project that retrieves military expenditure data from the World Bank API, cleans it, and presents it through an interactive Streamlit dashboard.

## Project Overview
This project tracks and visualizes military spending across countries over time, using official World Bank data. It provides insights into global defense expenditure patterns, comparing countries by total spending, percentage of GDP, and percentage of government expenditure.

## Features
- Data Acquisition: Retrieves military spending data from World Bank API using the wbgapi library
- Data Cleaning: Processes and transforms raw data into analysis-ready datasets
- Data Visualization: Interactive charts and graphs showing spending patterns
- Streamlit Dashboard: User-friendly interface with filtering options by:
    - Country
    - Year range
    - Various expenditure metrics

## Getting Started

Installation
1. Clone this repository
```bash
git clone https://github.com/yourusername/military_spending.git
cd military_spending
```

2. Install dependencies (example with UV):
```bash
uv venv
source .venv/bin/activate  # On Windows, use .env\Scripts\activate
uv pip install -e .
```

3. Run the data acquisition and cleaning scripts
```bash
python 01_get_data.py
python 02_clean_data.py
```

4. Launch the Streamlit app
```bash
streamlit run app.py
```

## Technologies Used
- Python
- Pandas for data manipulation
- Plotly for interactive visualizations
- Streamlit for dashboard creation
- World Bank API (wbgapi) for data retrieval