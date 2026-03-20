"""
Data visualization utilities.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List
import os

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def create_visualizations(df: pd.DataFrame, output_dir: str = 'reports/figures/') -> None:
    """
    Create a comprehensive set of visualizations for the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    output_dir : str
        Directory to save the visualizations
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print("\n" + "="*50)
    print("📊 CREATING VISUALIZATIONS")
    print("="*50)
    
    # 1. Distribution plots for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        for idx, col in enumerate(numeric_cols[:6]):
            axes[idx].hist(df[col].dropna(), bins=30, edgecolor='black', alpha=0.7)
            axes[idx].set_title(f'Distribution of {col}')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frequency')
        
        # Hide unused subplots
        for idx in range(len(numeric_cols), 6):
            axes[idx].set_visible(False)
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'numeric_distributions.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: numeric_distributions.png")
    
    # 2. Correlation heatmap
    if len(numeric_cols) > 1:
        plt.figure(figsize=(10, 8))
        correlation = df[numeric_cols].corr()
        sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', 
                    center=0, square=True, linewidths=0.5)
        plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), dpi=150, bbox_inches='tight')
        plt.close()
        print(f"✅ Saved: correlation_heatmap.png")
    
    print("\n✅ All visualizations created successfully!")
