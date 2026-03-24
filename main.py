#!/usr/bin/env python
"""
Data Analysis Portfolio - Main Application
A comprehensive data analysis tool with interactive menu
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import custom modules
from python.load_data import load_csv_data
from python.eda_analysis import basic_data_overview
from python.data_visualization import create_visualizations

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print application header"""
    print("="*60)
    print("📊 DATA ANALYSIS PORTFOLIO")
    print("="*60)
    print("Version: 1.0.0")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

def print_menu():
    """Print main menu"""
    print("\n🔍 MAIN MENU")
    print("-"*40)
    print("1. Load and Explore Data")
    print("2. Generate Sample Data")
    print("3. Run Data Cleaning")
    print("4. Create Visualizations")
    print("5. Generate Full Analysis Report")
    print("6. View Sample SQL Queries")
    print("7. Help")
    print("0. Exit")
    print("-"*40)

def generate_sample_data():
    """Generate sample sales data"""
    print("\n📦 Generating sample data...")
    
    import numpy as np
    from datetime import datetime, timedelta
    
    np.random.seed(42)
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=x) for x in range(730)]
    
    n_records = 5000
    data = {
        'sale_date': np.random.choice(dates, n_records),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 'Toys'], n_records),
        'price': np.random.uniform(10, 1000, n_records),
        'quantity': np.random.randint(1, 20, n_records),
        'amount': np.random.uniform(50, 5000, n_records),
        'customer_id': np.random.randint(1000, 9999, n_records),
        'region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n_records)
    }
    data['total_sales'] = data['price'] * data['quantity']
    
    df = pd.DataFrame(data)
    
    # Create directories if they don't exist
    os.makedirs('data/raw', exist_ok=True)
    
    # Save to file
    filepath = 'data/raw/sales_data_complete.csv'
    df.to_csv(filepath, index=False)
    
    print(f"✅ Sample data generated successfully!")
    print(f"   File: {filepath}")
    print(f"   Records: {len(df)}")
    print(f"   Columns: {len(df.columns)}")
    
    return df

def load_and_explore():
    """Load and explore data"""
    print("\n📂 LOADING DATA")
    print("-"*40)
    
    filepath = input("Enter file path (or press Enter for sample data): ").strip()
    
    if not filepath:
        print("No file specified. Loading sample data...")
        df = generate_sample_data()
    else:
        try:
            df = load_csv_data(filepath)
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            return None
    
    # Show basic overview
    basic_data_overview(df)
    
    return df

def run_data_cleaning(df=None):
    """Run data cleaning pipeline"""
    from python.data_cleaning import clean_dataset
    
    if df is None:
        print("\n⚠️ No data loaded. Please load data first.")
        df = load_and_explore()
        if df is None:
            return None
    
    print("\n🧹 RUNNING DATA CLEANING")
    print("-"*40)
    
    # Ask for cleaning options
    print("Cleaning options:")
    print("1. Drop missing values")
    print("2. Fill missing values (recommended)")
    print("3. Forward fill")
    
    choice = input("\nSelect option (1-3, default=2): ").strip()
    
    if choice == '1':
        cleaned_df = clean_dataset(df, handle_missing='drop')
    elif choice == '3':
        cleaned_df = clean_dataset(df, handle_missing='ffill')
    else:
        cleaned_df = clean_dataset(df, handle_missing='fill')
    
    # Save cleaned data
    os.makedirs('data/processed', exist_ok=True)
    output_path = 'data/processed/sales_cleaned.csv'
    cleaned_df.to_csv(output_path, index=False)
    
    print(f"\n✅ Cleaned data saved to: {output_path}")
    
    return cleaned_df

def create_visualizations_from_data(df=None):
    """Create visualizations"""
    if df is None:
        print("\n⚠️ No data loaded. Loading sample data...")
        try:
            df = pd.read_csv('data/raw/sales_data_complete.csv')
            print(f"✅ Loaded {len(df)} records")
        except:
            print("❌ No data found. Generating sample data...")
            df = generate_sample_data()
    
    print("\n📊 CREATING VISUALIZATIONS")
    print("-"*40)
    
    # Create output directory
    os.makedirs('reports/figures', exist_ok=True)
    
    # Create visualizations
    create_visualizations(df, output_dir='reports/figures')
    
    print("\n✅ Visualizations saved to reports/figures/")
    print("   You can view them in the folder.")

