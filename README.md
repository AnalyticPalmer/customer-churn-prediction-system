<p align="center">
  <img src="figures/banner.png" alt="Customer Churn Prediction System Banner" width="100%">
</p>

<h1 align="center">📊 Customer Churn Prediction System</h1>

<p align="center">
An end-to-end Machine Learning project that predicts customer churn using XGBoost and an interactive Streamlit web application.
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
<img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?logo=streamlit" />
<img src="https://img.shields.io/badge/XGBoost-Classifier-2E8B57" />
<img src="https://img.shields.io/badge/Scikit--Learn-Latest-F7931E?logo=scikitlearn" />
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" />
<img src="https://img.shields.io/badge/License-MIT-green" />

</p>

<p align="center">
<a href="https://analyticpalmer-customer-churn-prediction-system-appapp-z0tzqn.streamlit.app/">🚀 Live Demo</a> •
<a href="https://github.com/AnalyticPalmer/customer-churn-prediction-system">💻 GitHub Repository</a>
</p>

---

# 📑 Table of Contents

* Project Overview
* Business Problem
* Features
* Technology Stack
* Project Structure
* Machine Learning Pipeline
* Models Trained
* Application Screenshots
* Installation
* Running the Application
* Dataset
* Future Improvements
* Author
* License

---

# 📖 Project Overview

Customer churn is a major challenge for subscription-based businesses. Losing existing customers often costs significantly more than acquiring new ones.

This project uses Machine Learning to identify customers who are likely to leave a telecom company based on their demographics, account information, billing details, and subscribed services.

The solution includes a complete end-to-end machine learning pipeline, from data preprocessing and model training to deployment as an interactive web application using Streamlit.

---

# 💼 Business Problem

Companies lose revenue whenever customers cancel their subscriptions.

By predicting churn before it happens, businesses can:

* Improve customer retention
* Reduce revenue loss
* Identify high-risk customers
* Support targeted marketing campaigns
* Improve customer satisfaction

---

# ✨ Features

* Interactive Streamlit dashboard
* Real-time customer churn prediction
* Churn probability score
* Risk level classification
* Customer information summary
* Download prediction results as CSV
* Responsive user interface
* Clean project architecture

---

# 🛠 Technology Stack

### Programming

* Python

### Machine Learning

* Scikit-learn
* XGBoost

### Data Processing

* Pandas
* NumPy

### Visualization

* Streamlit

### Model Serialization

* Joblib

### Development Tools

* Git
* GitHub
* VS Code

---

# 📂 Project Structure

```text
customer-churn-prediction-system/
│
├── app/
│   ├── app.py
│   ├── config.py
│   ├── model_loader.py
│   ├── prediction.py
│   ├── styles.py
│   ├── ui.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── figures/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── src/
│
├── tests/
│
├── requirements.txt
├── README.md
├── LICENSE
└── main.py
```

---

# 🔄 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Selection
9. Model Deployment
10. Streamlit Application Development

---

# 🤖 Models Trained

* Logistic Regression
* Random Forest Classifier
* XGBoost Classifier ✅ (Selected Model)

The XGBoost model produced the best performance and was selected for deployment.

---

# 🖥 Application Screenshots

## Home Page

![Home](figures/app-home.png)

---

## Prediction Result

![Prediction](figures/prediction-result.png)

---

## Customer Details

![Customer Details](figures/customer-details.png)

---

## Download Report

![Download Report](figures/download-report.png)

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AnalyticPalmer/customer-churn-prediction-system.git
```

Move into the project folder:

```bash
cd customer-churn-prediction-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Start the Streamlit application:

```bash
streamlit run app/app.py
```

The application will open in your default browser.

---

# 📊 Dataset

**Dataset:** Telco Customer Churn Dataset

Target Variable:

* Churn

Key Features:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Internet Service
* Online Security
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract Type
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

---

# 📈 Future Improvements

* Batch prediction using CSV upload
* REST API with FastAPI
* Docker containerization
* SHAP explainability dashboard
* Feature importance visualization
* User authentication
* Prediction history
* CI/CD pipeline
* Cloud deployment using Docker
* Model monitoring and retraining

---

# 👨‍💻 Author

**Palmer Ogiriki**

Quality Assurance Engineer | Data Analyst | Machine Learning Engineer

**GitHub**

https://github.com/AnalyticPalmer

**LinkedIn**

https://www.linkedin.com/in/palmer-ogiriki/

---

# 🤝 Contributing

Contributions are welcome.

If you have suggestions or improvements:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.

---

# 📄 License

This project is licensed under the MIT License.
