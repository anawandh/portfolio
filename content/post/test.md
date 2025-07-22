---
title: "Data Analysis with Python: Sales Dashboard Example"
date: 2025-07-21T22:48:55
draft: false
tags: ["jupyter", "data-science"]
categories: ["blog"]
---

# Data Analysis with Python: Sales Dashboard Example

This notebook demonstrates how to create a simple sales data analysis that will be converted to a Hugo blog post. We'll explore some sample sales data and create visualizations.

## Introduction

In this analysis, we'll:
- Generate sample sales data
- Perform basic statistical analysis
- Create visualizations
- Draw insights from the data

This is a great example of how Jupyter notebooks can be used to create data-driven blog posts that combine code, analysis, and narrative.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("Libraries imported successfully!")
```

## Generating Sample Data

Let's create some realistic sample sales data for our analysis.


```python
# Set random seed for reproducibility
np.random.seed(42)

# Generate date range
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Create sample data
data = []
products = ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E']
regions = ['North', 'South', 'East', 'West']

for date in date_range:
    # Add some seasonality (higher sales in Q4)
    seasonal_factor = 1.2 if date.month >= 10 else 1.0
    
    for _ in range(np.random.poisson(8)):  # Average 8 sales per day
        data.append({
            'date': date,
            'product': np.random.choice(products),
            'region': np.random.choice(regions),
            'quantity': np.random.randint(1, 10),
            'unit_price': np.random.uniform(50, 200) * seasonal_factor,
            'customer_type': np.random.choice(['New', 'Returning'], p=[0.3, 0.7])
        })

# Create DataFrame
df = pd.DataFrame(data)
df['total_sales'] = df['quantity'] * df['unit_price']
df['month'] = df['date'].dt.month
df['quarter'] = df['date'].dt.quarter

print(f"Generated {len(df)} sales records")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
df.head()
```

## Basic Statistics

Let's examine the basic statistics of our sales data.


```python
# Basic statistics
print("=== SALES SUMMARY ===")
print(f"Total Sales: ${df['total_sales'].sum():,.2f}")
print(f"Average Order Value: ${df['total_sales'].mean():.2f}")
print(f"Total Orders: {len(df):,}")
print(f"Average Daily Sales: ${df.groupby('date')['total_sales'].sum().mean():.2f}")

print("\n=== PRODUCT BREAKDOWN ===")
product_sales = df.groupby('product')['total_sales'].sum().sort_values(ascending=False)
for product, sales in product_sales.items():
    print(f"{product}: ${sales:,.2f}")
```

## Visualizations

Now let's create some visualizations to better understand our data.


```python
# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Sales Analysis Dashboard', fontsize=16, fontweight='bold')

# 1. Monthly sales trend
monthly_sales = df.groupby('month')['total_sales'].sum()
axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2)
axes[0, 0].set_title('Monthly Sales Trend')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Total Sales ($)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Sales by product
product_sales.plot(kind='bar', ax=axes[0, 1], color='skyblue')
axes[0, 1].set_title('Sales by Product')
axes[0, 1].set_xlabel('Product')
axes[0, 1].set_ylabel('Total Sales ($)')
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Sales by region
region_sales = df.groupby('region')['total_sales'].sum()
axes[1, 0].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
axes[1, 0].set_title('Sales Distribution by Region')

# 4. Customer type comparison
customer_sales = df.groupby('customer_type')['total_sales'].sum()
customer_sales.plot(kind='bar', ax=axes[1, 1], color=['lightcoral', 'lightgreen'])
axes[1, 1].set_title('Sales by Customer Type')
axes[1, 1].set_xlabel('Customer Type')
axes[1, 1].set_ylabel('Total Sales ($)')
axes[1, 1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()
```

## Quarterly Analysis

Let's dive deeper into quarterly performance to understand seasonal trends.


```python
# Quarterly analysis
quarterly_summary = df.groupby('quarter').agg({
    'total_sales': ['sum', 'mean', 'count'],
    'quantity': 'sum'
}).round(2)

quarterly_summary.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count', 'Total_Quantity']
quarterly_summary.index = [f'Q{i}' for i in quarterly_summary.index]

print("Quarterly Performance Summary:")
print(quarterly_summary)

# Calculate quarter-over-quarter growth
quarterly_sales = df.groupby('quarter')['total_sales'].sum()
qoq_growth = quarterly_sales.pct_change() * 100

print("\nQuarter-over-Quarter Growth:")
for quarter, growth in qoq_growth.items():
    if not np.isnan(growth):
        print(f"Q{quarter}: {growth:.1f}%")
```

## Key Insights and Recommendations

Based on our analysis, here are the key findings:


```python
# Calculate key metrics for insights
best_product = product_sales.index[0]
best_region = region_sales.idxmax()
peak_month = monthly_sales.idxmax()
total_revenue = df['total_sales'].sum()

print("🎯 KEY INSIGHTS:")
print(f"📈 Total Revenue: ${total_revenue:,.2f}")
print(f"🏆 Best Performing Product: {best_product} (${product_sales[best_product]:,.2f})")
print(f"🌟 Top Region: {best_region} (${region_sales[best_region]:,.2f})")
print(f"📅 Peak Sales Month: Month {peak_month} (${monthly_sales[peak_month]:,.2f})")
print(f"👥 Customer Mix: {(df['customer_type'] == 'Returning').mean()*100:.1f}% returning customers")

print("\n💡 RECOMMENDATIONS:")
print(f"• Focus marketing efforts on {best_product} as it's the top performer")
print(f"• Expand operations in {best_region} region")
print("• Leverage Q4 seasonality for holiday promotions")
print("• Implement customer retention programs to increase returning customer ratio")
```

## Conclusion

This analysis demonstrates how we can use Python and Jupyter notebooks to:

1. **Generate and process data** efficiently with pandas
2. **Create meaningful visualizations** that tell a story
3. **Extract actionable insights** from raw data
4. **Present findings** in a clear, narrative format

The seasonal trends we observed and the product performance differences provide clear direction for business strategy. This notebook will be automatically converted to a Hugo blog post, making it easy to share these insights with stakeholders.

---

*This analysis was generated using Python, pandas, matplotlib, and seaborn. The data used is synthetic but represents realistic business scenarios.*
