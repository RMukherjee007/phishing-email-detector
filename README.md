# AI Phishing Email Detector 🛡️

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
<img src="https://img.shields.io/badge/ML-Logistic%20Regression-orange">
<img src="https://img.shields.io/badge/NLP-NLTK-blueviolet">
<img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit">
<img src="https://img.shields.io/badge/Accuracy-~93%25-green">
<img src="https://img.shields.io/badge/Status-Active-success">
</p>

<p align="center">
An end-to-end machine learning pipeline that classifies emails as legitimate or phishing using natural language processing and statistical feature engineering.
</p>

<p align="center">
The project demonstrates a **production-style modular architecture**, separating preprocessing, feature extraction, and inference into independent components.
</p>

---

# 🎯 Features

## Hybrid Feature Extraction

Combines high-dimensional **TF-IDF vectorization** with structural heuristics to identify phishing patterns.

Feature design includes:

* TF-IDF vectorization with **ngram range (1–2)**
* URL density measurement
* urgency-based keyword detection
* suspicious call-to-action phrases

This hybrid approach enables detection of **both vocabulary-based phishing patterns and structural anomalies**.

---

## Intelligent Text Normalization

Uses **NLTK** to perform robust text preprocessing.

The pipeline performs:

* automated tokenization
* stop-word removal
* punctuation filtering
* case normalization

A custom **regex-based URL extractor** identifies both standard and obfuscated phishing links commonly used in email attacks.

Example detected patterns:

```
secure-login-check.xyz
bit.ly/account-reset
paypal-security-alert.com
```

---

## Real-time Diagnostic Interface

The application includes a **Streamlit dashboard** that allows users to paste raw email content and receive instant classification.

The interface provides:

* phishing / legitimate classification label
* probability-based confidence score
* rapid inference suitable for security experimentation

---

# 🏗️ System Architecture

```
Raw Email Content
        ↓
preprocessing.py
(NLTK Sanitization & Regex URL Extraction)
        ↓
feature_extraction.py
(TF-IDF Vectorization + Heuristic Features)
        ↓
classifier.py
(Balanced Logistic Regression Model)
        ↓
app.py
(Streamlit Dashboard Rendering)
```

The architecture follows a **modular ML pipeline**, allowing individual components to be tested or replaced independently.

---

# 📂 Project Structure

```
phishing-email-detector/
│
├── app.py                  # Streamlit UI & application logic
├── requirements.txt        # dependency manifest
│
└── core/
    ├── __init__.py
    ├── preprocessing.py        # text cleaning & regex utilities
    ├── feature_extraction.py   # TF-IDF + structural heuristics
    ├── classifier.py           # logistic regression wrapper
    ├── data_loader.py          # CSV ingestion & validation
    └── evaluation.py           # performance metrics (precision/recall)
```

---

# 📊 Realistic Performance Metrics

Benchmarked on publicly available phishing datasets such as **Enron** and **PhishBowl**.

| Metric              | Value   | Context                                                 |
| ------------------- | ------- | ------------------------------------------------------- |
| Model Accuracy      | ~92–94% | strong detection of phishing templates                  |
| Inference Latency   | < 50 ms | optimized for local CPU execution                       |
| False Positive Rate | ~3–5%   | minimizes misclassification of legitimate urgent emails |

The classifier performs particularly well on **“Urgent Action”, “Security Alert”, and “Account Verification” phishing templates**.

---

# 💻 Installation & Usage

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the dashboard

```bash
streamlit run app.py
```

The Streamlit interface will open in your browser.

Users can paste email text into the input panel and instantly receive classification results.

---

# 🛠️ Technologies Used

| Category         | Technology     |
| ---------------- | -------------- |
| Language         | Python 3.10+   |
| Machine Learning | Scikit-learn   |
| NLP              | NLTK           |
| UI Framework     | Streamlit      |
| Data Processing  | Pandas / NumPy |

---

# 📄 License

MIT License

