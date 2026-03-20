import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('data/raw/sales_data_complete.csv')

# Análisis de ventas por categoría y región
print("="*50)
print("📊 SALES PERFORMANCE ANALYSIS")
print("="*50)

# Agrupar por categoría y región
category_sales = df.groupby(['product_category', 'region'])['total_sales'].agg(['sum', 'mean', 'count'])
category_sales = category_sales.round(2)
print("\nVentas por categoría y región:")
print(category_sales.head(10))

# Top 10 categorías por ventas
top_categories = df.groupby('product_category')['total_sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 categorías por ventas totales:")
print(top_categories)

# Visualizar resultados
plt.figure(figsize=(12, 6))
top_categories.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Categories by Total Sales', fontsize=16, fontweight='bold')
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('reports/figures/top_categories.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Gráfico guardado: reports/figures/top_categories.png")

# Análisis adicional: Ventas por región
region_sales = df.groupby('region')['total_sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Sales by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/sales_by_region.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Gráfico guardado: reports/figures/sales_by_region.png")

from datetime import datetime

print("\n" + "="*50)
print("👥 CUSTOMER SEGMENTATION - RFM ANALYSIS")
print("="*50)

# Preparar datos para RFM
# Convertir purchase_date a datetime
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Definir fecha de hoy para el análisis
today = datetime.now()

# Realizar RFM Analysis
rfm = df.groupby('customer_id').agg({
    'purchase_date': lambda x: (today - x.max()).days,  # Recency
    'order_id': 'count',  # Frequency
    'amount': 'sum'  # Monetary
}).reset_index()

# Renombrar columnas
rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

# Calcular puntajes RFM (1-4, donde 4 es mejor)
rfm['r_score'] = pd.qcut(rfm['recency'], 4, labels=['4', '3', '2', '1']).astype(str)
rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 4, labels=['1', '2', '3', '4']).astype(str)
rfm['m_score'] = pd.qcut(rfm['monetary'], 4, labels=['1', '2', '3', '4']).astype(str)

# Crear segmento combinado
rfm['rfm_score'] = rfm['r_score'] + rfm['f_score'] + rfm['m_score']

# Clasificar clientes por segmento
def segment_customers(row):
    if row['r_score'] in ['4', '3'] and row['f_score'] in ['4', '3'] and row['m_score'] in ['4', '3']:
        return 'Top Customers'
    elif row['r_score'] in ['4', '3'] and row['f_score'] in ['1', '2']:
        return 'New Customers'
    elif row['r_score'] in ['1', '2'] and row['f_score'] in ['4', '3']:
        return 'At Risk'
    elif row['r_score'] in ['1', '2'] and row['f_score'] in ['1', '2']:
        return 'Lost Customers'
    else:
        return 'Regular'

rfm['segment'] = rfm.apply(segment_customers, axis=1)

# Mostrar resultados
print("\n📊 RFM Analysis Results:")
print(f"Total customers analyzed: {len(rfm)}")
print(f"\nCustomer Segments Distribution:")
segment_distribution = rfm['segment'].value_counts()
print(segment_distribution)

# Visualizar distribución de segmentos
plt.figure(figsize=(10, 6))
segment_distribution.plot(kind='bar', color=['green', 'blue', 'orange', 'red', 'gray'])
plt.title('Customer Segments Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Customer Segment', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/customer_segments.png', dpi=150, bbox_inches='tight')
plt.show()

# Mostrar top 10 clientes por valor
print("\n🏆 Top 10 Customers by Monetary Value:")
top_customers = rfm.nlargest(10, 'monetary')[['customer_id', 'monetary', 'frequency', 'recency', 'segment']]
print(top_customers)

print("\n✅ Análisis RFM completado")

print("\n" + "="*50)
print("📈 TIME SERIES ANALYSIS")
print("="*50)

# Asegurar que sale_date es datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Análisis de series temporales mensuales
monthly_sales = df.groupby(pd.Grouper(key='sale_date', freq='ME'))['total_sales'].sum()

print("\nMonthly Sales Trend (first 12 months):")
print(monthly_sales.head(12))

# Crear figura con múltiples subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. Serie temporal original
axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2, markersize=4)
axes[0, 0].set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Total Sales ($)')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Moving Average (3 meses)
ma_3 = monthly_sales.rolling(window=3).mean()
ma_6 = monthly_sales.rolling(window=6).mean()

axes[0, 1].plot(monthly_sales.index, monthly_sales.values, label='Original', alpha=0.5)
axes[0, 1].plot(monthly_sales.index, ma_3, label='3-Month MA', linewidth=2)
axes[0, 1].plot(monthly_sales.index, ma_6, label='6-Month MA', linewidth=2)
axes[0, 1].set_title('Moving Average Analysis', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Date')
axes[0, 1].set_ylabel('Sales ($)')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Monthly Sales by Category (Top 3)
top_categories = df.groupby('product_category')['total_sales'].sum().nlargest(3).index
for category in top_categories:
    category_data = df[df['product_category'] == category]
    monthly_cat = category_data.groupby(pd.Grouper(key='sale_date', freq='ME'))['total_sales'].sum()
    axes[1, 0].plot(monthly_cat.index, monthly_cat.values, label=category, linewidth=2)
axes[1, 0].set_title('Monthly Sales by Top Categories', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Date')
axes[1, 0].set_ylabel('Sales ($)')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Seasonality Heatmap (por mes)
monthly_sales_by_month = df.groupby(df['sale_date'].dt.month)['total_sales'].sum()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
axes[1, 1].bar(months[:len(monthly_sales_by_month)], monthly_sales_by_month.values, color='lightblue', edgecolor='black')
axes[1, 1].set_title('Seasonality Pattern by Month', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Total Sales ($)')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('reports/figures/time_series_analysis.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n✅ Time series analysis completado")
