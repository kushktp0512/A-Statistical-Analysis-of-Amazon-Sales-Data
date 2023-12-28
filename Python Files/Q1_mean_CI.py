import numpy as np
import pandas as pd
from tabulate import tabulate
import random
import matplotlib.pyplot as plt
from scipy.stats import norm

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

#  Q1: Should I buy Computers & Accessories on Amazon ? Let me check the product ratings first!
#  It is not possible to check ratings for all listings, so we need an estimate!
#  Let's calculate a confidence interval for estimation.

# Get a list of rating for main_category -> Computers&Accessories
rating_list = df[df['main_category'] == 'Computers&Accessories']['rating'].tolist()

#  Histogram of population values
plt.hist(rating_list, bins=15, align='left',
         rwidth=0.8)
plt.xlabel('Rating of Products')
plt.ylabel('Frequency')
plt.title('Distribution of ratings for Computers&Accessories')
plt.show()

#  As we can observe, the distribution is approximately normal with a slight negative skew
#  Hence we will take a sample size of 45

#  Calculate population mean -> μ
print(f'\nMean rating of Computers&Accessories-> ', np.mean(rating_list))

#  generate random sample of 45
sample = random.sample(rating_list, 45)
n = len(sample)
x_bar = np.mean(sample)
s = np.sqrt(np.var(sample, ddof=1))
print(f'\nSample size n = {n}')
print(f'\nSample average x-bar = {x_bar}')
print(f'\nSample Std dev = {s}')

#  95% CI calculation for proportion
CL = 0.95
alpha = 1 - CL
z = norm.ppf(1 - alpha / 2)
print("Z value->", z)

lb = x_bar - z*(s/np.sqrt(n))
ub = x_bar + z*(s/np.sqrt(n))
w = ub - lb
print(f'\n95% CI => ({lb},{ub})')
