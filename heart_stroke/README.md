# Heart stroke prediction

## Table of contents
* [Project Description](#project-description)
* [Libraries and Packages](#libraries-and-packages)
* [Method](#method)
* [Sources](#sources)

<a name="project-description"></a>
## Project Description
In this project we are trying to build predictive machine learning models to classify if a patient is at risk of heart stroke or not. We will use different pre-processing methods and compare the models with AUC.
Moreover, we will use feature selection to understand which life habits and variables impact the most in this case.

<a name="libraries-and-packages"></a>
## Libraries and Packages
In order to run the code for this project, you will need to run the following command to install the necessary packages:

For Python 3:
```
python3 -m pip install -U pip
python3 -m pip install -U pandas numpy matplotlib scikit-learn scipy seaborn statsmodels plotly cufflinks ipywidgets
```

For Python 2:
```
python -m pip install -U pip
python -m pip install -U pandas numpy matplotlib scikit-learn scipy seaborn statsmodels plotly cufflinks ipywidgets
```

<a name="method"></a>
## Method
1. Cleaning the data;
2. Visualize the data using Tableau (you can find the figures in the folder called ML Visualizations);
3. Build six machine learning models (logistic regression, decision tree, random forest, SVM, Naive Bayes, KNN) with different pre-processing methods (undersampling, oversampling and feature selection);
4. Compare the different models by using AUC measurement.

<a name="sources"></a>
## Sources
Kaggle database website:
https://www.kaggle.com/fedesoriano/stroke-prediction-dataset
