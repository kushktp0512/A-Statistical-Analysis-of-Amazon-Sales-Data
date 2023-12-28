import numpy as np
import pandas as pd
from tabulate import tabulate
import random
import matplotlib.pyplot as plt
from scipy.stats import norm
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

#  List of discount% for main_category -> Electronics
mean_disc1 = (df[(df['main_category'] == 'Electronics')]['discount_percentage'].tolist())
#  List of discount% for main_category -> Home&Kitchen
mean_disc2 = (df[(df['main_category'] == 'Home&Kitchen')]['discount_percentage'].tolist())

#  Sample calculations for Electronics
disc1_sample = random.sample(mean_disc1, 44)  # generate a random sample of n=100
sum_Xi = [value for value in disc1_sample if value >= 65]
prop_1 = len(sum_Xi)/len(disc1_sample)
print(f'Summation Xi = {sum_Xi}')
print(f'p1 = {prop_1}')

#  Sample calculations for Home&Kitchen
disc2_sample = random.sample(mean_disc2, 44)  # generate a random sample of n=100
sum_Yi = [value2 for value2 in disc2_sample if value2 >= 65]
prop_2 = len(sum_Yi)/len(disc2_sample)
print(f'Summation Yi = {sum_Yi}')
print(f'p2 = {prop_2}')

#  As we can see, consistently the Electronics category has more proportion of products with a discount >= 65%
