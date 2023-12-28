import numpy as np
import pandas as pd
from tabulate import tabulate
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Giving file path to python
dataset = '/Users/ashu_k/Documents/MEM_PS/PS Project/Datasets/amazon.csv'

# Storing dataset as "df" for manipulation by python
df = pd.read_csv(dataset)


# Function to check missing values column-wise
def check_missing_values(dataframe):
    return dataframe.isnull().sum()


# Remove rows with missing values from df
df.dropna(subset=['rating_count'], inplace=True)


# Check for duplicate entries
def check_duplicates(dataframe):
    return dataframe.duplicated().sum()


# Check data type in csv file
def check_data_types(dataframe):
    return dataframe.dtypes


#  Converting numerical for required categories values to float for calculation
df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%', '').astype(float)
df['rating'] = df['rating'].astype(float)
df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '').astype(float)

#  splitting of main and sub categories
df['sub_category-2'] = df['category'].astype(str).str.split('|').str[-1]
df['main_category'] = df['category'].astype(str).str.split('|').str[0]
df['sub_category-1'] = df['category'].astype(str).str.split('|').str[1]

selected_columns = ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']
selected_df = df[selected_columns]
correlation_matrix = selected_df.corr()

# Displaying the correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='gist_earth', linewidths=.5)
plt.title("Correlation Heatmap")
plt.show()
