# Data Analysis Portfolio

<p align="center">
  <strong>Pandas • SQL • Jupyter • Data Visualization • Exploratory Data Analysis</strong>
</p>

<p align="center">
  A professional portfolio project that demonstrates practical data analysis workflows, from raw data preparation to insight generation, visualization, and SQL-based querying.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/SQL-Analytics-336791?logo=postgresql&logoColor=white" alt="SQL">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white" alt="Jupyter">
  <img src="https://img.shields.io/badge/Visualization-Matplotlib%20%26%20Seaborn-success" alt="Visualization">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## Overview

**Data Analysis Portfolio** is a portfolio-ready repository designed to showcase core analytics skills through clear, reproducible, and well-documented projects.

This repository demonstrates:

- Data cleaning and preprocessing with **Pandas**
- Exploratory Data Analysis (**EDA**) and statistical summaries
- Data visualization with **Matplotlib** and **Seaborn**
- SQL querying for extraction, aggregation, and analytical reporting
- Interactive analysis with **Jupyter Notebooks**
- Professional project organization suitable for recruiters, collaborators, and hiring managers

The goal of this project is to present an end-to-end view of how raw data can be transformed into meaningful insights through structured analysis and clean technical documentation.

---

## Why This Repository Stands Out

- **Portfolio-focused design** with professional documentation
- **Multiple datasets** across practical business-style scenarios
- **Reproducible workflows** with clear project organization
- **SQL + Python integration** for broader analytical coverage
- **Presentation-ready outputs** including reports and charts
- **Clean and maintainable code** aligned with industry best practices

---

## Key Features

### Python Analysis Modules

| Module | Purpose |
|--------|---------|
| `data_cleaning.py` | Handles missing values, duplicates, outliers, and data type conversions |
| `eda_analysis.py` | Performs descriptive analysis, distributions, correlations, and summary reporting |
| `data_visualization.py` | Generates reusable charts and visual outputs |
| `load_data.py` | Loads datasets from CSV, Excel, and SQL sources |

### SQL Practice Library

| File | Purpose |
|------|---------|
| `basic_queries.sql` | Fundamental filtering and sorting queries |
| `aggregations.sql` | Grouping and aggregate calculations |
| `joins.sql` | Join operations across related tables |
| `advanced_queries.sql` | CTEs, subqueries, window functions, and conditional logic |

### Jupyter Notebooks

| Notebook | Purpose |
|----------|---------|
| `01_data_cleaning.ipynb` | Step-by-step data cleaning workflow |
| `02_exploratory_analysis.ipynb` | Exploratory analysis with charts and observations |
| `03_statistical_analysis.ipynb` | Statistical summaries and analytical testing |
| `04_sql_integration.ipynb` | SQL workflows connected with Python analysis |

---

## Technology Stack

| Technology | Use Case |
|------------|----------|
| **Python 3.9+** | Core programming language |
| **Pandas** | Data cleaning and manipulation |
| **NumPy** | Numerical operations |
| **Matplotlib** | Foundational visualizations |
| **Seaborn** | Statistical plotting |
| **Jupyter Notebook** | Interactive data exploration |
| **SQLite / PostgreSQL** | Relational database querying |
| **SQLAlchemy** | SQL connectivity and workflow integration |
| **Plotly** *(optional)* | Interactive visual analytics |
| **Scikit-learn** *(optional)* | Introductory modeling and predictive experiments |

---

## Project Structure

