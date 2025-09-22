# Abuja Housing Data Analysis and Price Prediction
## Project Overview

    This project focuses on the Abuja real estate market. The goal was to collect housing data, clean and analyze it, and then build a regression model to predict house prices based on property features.

## Data Collection

    I scraped real estate listings from an online property website using BeautifulSoup and python. The dataset included property attributes such as the price,address, property ref,date listed , last updated , market status, type, bedrooms, bathrooms, toilets, parking spaces. with some columns  containing missing values.

## Data Cleaning
    
    After collection, I cleaned the dataset by:
    Removing duplicate records
    moving data that were in incorrect columns to thier correct columns using custom functions
    Dropping columns with too many missing values (e.g., parking spaces, covered area)
    Handling correlated features by keeping the most representative ones (e.g., bedrooms instead of bedrooms, bathrooms, and toilets together)
    Converting prices into numerical format for analysis, creating new columns where neccesary
    This process ensured that the dataset was consistent and ready for modeling.

## Exploratory Data Analysis

    I analyzed the distribution of housing prices and property features. The data showed:
    A strong right-skew in prices due to large, high-end properties
    Clear relationships between the number of rooms and price
    Trends that highlighted how certain property features influenced cost
    These insights were visualized through histograms, scatter plots, and correlation matrices.

## Predictive Modeling
 
    To predict housing prices, I trained a regression model using the cleaned dataset. The model captured how property features such as bedrooms and area contributed to overall pricing. Performance was evaluated using error metrics to understand the accuracy of predictions.

## Results and Insights

    The model was able to provide reasonable predictions of house prices in Abuja based on available features. While not perfect, it demonstrated how data-driven approaches can support real estate decision-making.

## Tech Stack
Python, BeautifulSoup (web scraping),Pandas (data manipulation)
Matplotlib / Seaborn (visualization),Scikit-learn (regression modeling and evaluation)

