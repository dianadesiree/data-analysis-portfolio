"""
Data loading utilities for various file formats and databases.
"""

import pandas as pd
import numpy as np
import os
from typing import Optional, Union

def load_csv_data(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Load data from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
    **kwargs : additional arguments
        Additional arguments to pass to pd.read_csv()
    
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    try:
        df = pd.read_csv(filepath, **kwargs)
        print(f"✅ Successfully loaded {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        print(f"❌ Error loading file {filepath}: {e}")
        raise

def load_excel_data(filepath: str, sheet_name: Union[str, int] = 0, **kwargs) -> pd.DataFrame:
    """
    Load data from Excel file.
    
    Parameters:
    -----------
    filepath : str
        Path to the Excel file
    sheet_name : str or int
        Sheet name or index to read
    **kwargs : additional arguments
        Additional arguments to pass to pd.read_excel()
    
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    try:
        df = pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)
        print(f"✅ Successfully loaded {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        print(f"❌ Error loading file {filepath}: {e}")
        raise

def get_sample_data() -> pd.DataFrame:
    """
    Create a sample dataset for testing purposes.
    
    Returns:
    --------
    pd.DataFrame
        Sample dataframe
    """
    # Create sample sales data
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    data = {
        'date': np.random.choice(dates, 500),
        'product': np.random.choice(['Product A', 'Product B', 'Product C'], 500),
        'sales': np.random.randint(100, 1000, 500),
        'quantity': np.random.randint(1, 50, 500),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 500)
    }
    return pd.DataFrame(data)
