# Loan-Approval-Prediction-Web-App
Machine Learning-based Loan Approval Prediction Web App built with Python, Scikit-learn, and Streamlit.


## Project Overview
This project is a Machine Learning-based Loan Approval Prediction Web App built using Python, Scikit-learn, and Streamlit. It predicts whether a loan application is likely to be approved or not based on applicant details.

The project includes a Google Colab notebook for data preprocessing, model training, and evaluation, along with a Streamlit application for making predictions.

## Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Pickle

## Project Structure

```text
Loan-Approval-Prediction-Web-App/
│
├── Loan_Approval_Prediction_Model.ipynb
├── loan_prediction.py
├── loan_dataset.csv
├── loan_model.sav
├── requirements.txt
└── README.md
```

## Features
- Data preprocessing and exploratory data analysis
- Categorical feature encoding
- Support Vector Machine (SVM) model training
- Model evaluation using training and testing accuracy
- Interactive web interface built with Streamlit
- Loan approval prediction based on applicant information

## Dataset
The project uses `loan_dataset.csv`, which contains applicant information such as gender, marital status, dependents, education, income, loan amount, loan term, credit history, and property area.

## Machine Learning Model
A Support Vector Classifier (SVC) from Scikit-learn is trained to predict loan approval. The trained model is saved as `loan_model.sav` using Pickle and loaded by the Streamlit application.

## Installation and Usage

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Loan-Approval-Prediction-Web-App
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application

```bash
streamlit run loan_prediction.py
```

The application will open in your web browser. Enter the applicant details and click the prediction button to view the result.

## Model Evaluation
The model's performance is evaluated using training and testing accuracy. The results are available in the Jupyter Notebook.

## Disclaimer
This project is intended for educational and learning purposes only. Its predictions should not be used as the sole basis for real financial or lending decisions.

## Author
Kunal Bhardwaj
