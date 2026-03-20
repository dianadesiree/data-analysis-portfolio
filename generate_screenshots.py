import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Crear directorio para screenshots
os.makedirs('docs/screenshots', exist_ok=True)

# Cargar datos
df = pd.read_csv('data/raw/sales_data_complete.csv')

print("="*50)
print("GENERATING SCREENSHOTS FOR DOCUMENTATION")
print("="*50)

# 1. Guardar EDA Summary como texto
print("\n1. Generating EDA Summary...")
with open('docs/screenshots/eda_summary.txt', 'w') as f:
    f.write("="*50 + "\n")
    f.write("EDA SUMMARY\n")
    f.write("="*50 + "\n\n")
    f.write(f"Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns\n\n")
    f.write("Column Information:\n")
    for col in df.columns:
        f.write(f"  - {col}: {df[col].dtype}\n")
    f.write("\nStatistical Summary:\n")
    f.write(str(df.describe()))
print("✅ Saved: docs/screenshots/eda_summary.txt")

# 2. Generar visualizaciones
print("\n2. Generating Visualizations...")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Correlation heatmap
numeric_cols = df.select_dtypes(include=['number']).columns
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=axes[0,0])
axes[0,0].set_title('Correlation Heatmap', fontsize=14)

# Distribution plots
df['total_sales'].hist(bins=50, ax=axes[0,1], edgecolor='black')
axes[0,1].set_title('Sales Distribution', fontsize=14)
axes[0,1].set_xlabel('Total Sales')

# Sales by category
top_categories = df.groupby('product_category')['total_sales'].sum().sort_values(ascending=False).head(10)
top_categories.plot(kind='bar', ax=axes[1,0], color='skyblue')
axes[1,0].set_title('Top 10 Categories by Sales', fontsize=14)
axes[1,0].set_xlabel('Category')
axes[1,0].set_ylabel('Total Sales')
plt.setp(axes[1,0].xaxis.get_majorticklabels(), rotation=45, ha='right')

# Sales by region
region_sales = df.groupby('region')['total_sales'].sum()
region_sales.plot(kind='bar', ax=axes[1,1], color='lightcoral')
axes[1,1].set_title('Sales by Region', fontsize=14)
axes[1,1].set_xlabel('Region')
axes[1,1].set_ylabel('Total Sales')

plt.tight_layout()
plt.savefig('docs/screenshots/visualizations_summary.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Saved: docs/screenshots/visualizations_summary.png")

# 3. SQL Queries ejemplo
print("\n3. Generating SQL Examples...")
import sqlite3
conn = sqlite3.connect('data/sales_database.db')
df.to_sql('transactions', conn, if_exists='replace', index=False)

queries = {
    'basic_query.sql': """
SELECT 
    product_category,
    COUNT(*) as total_transactions,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_transaction_value
FROM transactions
GROUP BY product_category
ORDER BY total_revenue DESC
LIMIT 5
""",
    'aggregation_query.sql': """
SELECT 
    strftime('%Y-%m', sale_date) as month,
    COUNT(*) as transactions,
    SUM(amount) as monthly_revenue,
    AVG(amount) as avg_transaction
FROM transactions
WHERE sale_date >= '2024-01-01'
GROUP BY month
ORDER BY month DESC
"""
}

for filename, query in queries.items():
    result = pd.read_sql_query(query, conn)
    result.to_csv(f'docs/screenshots/{filename.replace(".sql", ".csv")}', index=False)
    with open(f'docs/screenshots/{filename}', 'w') as f:
        f.write(query)
        f.write("\n\n-- Results:\n")
        f.write(result.to_string())

conn.close()
print("✅ Saved SQL examples to docs/screenshots/")

# 4. Cleaning process
print("\n4. Documenting Cleaning Process...")
with open('docs/screenshots/cleaning_process.txt', 'w') as f:
    f.write("="*50 + "\n")
    f.write("DATA CLEANING PROCESS\n")
    f.write("="*50 + "\n\n")
    f.write(f"Initial dataset shape: {df.shape}\n")
    f.write(f"Initial missing values: {df.isnull().sum().sum()}\n")
    f.write(f"Initial duplicates: {df.duplicated().sum()}\n\n")
    
    # Simular limpieza
    df_clean = df.drop_duplicates()
    f.write("After removing duplicates:\n")
    f.write(f"  Shape: {df_clean.shape}\n\n")
    
    df_clean = df_clean.dropna()
    f.write("After removing missing values:\n")
    f.write(f"  Shape: {df_clean.shape}\n")
    f.write(f"  Missing values removed: {df.isnull().sum().sum() - df_clean.isnull().sum().sum()}\n")

print("✅ Saved: docs/screenshots/cleaning_process.txt")

# 5. Final report
print("\n5. Generating Final Report...")
with open('docs/screenshots/final_report.txt', 'w') as f:
    f.write("="*50 + "\n")
    f.write("FINAL ANALYSIS REPORT\n")
    f.write("="*50 + "\n\n")
    
    f.write("KEY INSIGHTS:\n")
    f.write("-"*30 + "\n")
    
    # Top selling category
    top_cat = df.groupby('product_category')['total_sales'].sum().idxmax()
    top_sales = df.groupby('product_category')['total_sales'].sum().max()
    f.write(f"1. Top selling category: {top_cat} (${top_sales:,.2f})\n\n")
    
    # Best region
    top_region = df.groupby('region')['total_sales'].sum().idxmax()
    f.write(f"2. Best performing region: {top_region}\n\n")
    
    # Average transaction
    avg_transaction = df['amount'].mean()
    f.write(f"3. Average transaction value: ${avg_transaction:,.2f}\n\n")
    
    # Total revenue
    total_revenue = df['total_sales'].sum()
    f.write(f"4. Total revenue: ${total_revenue:,.2f}\n\n")
    
    f.write("\nRECOMMENDATIONS:\n")
    f.write("-"*30 + "\n")
    f.write("• Focus marketing efforts on top-performing categories\n")
    f.write("• Expand operations in best-performing regions\n")
    f.write("• Implement customer loyalty program for high-value customers\n")
    f.write("• Optimize inventory based on seasonal trends\n")

print("✅ Saved: docs/screenshots/final_report.txt")

print("\n" + "="*50)
print("✅ ALL SCREENSHOTS GENERATED SUCCESSFULLY!")
print("="*50)
print("\nFiles created in docs/screenshots/:")
print("  - eda_summary.txt")
print("  - visualizations_summary.png")
print("  - basic_query.sql")
print("  - basic_query.csv")
print("  - aggregation_query.sql")
print("  - aggregation_query.csv")
print("  - cleaning_process.txt")
print("  - final_report.txt")
