import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate dates
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

# Generate sample data
n_records = 1000
data = {
    'sale_date': np.random.choice(dates, n_records),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books'], n_records),
    'product_name': np.random.choice(['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], n_records),
    'price': np.random.uniform(10, 500, n_records),
    'quantity': np.random.randint(1, 10, n_records),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n_records),
    'customer_id': np.random.randint(1000, 9999, n_records),
    'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Debit Card', 'Cash'], n_records)
}

# Calculate total sales
data['sales'] = data['price'] * data['quantity']

# Add some missing values for demonstration
df = pd.DataFrame(data)
df.loc[np.random.choice(df.index, 50), 'price'] = np.nan
df.loc[np.random.choice(df.index, 30), 'quantity'] = np.nan

# Save to CSV
df.to_csv('data/raw/sales_data.csv', index=False)
print("✅ Sample sales_data.csv created!")
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