```text
data-analysis-portfolio/
│
├── python/
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── data_visualization.py
│   ├── load_data.py
│   └── requirements.txt
│
├── sql/
│   ├── basic_queries.sql
│   ├── aggregations.sql
│   ├── joins.sql
│   ├── advanced_queries.sql
│   └── README.md
│
├── jupyter/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_statistical_analysis.ipynb
│   ├── 04_sql_integration.ipynb
│   └── README.md
│
├── data/
│   ├── raw/
│   │   └── sales_data_complete.csv
│   ├── processed/
│   │   └── sales_cleaned.csv
│   └── external/
│
├── notebooks/
│
├── config/
│   ├── settings.json
│   └── database_config.json
│
├── docs/
│   ├── screenshots/
│   │   ├── eda_summary.txt
│   │   ├── visualizations_summary.png
│   │   ├── basic_query.sql
│   │   ├── cleaning_process.txt
│   │   ├── final_report.txt
│   │   └── README.md
│   └── examples/
│
├── reports/
│   ├── figures/
│   │   ├── top_categories.png
│   │   ├── sales_by_region.png
│   │   ├── customer_segments.png
│   │   ├── correlation_heatmap.png
│   │   └── time_series_analysis.png
│   └── sql_basic_aggregation.csv
│
├── tests/
│   ├── test_data_cleaning.py
│   └── test_analysis.py
│
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

Before running the project, make sure you have:

- **Python 3.9 or higher**
- **pip**
- **Git** *(optional, but recommended)*
- **SQLite or PostgreSQL** *(optional, for SQL examples)*

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/dianadesiree/data-analysis-portfolio.git
cd data-analysis-portfolio
```

#### 2. Create and activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### Manual package installation

```bash
pip install pandas numpy matplotlib seaborn jupyter
pip install sqlalchemy openpyxl xlsxwriter
```

### Verify the setup

```bash
python -c "import pandas; print(pandas.__version__)"
python -c "import jupyter; print('Jupyter installed successfully')"
```

---

## Quick Start

### 1. Generate sample data

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(730)]

n_records = 5000
data = {
    "sale_date": np.random.choice(dates, n_records),
    "product_category": np.random.choice(
        ["Electronics", "Clothing", "Home & Garden", "Sports", "Books", "Toys"],
        n_records
    ),
    "price": np.random.uniform(10, 1000, n_records),
    "quantity": np.random.randint(1, 20, n_records),
    "amount": np.random.uniform(50, 5000, n_records),
    "customer_id": np.random.randint(1000, 9999, n_records),
    "region": np.random.choice(["North", "South", "East", "West", "Central"], n_records)
}

data["total_sales"] = data["price"] * data["quantity"]

df = pd.DataFrame(data)
df.to_csv("data/raw/sales_data_complete.csv", index=False)

print(f"Created sales_data_complete.csv with {len(df)} rows")
```

### 2. Load and inspect the dataset

```python
from python.load_data import load_csv_data
from python.eda_analysis import basic_data_overview

df = load_csv_data("data/raw/sales_data_complete.csv")
basic_data_overview(df)
```

### 3. Run the cleaning pipeline

```python
from python.data_cleaning import clean_dataset

cleaned_df = clean_dataset(df)
cleaned_df.to_csv("data/processed/sales_cleaned.csv", index=False)
```

### 4. Run exploratory analysis

```python
from python.eda_analysis import generate_eda_report

eda_results = generate_eda_report(cleaned_df)
```

### 5. Generate visualizations

```python
from python.data_visualization import create_visualizations

create_visualizations(cleaned_df, output_dir="reports/figures/")
```

### 6. Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open and run the notebooks in this order:

1. `01_data_cleaning.ipynb`
2. `02_exploratory_analysis.ipynb`
3. `03_statistical_analysis.ipynb`
4. `04_sql_integration.ipynb`

---

## Analysis Examples

### Example 1: Sales Performance Analysis

```python
import matplotlib.pyplot as plt

category_sales = (
    df.groupby(["product_category", "region"])["total_sales"]
    .agg(["sum", "mean", "count"])
)

top_categories = category_sales.sort_values("sum", ascending=False).head(10)

top_categories["sum"].plot(kind="bar", title="Top 10 Categories by Sales")
plt.tight_layout()
plt.savefig("reports/figures/top_categories.png")
plt.show()
```

### Example 2: Customer Segmentation (RFM Analysis)

```python
from datetime import datetime

