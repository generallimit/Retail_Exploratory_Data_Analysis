# Retail Data Analysis with Python

## Overview
This project performs exploratory data analysis (EDA) on transactional data from an online retail store. The goal is to uncover insights into sales trends, customer behavior, and product performance to support data-driven decision-making.

## Key Features
- **Data Loading and Cleaning**: 
  - Consolidates multiple CSV files into a single DataFrame.
  - Cleans column names and handles missing values.
  - Removes duplicates and filters invalid data.

- **Data Transformation**:
  - Renames columns for better readability.
  - Creates new columns such as `Gross` (calculated as `QuantityOrdered * CostOfGoodsSold`) and `MonthYear` for time-based analysis.

- **Statistical Analysis**:
  - Provides descriptive statistics for key metrics.
  - Identifies outliers using Z-scores and removes them for cleaner analysis.

- **Data Visualization**:
  - Visualizes sales trends over time using line plots.
  - Analyzes sales distribution by day of the week and month using bar charts.
  - Displays gross amount distribution with box plots.

- **Insights Extraction**:
  - Identifies the busiest month and day of the week for sales.
  - Highlights the most valuable customers and products.
  - Determines the top-performing regions based on sales.

## Analysis Workflow
1. **Load Data**:
   - Combine CSV files from the `./projects/sales/sales/` directory into a single DataFrame.
   - Preview the data using `df.head()` and inspect its structure with `df.info()`.

2. **Clean and Transform Data**:
   - Standardize column names and handle missing values.
   - Drop unnecessary columns like `OrderId` and `SKU`.
   - Add calculated fields such as `Gross` and `MonthYear`.

3. **Explore Data**:
   - Analyze missing values and unique values per column.
   - Group data by time periods (e.g., months) and categories (e.g., products, regions).

4. **Visualize Data**:
   - Plot sales trends over time.
   - Create bar charts for sales by day of the week and month.
   - Use box plots to visualize the distribution of gross amounts.

5. **Extract Insights**:
   - Identify top customers, products, and regions.
   - Highlight sales trends and patterns for decision-making.

## Key Insights
- The busiest month and day of the week for sales are identified.
- The top 10 customers and products contributing to gross sales are highlighted.
- The regions with the highest sales are determined.

## Tools and Libraries
- **Python**: Core programming language for analysis.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Matplotlib** and **Seaborn**: Data visualization.
- **Scipy**: Statistical analysis.

## How to Run
1. Ensure all required libraries are installed:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy