# The below code performs the analysis described in D598 Task 1 and incorporates the Original Code.docx.

# In developing the code, sources include:
# Python Software Foundation. (n.d.). PEP 8 – Style guide for Python code. 
# Python Enhancement Proposals. https://peps.python.org/pep-0008/

# Formatting the code, sources include: 
# pandas Development Team. (n.d.). pandas documentation (Version 2.x). 
# https://pandas.pydata.org/docs/reference/

#With formatting the code, sources include https://peps.python.org/pep-0008/.

#####################################################################################################

#!/usr/bin/env python
# coding: utf-8

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load D598 Data Set into a data frame

df = pd.read_excel('/Users/janekaporter/Documents/WGU Masters/Analytics Programming/D598 Data Set.xlsx')

# Check for duplicate rows; If duplicates exist, display count and drop duplicates
duplicates = df.duplicated().sum()
if duplicates > 0:
    df = df.drop_duplicates()
    print(f"\nDuplicates removed: {duplicates}")
else: 
    print(f"\nNumber of duplicates in dataset: {duplicates}")

# Group data by state and compute descriptive stats (mean, median, min, & max) 
# and store state statistics in new dataframe

# original code
# df2 = df.groupby("Business State").mean(numeric_only=True)

# Updated code to include one line of statistics and store to df_state
df_state = df.groupby("Business State").agg(['mean', 'median', 'min', 'max']) 
print("\nDescriptive statistics by state computed successfully.")

# Display first 10 rows to confirm results
#print(df_state.head(10))

# Filter data frame for negative debt-to-equity ratio
filtered_dte = df[df["Debt to Equity"]< 0]
print(f"\nFound {len(filtered_dte)} businesses with negative Debt-to-Equity ratios.")

# Calculate debt-to-income ratio for each business
df_dti = pd.DataFrame({
    'Debt to Income Ratio': np.where(
        df['Total Revenue'] == 0,
        np.nan,
        df['Total Long-term Debt'] / df['Total Revenue']
    )

})
print("\nDebt-To-Income Ratio added successfully.")

# Concatenate debt-to-income data frame to original data frame.

# df_final = pd.concat([df, df_dti["Debt-To-Income Ratio"]], axis=1)

df_final = pd.concat(
    [df.reset_index(drop=True), df_dti.reset_index(drop=True)],
    axis=1
)
print("\nDebt-To-Income Ratio added successfully to original df.")

# Display first 10 rows to confirm results
#print(df_final.head(10))

#Provide 4 customized data visualizations.

#Line Chart of Total long-term Debt by State

# Group and sum Total Long-term Debt by State
debt_by_state = df.groupby('Business State')['Total Long-term Debt'].sum()

# Sort from highest to lowest
debt_by_state = debt_by_state.sort_values('Total Long-term Debt', ascending=False)

# Format numbers as currency
debt_by_state["Total Long-term Debt"] = debt_by_state["Total Long-term Debt"].apply(lambda x: round(x, 2))

# Plot line chart
debt_by_state.plot(kind="line", figsize=(18, 6), marker="o", color="teal")

# Add titles and labels
plt.title("Total Long-Term Debt by State", fontsize=14)
plt.xlabel("Business State", fontsize=12)
plt.ylabel("Total Long-Term Debt", fontsize=12)
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

# Display the chart
plt.show()

#Bar Chart of Average Revenue by State






