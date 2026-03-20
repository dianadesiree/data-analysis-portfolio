"""
Exploratory Data Analysis (EDA) functions.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any

def basic_data_overview(df: pd.DataFrame) -> None:
    """
    Print basic information about the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    """
    print("\n" + "="*50)
    print("📊 BASIC DATA OVERVIEW")
    print("="*50)
    
    # Basic info
    print(f"\n📈 Dataset Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Column info
    print("\n📋 Column Information:")
    for col in df.columns:
        dtype = df[col].dtype
        nulls = df[col].isnull().sum()
        null_pct = (nulls / len(df)) * 100
        unique = df[col].nunique()
        print(f"  • {col}: {dtype} | {nulls} nulls ({null_pct:.1f}%) | {unique} unique values")
    
    # Basic statistics
    print("\n📊 Statistical Summary:")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        print(df[numeric_cols].describe())
    
    # First few rows
    print("\n🔍 First 5 rows:")
    print(df.head())

def generate_eda_report(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Generate a comprehensive EDA report.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    
    Returns:
    --------
    Dict[str, Any]
        Dictionary containing EDA results
    """
    print("\n" + "="*50)
    print("📈 GENERATING EDA REPORT")
    print("="*50)
    
    report = {}
    
    # 1. Basic info
    report['shape'] = {'rows': df.shape[0], 'columns': df.shape[1]}
    report['column_names'] = list(df.columns)
    
    # 2. Data types
    report['data_types'] = df.dtypes.astype(str).to_dict()
    
    # 3. Missing values
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    report['missing_values'] = {
        'count': missing.to_dict(),
        'percentage': missing_pct.to_dict()
    }
    
    # 4. Duplicates
    duplicates = df.duplicated().sum()
    report['duplicates'] = duplicates
    print(f"🔍 Found {duplicates} duplicate rows")
    
    # 5. Numeric columns statistics
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        report['numeric_stats'] = df[numeric_cols].describe().to_dict()
        
        # Correlation matrix
        report['correlation'] = df[numeric_cols].corr().to_dict()
    
    # 6. Categorical columns analysis
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        report['categorical_summary'] = {}
        for col in categorical_cols:
            value_counts = df[col].value_counts()
            report['categorical_summary'][col] = {
                'top_values': value_counts.head(5).to_dict(),
                'unique_count': len(value_counts)
            }
    
    print("\n✅ EDA Report Generated Successfully!")
    return report
