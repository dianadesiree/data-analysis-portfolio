"""
Data cleaning and preprocessing functions.
"""

import pandas as pd
import numpy as np
from typing import List, Optional

def clean_dataset(df: pd.DataFrame, 
                  handle_missing: str = 'drop',
                  fill_value: Optional[any] = None) -> pd.DataFrame:
    """
    Clean a dataset by handling missing values, duplicates, and data types.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    handle_missing : str
        Strategy for handling missing values: 'drop', 'fill', 'ffill', 'bfill'
    fill_value : any
        Value to fill missing values with (if handle_missing='fill')
    
    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe
    """
    df_clean = df.copy()
    
    # Remove duplicates
    initial_rows = len(df_clean)
    df_clean.drop_duplicates(inplace=True)
    duplicates_removed = initial_rows - len(df_clean)
    print(f"🔍 Removed {duplicates_removed} duplicate rows")
    
    # Handle missing values
    missing_before = df_clean.isnull().sum().sum()
    
    if handle_missing == 'drop':
        df_clean.dropna(inplace=True)
    elif handle_missing == 'fill':
        if fill_value is not None:
            df_clean.fillna(fill_value, inplace=True)
        else:
            # Fill numeric columns with median, categorical with mode
            for col in df_clean.columns:
                if df_clean[col].dtype in ['int64', 'float64']:
                    df_clean[col].fillna(df_clean[col].median(), inplace=True)
                else:
                    df_clean[col].fillna(df_clean[col].mode()[0] if not df_clean[col].mode().empty else 'Unknown', inplace=True)
    elif handle_missing == 'ffill':
        df_clean.fillna(method='ffill', inplace=True)
    elif handle_missing == 'bfill':
        df_clean.fillna(method='bfill', inplace=True)
    
    missing_after = df_clean.isnull().sum().sum()
    print(f"🔍 Handled {missing_before - missing_after} missing values")
    
    # Convert date columns
    for col in df_clean.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            try:
                df_clean[col] = pd.to_datetime(df_clean[col])
                print(f"📅 Converted {col} to datetime")
            except:
                pass
    
    print(f"✅ Dataset cleaned: {len(df_clean)} rows remaining")
    return df_clean
