# Bitcoin Price Prediction

A machine learning project that predicts future Bitcoin closing prices using historical Bitcoin market data obtained from Yahoo Finance.

The project uses Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib, and Streamlit.

## Project Overview

Bitcoin is a highly volatile cryptocurrency whose price changes continuously based on market conditions.

This project explores historical Bitcoin price data and develops a Linear Regression model to predict Bitcoin's closing price.

The project contains two main components:

1. Exploratory Data Analysis and Machine Learning model development using Jupyter Notebook.
2. A Streamlit web application that allows users to predict the Bitcoin closing price for a selected number of future days.

## Features

- Downloads historical Bitcoin data using Yahoo Finance.
- Performs exploratory data analysis on historical Bitcoin prices.
- Cleans and prepares the dataset.
- Creates time-series based features.
- Uses Linear Regression for price prediction.
- Evaluates the model using standard regression metrics.
- Saves the trained model using Joblib.
- Saves the feature column information using Joblib.
- Provides a Streamlit interface for future price prediction.

## Dataset

The project uses Bitcoin historical market data for the BTC-USD ticker from Yahoo Finance.

The notebook initially retrieves approximately five years of historical Bitcoin data.

The Streamlit application retrieves Bitcoin data starting from January 1, 2020 up to the current date.

The primary target variable is the Bitcoin closing price.

## Machine Learning Workflow

The project follows the following workflow:

Historical Bitcoin Data
        |
        v
Data Collection
        |
        v
Data Cleaning
        |
        v
Exploratory Data Analysis
        |
        v
Feature Engineering
        |
        v
Train/Test Split
        |
        v
Linear Regression
        |
        v
Model Evaluation
        |
        v
Model Serialization
        |
        v
Streamlit Prediction Application

## Exploratory Data Analysis

The notebook performs several exploratory analysis steps including:

- Inspecting the first and last records.
- Checking for missing values.
- Checking for duplicate records.
- Inspecting dataset columns.
- Visualizing Bitcoin price trends.
- Analyzing Open, High, Low, and Close prices.
- Examining relationships between numerical variables.

The notebook uses Matplotlib and Seaborn for visualization.

## Feature Engineering

The machine learning model developed in the notebook uses historical Bitcoin price information to create additional features.

The features include:

- Close_Lag1
- Close_Lag2
- Close_Lag3
- Close_Lag4
- Close_Lag7
- Close_Lag14
- Close_MA7
- Close_MA30
- Volatility_7
- Volatility_30
- Returns

### Lag Features

Lag features represent Bitcoin's historical closing prices.

For example:

Close_Lag1 represents the previous day's closing price.

Close_Lag7 represents the closing price from seven days earlier.

Close_Lag14 represents the closing price from fourteen days earlier.

### Moving Average Features

The project calculates:

- 7-day moving average
- 30-day moving average

These features provide information about recent Bitcoin price trends.

### Volatility Features

The project calculates rolling standard deviation over:

- 7 days
- 30 days

These features provide information about recent price variability.

### Returns

The Returns feature is calculated using the percentage change in Bitcoin's closing price.

## Model

The project uses Linear Regression from Scikit-learn.

The notebook separates the dataset into training and testing data using an 80/20 split.

The first 80 percent of the processed data is used for training and the remaining 20 percent is used for testing.

The model is evaluated using:

- Mean Squared Error
- Mean Absolute Error
- Root Mean Squared Error
- R-squared

## Model Persistence

The notebook uses Joblib to save the trained machine learning model and the feature column information.

The generated files are:

btc_lr_model_joblib.pkl

btc_feature_columns.pkl

These files can be used to preserve the trained model and the feature configuration.

## Streamlit Application

The Streamlit application provides a simple interface for predicting Bitcoin prices.

The application:

1. Downloads Bitcoin historical data.
2. Extracts the Date and Close columns.
3. Creates a next-day prediction target.
4. Trains a Linear Regression model.
5. Allows the user to enter the number of days to predict ahead.
6. Iteratively predicts future Bitcoin prices.
7. Displays the predicted closing price.

The current application allows predictions between 1 and 30 days ahead.

## Project Structure

```text
Bitcoin-Price-Prediction/
|
|-- BITCOIN PRICE PREDICTION.ipynb
|-- main.py
|-- requirements.txt
|-- btc_lr_model_joblib.pkl
|-- btc_feature_columns.pkl
|-- README.md
