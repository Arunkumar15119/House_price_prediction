# House_price_prediction
House price prediction for Bengaluru by using python, Scikit-learn, Linear Regression and Random Forest .Including data cleaning, feature engineering(Location, BHK, Sqft), and outlier removal.


# 🏠 FutureHome: Bengaluru House Price Prediction App
📌 Project Overview

Finding the right price for a home in Bengaluru is complex due to the rapid development and variety of locations. This project is an end-to-end Data Science solution that predicts real estate prices using historical market data.

Why this project is unique: As an MBA graduate who has managed the construction of a private residence, I used my domain knowledge to perform advanced data cleaning—identifying unrealistic square footage and price outliers that a standard algorithm might miss.

🚀 Live Demo

The project is deployed using Streamlit. Users can input:

Location (from 1,300+ areas in Bengaluru)

Square Footage

BHK (Bedrooms)

Number of Bathrooms

The app then provides an instant price estimate in Lakhs.

🛠️ Technical Workflow

1. Data Preprocessing & Cleaning
Feature Engineering: Converted inconsistent size data (e.g., '3 BHK' vs '4 Bedroom') into a unified numerical format.

Dimensionality Reduction: Used the "Other" category technique to handle the high cardinality of locations, reducing 1,300+ locations into a manageable feature set.

Outlier Removal: Applied logic to remove data points where price-per-sqft was extreme or bedroom-to-area ratios were physically impossible.

2. Machine Learning Models
I compared two different algorithms to ensure the highest accuracy:

Linear Regression: Provided a strong baseline for price trends.

Random Forest Regressor: Handled non-linear patterns and complex interactions between locations and amenities.

Optimization: Used K-Fold Cross Validation to ensure the model performs well on unseen data.

📊 Performance Comparison

Model	R² Score	Best For

Linear Regression	~82%	General Market Trends

Random Forest	~89%	High Precision Valuation

📂 Project Structure


├── app.py                # Streamlit web application code

├── model.pkl             # Trained Random Forest model

├── columns.json          # List of location features for the app

├── Bengaluru_House_Data.csv # Original Dataset

└── House_Price_Analysis.ipynb # Jupyter Notebook with EDA & Model Training
