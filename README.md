# Data Analysis Portfolio

**Pandas | SQL | Jupyter | Data Visualization | EDA**

A comprehensive data analysis portfolio showcasing practical data cleaning, exploration, visualization, and SQL querying skills. This repository demonstrates end-to-end data analysis workflows using Python (Pandas), SQL databases, and interactive Jupyter notebooks.

The project includes real-world datasets, exploratory data analysis (EDA), statistical summaries, data visualizations, and SQL query examples that highlight analytical thinking and technical execution.

## Table of Contents
- [Overview](#overview)
- [Highlights](#highlights)
- [Core Features](#core-features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Analysis Examples](#analysis-examples)
- [SQL Queries](#sql-queries)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
Data Analysis Portfolio is a portfolio-ready project designed to demonstrate proficiency in:

- Data cleaning and preprocessing with Pandas
- Exploratory Data Analysis (EDA) and statistical summaries
- Data visualization with Matplotlib and Seaborn
- SQL query writing for data extraction and analysis
- Interactive analysis using Jupyter notebooks
- Professional documentation and presentation of results

The project analyzes multiple datasets to answer business questions, identify trends, and provide actionable insights through clear visualizations and well-documented code.

## Highlights
This version includes several features that make the project stronger for portfolio and recruiter review:

- **Multiple datasets** covering different domains (sales, customer, product, etc.)
- **Comprehensive EDA** with statistical summaries and correlation analysis
- **Interactive Jupyter notebooks** with markdown explanations
- **SQL query library** for common analytical patterns
- **Professional visualizations** ready for presentation
- **Clean, documented code** following PEP 8 standards
- **Reproducible analysis** with clear step-by-step methodology
- **Project structure** that mirrors real-world data science workflows

## Core Features

### Python/Pandas Analysis
| Component | Description |
|-----------|-------------|
| `data_cleaning.py` | Data preprocessing functions for handling missing values, outliers, and data type conversions |
| `eda_analysis.py` | Exploratory data analysis with statistical summaries and visualizations |
| `data_visualization.py` | Custom visualization functions for common chart types |
| `analysis_pipeline.py` | End-to-end analysis pipeline combining all components |

### SQL Queries
| Category | Description |
|----------|-------------|
| `basic_queries.sql` | SELECT, WHERE, ORDER BY, LIMIT operations |
| `aggregations.sql` | GROUP BY, COUNT, SUM, AVG, MIN, MAX queries |
| `joins.sql` | INNER, LEFT, RIGHT, FULL OUTER JOIN examples |
| `advanced_queries.sql` | Subqueries, CTEs, window functions, and CASE statements |

### Jupyter Notebooks
| Notebook | Description |
|----------|-------------|
| `01_data_cleaning.ipynb` | Step-by-step data cleaning and preprocessing |
| `02_exploratory_analysis.ipynb` | Comprehensive EDA with visualizations |
| `03_statistical_analysis.ipynb` | Statistical tests and correlation analysis |
| `04_sql_integration.ipynb` | Python + SQL integration examples |

### Data Processing Scripts
| Script | Description |
|--------|-------------|
| `load_data.py` | Functions to load data from CSV, Excel, and SQL databases |
| `clean_data.py` | Standardized data cleaning functions |
| `transform_data.py` | Feature engineering and data transformation |
| `export_results.py` | Export analysis results to CSV, Excel, or JSON |

## Technologies Used
| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language for data analysis |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computing |
| **Matplotlib** | Basic data visualization |
| **Seaborn** | Statistical data visualization |
| **Jupyter Notebook** | Interactive analysis environment |
| **SQLite/PostgreSQL** | Relational database management |
| **SQLAlchemy** | SQL toolkit and ORM |
| **Plotly** (optional) | Interactive visualizations |
| **Scikit-learn** (optional) | Basic machine learning models |

## Project Structure

data-analysis-portfolio/
│
├── python/
│ ├── data_cleaning.py # Data preprocessing functions
│ ├── eda_analysis.py # Exploratory analysis functions
│ ├── data_visualization.py # Visualization utilities
│ ├── analysis_pipeline.py # Complete analysis workflow
│ ├── load_data.py # Data loading utilities
│ ├── transform_data.py # Feature engineering
│ ├── export_results.py # Export functionality
│ └── requirements.txt # Python dependencies
│
├── sql/
│ ├── basic_queries.sql # SELECT, WHERE, ORDER BY
│ ├── aggregations.sql # GROUP BY and aggregate functions
│ ├── joins.sql # JOIN operations
│ ├── advanced_queries.sql # Subqueries, CTEs, window functions
│ └── README.md # SQL documentation
│
├── jupyter/
│ ├── 01_data_cleaning.ipynb # Data cleaning notebook
│ ├── 02_exploratory_analysis.ipynb # EDA notebook
│ ├── 03_statistical_analysis.ipynb # Statistics notebook
│ ├── 04_sql_integration.ipynb # SQL + Python notebook
│ └── README.md # Jupyter documentation
│
├── data/
│ ├── raw/ # Original, immutable data
│ │ ├── sales_data.csv
│ │ ├── customer_data.csv
│ │ └── product_data.csv
│ ├── processed/ # Cleaned and transformed data
│ │ ├── sales_cleaned.csv
│ │ └── analysis_results.csv
│ └── external/ # External reference data
│ └── reference_data.csv
│
├── notebooks/
│ └── (alternative location for Jupyter notebooks)
│
├── config/
│ ├── settings.json # Configuration parameters
│ └── database_config.json # Database connection settings
│
├── docs/
│ ├── screenshots/ # Analysis screenshots
│ │ ├── screenshot_1_eda.png
│ │ ├── screenshot_2_visualizations.png
│ │ ├── screenshot_3_sql_queries.png
│ │ ├── screenshot_4_correlation_heatmap.png
│ │ ├── screenshot_5_distribution_plots.png
│ │ └── screenshot_6_jupyter_notebook.png
│ └── examples/ # Example outputs
│
├── reports/
│ ├── figures/ # Generated graphics
│ └── analysis_report.md # Summary report
│
├── tests/
│ ├── test_data_cleaning.py # Unit tests
│ └── test_analysis.py # Analysis tests
│
├── .gitignore # Git ignore rules
├── LICENSE # License file
├── setup.py # Python setup script
└── README.md # Main documentation


## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git (optional, for version control)
- SQLite or PostgreSQL (optional, for SQL examples)

### Option 1: Install from requirements.txt
```bash
# Clone the repository (if using Git)
git clone https://github.com/dianadesiree/data-analysis-portfolio.git
cd data-analysis-portfolio

# Install Python dependencies
pip install -r python/requirements.txt
