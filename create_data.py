import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
start_date = datetime(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]

n_records = 1000
data = {
    'sale_date': np.random.choice(dates, n_records),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports', 'Books'], n_records),
    'price': np.random.uniform(10, 500, n_records),
    'quantity': np.random.randint(1, 10, n_records),
    'region': np.random.choice(['North', 'South', 'East', 'West'], n_records)
}
data['sales'] = data['price'] * data['quantity']

df = pd.DataFrame(data)
df.loc[np.random.choice(df.index, 50), 'price'] = np.nan

df.to_csv('data/raw/sales_data.csv', index=False)
print(f"✅ Created sales_data.csv with {len(df)} rows")
