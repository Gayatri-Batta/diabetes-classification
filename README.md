# 🩺 Diabetes Prediction Web Service

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![ML](https://img.shields.io/badge/Model-Logistic%20Regression-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Overview
This project is a machine learning-powered web application designed to predict the likelihood of diabetes in patients based on diagnostic measures. 

Built with **Flask** and **Scikit-Learn**, the application utilizes a **Logistic Regression** model to classify patients based on key health indicators such as BMI, Blood Pressure, and Age. The system provides an accessible HTML front-end for real-time user input and prediction.

## 🚀 Key Features
* **Real-time Prediction:** Instant classification using a pre-trained ML model.
* **Web Interface:** User-friendly HTML/CSS front-end for easy data entry.
* **Lightweight Backend:** Built on Flask for efficient request handling and scalability.
* **Data-Driven:** Uses standard clinical features (Glucose, BMI, Age, etc.) for analysis.

## 🛠️ Technologies Used
* **Language:** Python
* **Web Framework:** Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Front-End:** HTML, CSS
* **Serialization:** Pickle (for model persistence)

## 📂 Project Structure
```bash
diabetes-classification/
├── app.py              # Main Flask application
├── model.py            # Script to train and save the ML model
├── model.pkl           # Serialized Logistic Regression model
├── templates/
│   └── index.html      # Front-end user interface
├── static/
│   └── style.css       # (Optional) Stylesheets
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
