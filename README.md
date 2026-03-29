# Disease Prediction System using Machine Learning

## Overview
This project is a machine learning-based system that predicts possible diseases based on user-selected symptoms. It uses a Random Forest Classifier to analyze patterns in the dataset and provides a predicted disease along with a confidence score.

The project is designed for educational purposes to demonstrate how machine learning can be applied in healthcare for basic symptom-based prediction.


## Features
- Predicts diseases based on selected symptoms  
- Displays confidence level for predictions  
- Interactive user interface using ipywidgets  
- Easy to run in Jupyter Notebook or Google Colab  



## Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- IPyWidgets  



## Dataset
The dataset contains symptoms as input features and diseases as output labels.

### Symptoms:
- Fever  
- Cough  
- Headache  
- Fatigue  
- Nausea  
- Vomiting  
- Body pain  
- Rash  
- Runny nose  

### Output:
- Disease name (Flu, COVID-19, Dengue, etc.)



## Installation

Install the required libraries using:
pip install pandas scikit-learn ipywidgets
[11:34 am, 29/03/2026] Vedant Salunkhe: Enable widgets (for Jupyter Notebook):
[11:34 am, 29/03/2026] Vedant Salunkhe: jupyter nbextension enable –py widgetsnbextension
[11:34 am, 29/03/2026] Vedant Salunkhe: ---

## How to Run

1. Place disease_data.csv in your working directory  
2. Open the project in Jupyter Notebook or Google Colab  
3. Run the Python script  
4. Select symptoms using the checkboxes  
5. Click on "Predict Disease"  
6. The predicted disease and confidence score will be displayed  

---

## How It Works

- The dataset is loaded using Pandas  
- Symptoms are used as input features  
- The disease column is used as the target variable  
- A Random Forest model is trained on the dataset  
- User input is converted into binary format  
- The model predicts the disease and calculates confidence  

---

## Example Output
[11:34 am, 29/03/2026] Vedant Salunkhe: Predicted Disease: Flu
Confidence: 87.45%
[11:34 am, 29/03/2026] Vedant Salunkhe: ---

## Advantages
- Simple and easy to understand  
- Provides quick predictions  
- Useful for learning machine learning concepts  
- Interactive interface  



## Limitations
- Small dataset  
- Limited number of diseases  
- Not suitable for real-world medical diagnosis  
- Accuracy depends on dataset quality  

---

## Future Improvements
- Use a larger and more realistic dataset  
- Convert into a web application  
- Add more symptoms and diseases  
- Improve model accuracy  
- Add chatbot-based input  

---

## Applications
- Educational projects  
- Machine learning demonstrations  
- Basic healthcare awareness tools  

---

## Author
sohan

---

## Disclaimer
This project is intended for educational purposes only and should not be used as a substitute for professional medical advice.
