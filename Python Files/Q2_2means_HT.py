import numpy as np
import pandas as pd
from tabulate import tabulate
import random
import matplotlib.pyplot as plt
from scipy.stats import norm
from statsmodels.stats.weightstats import ztest

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

#  Histogram of discount percentage values for Electronics
plt.hist(mean_disc1, bins=20, align='left',
         rwidth=0.8)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of discount% for Electronics')
plt.show()

#  Histogram of discount percentage values for Home&Kitchen
plt.hist(mean_disc2, bins=20, align='left',
         rwidth=0.8)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of discount% for Home&Kitchen')
plt.show()

# Does Amazon provide different discounts for different categories ? (Electronics and Home & Kitchen)
# Hypothesis Testing
# H-null: mu1 - mu2 = 0 (There is no difference in mean discount percentages)
# H-alt: mu1 - mu2 ≠ 0 (There is a significant difference in mean discount percentages)
# As both Distributions are not normal, we will perform a Large sample Z-test

#  Sample calculations for Electronics
disc1_sample = random.sample(mean_disc1, 75)  # generate a random sample of n=100
print(f'\nSample mean Discount% for Electronics-> ', np.mean(disc1_sample))

#  Sample calculations for Home&Kitchen
disc2_sample = random.sample(mean_disc2, 75)  # generate a random sample of n=100
print(f'\nSample mean Discount% for Home&Kitchen-> ', np.mean(disc2_sample))

delta = 0
var1 = np.var(disc1_sample, ddof=1)
var2 = np.var(disc2_sample, ddof=1)
num = np.mean(disc1_sample) - np.mean(disc2_sample) - delta
den = np.sqrt(var1 / len(disc1_sample) + var2 / len(disc2_sample))
z = num / den
print(f'Z value is: {z}')

# Calculate the two-tailed p-value
p_value = 2 * (1 - norm.cdf(abs(z)))
print("Two-tailed p-value:", p_value)

#  Conclusion
alpha = 0.05
if p_value <= alpha:
    print("Reject Null Hypothesis")
else:
    print("Do not reject Null Hypothesis")
#  Conclusion -> Generally Electronics category has more discount than Home&Kitchen
