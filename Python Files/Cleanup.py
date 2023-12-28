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

print("\nShape of df-> ", df.shape)


# Function to check missing values column-wise
def check_missing_values(dataframe):
    return dataframe.isnull().sum()


# Print an overview of null values wrt column header
print("\nCrosscheck table:")
print(check_missing_values(df))

# printing the rows which have null values
print("\nRows with null values")
print(tabulate(df[df.rating_count.isnull()], headers='keys', tablefmt='fancy_grid'))

# Remove rows with missing values from df
df.dropna(subset=['rating_count'], inplace=True)
print("\nCrosscheck table after removing rows->")
print(check_missing_values(df))

print("\nNew shape of df-> ", df.shape)


# Check for duplicate entries
def check_duplicates(dataframe):
    return dataframe.duplicated().sum()


print("\nNumber of duplicate entries-> ", check_duplicates(df))


# Check data type in csv file
def check_data_types(dataframe):
    return dataframe.dtypes


print("\nData type of entries-> ")
print(check_data_types(df))

#  Converting numerical for required categories values to float for calculation
df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%', '').astype(float)
df['rating'] = df['rating'].astype(float)
df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '').astype(float)

print("\nData type of entries after conversion-> ")
print(check_data_types(df))

#  splitting of main and sub categories
df['sub_category-2'] = df['category'].astype(str).str.split('|').str[-1]
df['main_category'] = df['category'].astype(str).str.split('|').str[0]
df['sub_category-1'] = df['category'].astype(str).str.split('|').str[1]