today = datetime.now()

rfm = df.groupby("customer_id").agg({
    "purchase_date": lambda x: (today - x.max()).days,
    "order_id": "count",
    "amount": "sum"
}).rename(columns={
    "purchase_date": "recency",
    "order_id": "frequency",
    "amount": "monetary"
})

rfm["segment"] = pd.qcut(rfm["recency"], 4, labels=["4", "3", "2", "1"])
```

### Example 3: Time Series Analysis

```python
monthly_sales = df.groupby(pd.Grouper(key="sale_date", freq="ME"))["total_sales"].sum()

monthly_sales.rolling(window=3).mean().plot()
plt.title("3-Month Moving Average of Sales")
plt.show()
```

---

## SQL Examples

### Basic Aggregation

```sql
SELECT
    product_category,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_transaction_value,
    MIN(amount) AS min_sale,
    MAX(amount) AS max_sale
FROM transactions
WHERE sale_date >= DATE('now', '-6 months')
GROUP BY product_category
HAVING COUNT(*) > 100
ORDER BY total_revenue DESC;
```

### Customer Lifetime Value Analysis

```sql
SELECT
    c.customer_id,
    c.customer_name,
    c.region,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS lifetime_value,
    AVG(o.amount) AS avg_order_value,
    MAX(o.order_date) AS last_purchase_date,
    JULIANDAY('now') - JULIANDAY(MAX(o.order_date)) AS days_since_last_purchase
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_status = 'completed'
GROUP BY c.customer_id
HAVING lifetime_value > 1000
ORDER BY lifetime_value DESC;
```

### Window Functions

```sql
SELECT
    product_name,
    sale_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY product_name
        ORDER BY sale_date
    ) AS running_total,
    RANK() OVER (
        PARTITION BY sale_date
        ORDER BY amount DESC
    ) AS daily_rank
FROM daily_sales
WHERE sale_date >= DATE('now', '-30 days');
```

---

## Screenshots

To keep the main README clean and recruiter-friendly, screenshots are linked instead of embedded directly.

| Asset | Description |
|-------|-------------|
| `eda_summary.txt` | Exploratory data analysis summary |
| `visualizations_summary.png` | Correlation heatmaps and distribution plots |
| `basic_query.sql` | Example SQL queries |
| `cleaning_process.txt` | Data cleaning workflow |
| `final_report.txt` | Final report and insights |

Browse the screenshots folder here:

```text
docs/screenshots/
```

---

## Roadmap

Planned improvements for future iterations:

- Add more datasets from additional industries
- Expand SQL examples with more advanced business cases
- Introduce predictive modeling workflows
- Build interactive dashboards with Plotly or Streamlit
- Add automated testing and CI/CD integration
- Include Power BI or Tableau dashboards
- Strengthen data quality validation checks
- Deploy a lightweight analytics app to the cloud

---

## Contributing

Contributions, ideas, and improvements are welcome.

1. Fork the repository
2. Create a feature branch  
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes  
   ```bash
   git commit -m "Add amazing feature"
   ```
4. Push to your branch  
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

For major changes, please open an issue first so the proposal can be discussed clearly.

---

## License

This project is distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

## Contact

**Diana Araujo**

- **Email:** dianadaraujo78@gmail.com
- **GitHub:** [dianadesiree](https://github.com/dianadesiree)
- **LinkedIn:** [Diana Araujo](https://www.linkedin.com/in/dianadaraujo/)

---

## Notes

- This repository is designed to present practical, portfolio-ready analytics work
- All code and analysis assets should remain clearly documented and reproducible
- For best results, run the notebooks in sequence
- The project uses modern Pandas conventions, including updated frequency aliases where applicable

---

## Optional Git Commands to Publish the Updated README

```powershell
git status
git add README.md
git commit -m "Refine README with professional GitHub presentation"
git push origin main
```
