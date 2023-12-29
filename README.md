# A Statistical Analysis of Amazon Sales Data

## Project Overview

This repository contains the code and documentation for an observational study conducted by me with my classmates from Northeastern University's Mechanical and Industrial Engineering Department. The study focuses on performing a statistical analysis of Amazon sales data sourced from Kaggle. The dataset comprises over 1000 product listings with various attributes, including original price, discount, rating, review count, and more.

## Abstract

The project aims to draw meaningful inferences from the dataset, utilizing visualization tools to identify trends, correlations between attributes, and provide insights into customer sentiment. The study poses questions such as the mean rating for a given product category, the proportion of electronics with low ratings, and explores relationships between variables like mean discount and mean rating for a given category.

## Project Details

### Course Information

- **Course Title:** IE 6200: Engineering Probability & Statistics
- **Semester:** Fall 2023
- **Instructor:** Prof. Paul Pei

### Dataset

The dataset used in this project is sourced from Kaggle and consists of 1000+ product listings from the Amazon India website. The attributes include original price, discount, rating, review count, and various other product-related details.

### Objectives

1. Conduct a statistical analysis of Amazon sales data.
2. Utilize visualization tools to identify trends and correlations.
3. Explore customer sentiment based on product attributes.

### Methodology

The observational study employs a sample size of 30 to 50, randomly selected from the larger population. Web scraping techniques using Python and libraries like BeautifulSoup and requests are utilized for data collection. The team acknowledges potential biases in the dataset, such as missing attributes in certain listings, and addresses them by cleaning up the database. The project also recognizes the inherent biases in user-generated ratings and reviews on public platforms like Amazon and outlines measures to mitigate their impact on the study's conclusions.

### Research Questions

1. What is the mean rating for a given product category?
2. What is the proportion of electronics with low ratings?
3. Are there relationships between variables like mean discount and mean rating for a given category?

## Repository Structure

- **data:** Contains the dataset used in the project.
- **notebooks:** Jupyter notebooks used for data analysis and visualization.
- **scripts:** Python scripts for web scraping and data cleaning.
- **reports:** Documentation and reports related to the project.

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Execute the Jupyter notebooks in the `notebooks` directory.

## Ethical Considerations

This project adheres to ethical and legal data collection practices. The team acknowledges and addresses potential biases in the dataset and takes measures to ensure the reliability and validity of the study's conclusions.

## License

This project is licensed under the [MIT License](LICENSE).
