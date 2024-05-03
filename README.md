# Patient Survival Prediction
This project aims to predict survival on various body and blood values of the patients. Various Machine Learning models are trained. On the website, the model with the best evaluation metrics is utilized.  
The dataset that will be used in this project is listed on Kaggle as [Patient Survival Prediction](https://www.kaggle.com/datasets/mitishaagarwal/patient).  

## Project Overview

The key aspects of this project include:

- Extensive exploratory data analysis on survival results of many patients with assorted features  
- Preprocessing data by handling null values, duplicates, outliers and converting categorical features  
- Visualizations for eliminating the non-contributing features  
- Feature engineering by using Chi-square distance to distinguish  
- Training classification models like Logistic Regression, Random Forest and Neural Networks  
- Comparing model performance to predict survival  

## Tech Stack

**Language**: Python  
**Technologies**: Pandas, Matplotlib, Seaborn, Sci-kit Learn, Tensorflow, Keras, Shap     
**Environment**: Jupyter Notebook, Streamlit    

## Getting Started  

### Prerequisites
- Python 3  
- Jupyter Notebook
- Streamlit  

### Installation

- Clone the repository
  ```bash
  git clone https://github.com/meric2/Patient-Survival-Prediction.git
  ```

- Start Jupyter notebook
  ```bash
  jupyter notebook
  ```

- Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
  
- Open `survivalprediction.ipynb` notebook and run all cells to train models.  
- Open [web app](https://meric2-patient-survival-prediction-yap470-app-rmgogf.streamlit.app/) to use the saved pre-trained model.  


## Usage

This project can serve as a reference for binary classification while building machine learning pipelines.  
On the website the most important features are given to the user to enter manually or load as a csv file. An instance of the csv file is given as `example.csv`. When necessary fields are filled, the website shows the survival prediction.  

## Contributors

- [Rana Demir](https://github.com/demirrana)  
- [Zeynep Meriç Aşık](https://github.com/meric2)
