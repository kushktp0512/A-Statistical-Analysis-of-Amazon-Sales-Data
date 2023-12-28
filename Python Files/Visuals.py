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

# Analyzing distribution of products by main category
main_category_counts = df['main_category'].value_counts()[:3]  # Select only the top 3

# Top 3 main categories
top_main_categories = pd.DataFrame(
    {'Main Category': main_category_counts.index, 'Number of Products': main_category_counts.values})
print('\nTop 3 main categories:')
print(top_main_categories.to_string(index=True))

# Analyzing distribution of products by sub category-1
sub_category1_counts = df['sub_category-1'].value_counts()[:3]  # Select only the top 3

# Top 3 sub category-1
top_sub_category1 = pd.DataFrame(
    {'sub_category-1': sub_category1_counts.index, 'Number of Products': sub_category1_counts.values})
print('\nTop 3 sub category-1:')
print(top_sub_category1.to_string(index=True))

# Analyzing distribution of products by sub category-2
sub_category2_counts = df['sub_category-2'].value_counts()[:3]  # Select only the top 3

# Top 3 sub category-2
top_sub_category2 = pd.DataFrame(
    {'sub_category-2': sub_category2_counts.index, 'Number of Products': sub_category2_counts.values})
print('\nTop 3 sub category-2:')
print(top_sub_category2.to_string(index=True))

# Plotting bar graph for the number of products in the top 3 main categories
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
ax = sns.barplot(x='Main Category', hue='Main Category', y='Number of Products', data=top_main_categories,
                 palette='twilight', legend=False)
# Adding values on each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.title('Number of Products in Top 3 Main Categories')
plt.xlabel('Main Category')
plt.ylabel('Number of Products')
plt.show()

# Plotting bar graph for the number of products in the top 3 sub category-1
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
ax = sns.barplot(x='sub_category-1', hue='sub_category-1', y='Number of Products', data=top_sub_category1,
                 palette='cubehelix', legend=False)
# Adding values on each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.title('Number of Products in Top 3 Sub Category-1')
plt.xlabel('Sub Category-1')
plt.ylabel('Number of Products')
plt.show()

# Plotting bar graph for the number of products in the top 3 sub category-2
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
ax = sns.barplot(x='sub_category-2', hue='sub_category-2', y='Number of Products', data=top_sub_category2,
                 palette='viridis', legend=False)
# Adding values on each bar
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.title('Number of Products in Top 3 Sub Category-2')
plt.xlabel('Sub Category-2')
plt.ylabel('Number of Products')
plt.show()
