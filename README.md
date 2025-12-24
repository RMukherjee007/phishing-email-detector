# Phishing Email Detection System

A Python application that classifies emails as phishing or legitimate using text processing and statistical features.

## Overview

This project analyzes email content and identifies common phishing patterns such as suspicious links, urgent language, and unusual formatting. It is built using classical text processing techniques and a linear classification model.

## Features

- Email text cleaning and normalization
- Feature extraction using TF-IDF and simple structural indicators
- Classification of emails as phishing or legitimate
- Confidence score for each prediction
- Simple web interface for testing single emails and batches

## Tech Stack

- Python
- scikit-learn
- pandas
- numpy
- nltk
- streamlit

## Project Structure

phishing-email-detector/
- core/
  - data_loader.py
  - preprocessing.py
  - feature_extraction.py
  - classifier.py
  - evaluation.py
- app.py
- requirements.txt
- README.md

## How to Run

pip install -r requirements.txt  
streamlit run app.py  

## Purpose

This project was built to practice text processing, feature engineering, and clean object-oriented design in Python.