def generate_full_report():
    """Generate complete analysis report"""
    print("\n📈 GENERATING FULL ANALYSIS REPORT")
    print("-"*40)
    
    # Load data
    try:
        df = pd.read_csv('data/raw/sales_data_complete.csv')
        print(f"✅ Loaded {len(df)} records")
    except:
        print("⚠️ Sample data not found. Generating...")
        df = generate_sample_data()
    
    # Clean data
    from python.data_cleaning import clean_dataset
    df_clean = clean_dataset(df, handle_missing='fill')
    
    # Create visualizations
    os.makedirs('reports/figures', exist_ok=True)
    create_visualizations(df_clean, output_dir='reports/figures')
    
    # Generate text report
    report_path = 'reports/analysis_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write("DATA ANALYSIS REPORT\n")
        f.write("="*60 + "\n\n")
        
        f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("DATASET OVERVIEW\n")
        f.write("-"*40 + "\n")
        f.write(f"Total Records: {len(df_clean):,}\n")
        f.write(f"Total Columns: {len(df_clean.columns)}\n\n")
        
        f.write("SALES SUMMARY\n")
        f.write("-"*40 + "\n")
        total_sales = df_clean['total_sales'].sum() if 'total_sales' in df_clean.columns else 0
        avg_sales = df_clean['total_sales'].mean() if 'total_sales' in df_clean.columns else 0
        f.write(f"Total Revenue: ${total_sales:,.2f}\n")
        f.write(f"Average Transaction: ${avg_sales:,.2f}\n\n")
        
        if 'product_category' in df_clean.columns:
            f.write("TOP PERFORMING CATEGORIES\n")
            f.write("-"*40 + "\n")
            top_categories = df_clean.groupby('product_category')['total_sales'].sum().sort_values(ascending=False).head(5)
            for cat, sales in top_categories.items():
                f.write(f"  • {cat}: ${sales:,.2f}\n")
        
        f.write("\n" + "="*60 + "\n")
        f.write("Report generated by Data Analysis Portfolio Tool\n")
        f.write("="*60 + "\n")
    
    print(f"✅ Report saved to: {report_path}")
    print(f"✅ Visualizations saved to: reports/figures/")

def view_sql_queries():
    """Display sample SQL queries"""
    print("\n🗄️ SAMPLE SQL QUERIES")
    print("="*60)
    
    queries = {
        "1. Basic Aggregation": """
SELECT 
    product_category,
    COUNT(*) as transaction_count,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_transaction_value
FROM sales_data
GROUP BY product_category
ORDER BY total_revenue DESC;
""",
        "2. Customer Lifetime Value": """
SELECT 
    customer_id,
    COUNT(*) as total_orders,
    SUM(amount) as lifetime_value,
    AVG(amount) as avg_order_value
FROM sales_data
GROUP BY customer_id
ORDER BY lifetime_value DESC
LIMIT 10;
""",
        "3. Time Series Analysis": """
SELECT 
    strftime('%Y-%m', sale_date) as month,
    COUNT(*) as transactions,
    SUM(amount) as monthly_revenue
FROM sales_data
WHERE sale_date >= DATE('now', '-6 months')
GROUP BY month
ORDER BY month DESC;
"""
    }
    
    for name, query in queries.items():
        print(f"\n📌 {name}")
        print("-"*40)
        print(query)
    
    input("\nPress Enter to continue...")

def show_help():
    """Show help information"""
    print("\n❓ HELP")
    print("="*60)
    print("""
DATA ANALYSIS PORTFOLIO - HELP

📁 File Locations:
   - Raw data: data/raw/
   - Processed data: data/processed/
   - Visualizations: reports/figures/
   - Reports: reports/

📊 Supported File Formats:
   - CSV (.csv)
   - Excel (.xlsx, .xls)

💡 Tips:
   1. Use option 1 to load your own CSV file
   2. Option 2 generates sample data if you don't have any
   3. Run data cleaning before creating visualizations
   4. Generated visualizations are saved as PNG files

🔧 Requirements:
   - Python 3.8 or higher
   - Required packages: pandas, numpy, matplotlib, seaborn

For more information, visit:
   https://github.com/dianadesiree/data-analysis-portfolio
""")
    
    input("\nPress Enter to continue...")

def main():
    """Main application loop"""
    df = None
    
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        choice = input("\nSelect an option (0-7): ").strip()
        
        if choice == '1':
            df = load_and_explore()
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            df = generate_sample_data()
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            df = run_data_cleaning(df)
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            create_visualizations_from_data(df)
            input("\nPress Enter to continue...")
        
        elif choice == '5':
            generate_full_report()
            input("\nPress Enter to continue...")
        
        elif choice == '6':
            view_sql_queries()
        
        elif choice == '7':
            show_help()
        
        elif choice == '0':
            print("\n👋 Thank you for using Data Analysis Portfolio!")
            print("Exiting...")
            break
        
        else:
            print("\n❌ Invalid option. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()