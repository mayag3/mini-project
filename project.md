\
# Brief of Mini project

TOPIC :India’s Lockdown During COVID-19: Analyzing Public Sentiment [REMEMBER THIS TITLE]



# Maya's part:
## Abstract:

This study focuses on using machine learning (ML) models to predict COVID-19 trends, aiding in effective decision-making during the pandemic. It evaluates four popular forecasting models:

Linear Regression (LR) - A basic statistical method that predicts outcomes based on a linear relationship between variables.
LASSO - A regression model that enhances prediction accuracy by selecting only the most important features.
Support Vector Machine (SVM) - A more complex model designed to find patterns in data but struggled in this context.
Exponential Smoothing (ES) - A model that prioritizes recent data, making it highly effective for short-term forecasting.
These models were tested to predict three key metrics—new COVID-19 cases, deaths, and recoveries—over a 10-day period. Results showed that exponential smoothing (ES) was the most reliable, providing accurate forecasts for all metrics.

## Intro:
COVID-19, first identified in Wuhan in 2019, spread rapidly worldwide, becoming a major global threat. This study focuses on forecasting COVID-19 cases, deaths, and recoveries over 10 days to help manage the pandemic.

Four ML models are used: linear regression (LR), LASSO, support vector machine (SVM), and exponential smoothing (ES). The models are trained on COVID-19 data from Johns Hopkins, using 85% of the data for training and 15% for testing.

Key findings:

ES performs best with limited data.
Different models excel in different predictions.
More data improves accuracy.
ML forecasting is crucial for pandemic management.
####Literature survey:
- J. Smith and A. Johnson, "Neural networks in financial time series forecasting" (2021)
  - Uses LSTM and GRU architectures.
  - Focused on predicting stock prices and market trends.

- P. Kumar, "Hybrid models combining machine learning and statistical techniques for weather prediction" (2019)
  - Combines ARIMA and SVM models.
  - Improves accuracy for short-term weather forecasts.

- R. Chen et al., "Deep learning applications in healthcare: Opportunities and challenges" (2023)
  - Applies DL to disease diagnosis and medical image analysis.
  - Addresses challenges in data privacy and interpretability.

- H. Asri, H. Mousannif, H. Al Moatassime, and T. Noel, "Using machine learning algorithms for breast cancer risk prediction and diagnosis" (2016)
  - Compares SVM, CART, NB, and kNN algorithms.
  - Focused on the Wisconsin Breast Cancer dataset.

- G. Bontempi, S. B. Taieb, and Y.-A. Le Borgne, "Machine learning strategies for time series forecasting" (2012)
  - Transitioned from ARIMA to machine learning models.
  - Explores robust techniques for predicting future behavior.


## Objectives

### Planning and Preparation:
Forecasting helps individuals and organizations plan and prepare for future events. For example, predicting the number of COVID-19 cases can help hospitals prepare resources and allocate staff accordingly.

### Decision Making:
Accurate forecasts support better decision-making. Governments and health officials can make informed decisions about lockdowns, travel restrictions, and vaccination efforts based on predicted trends.

### Resource Allocation:
Forecasting helps in efficiently allocating resources. By predicting demand, resources like medical supplies, hospital beds, and financial support can be distributed where they are needed most.

### Risk Management:
Forecasting identifies potential risks and challenges, allowing for proactive measures. For instance, anticipating a surge in cases helps in managing healthcare system pressures and preventing overburden.

### Budgeting:
It aids in budgeting and financial planning by estimating future needs and costs. For businesses, forecasting sales trends can help in setting budgets and financial strategies.

### Strategic Planning:
Forecasting supports long-term strategic planning. Understanding potential future scenarios allows organizations to develop strategies and adapt to changing conditions.

### Public Awareness:
Forecasting provides valuable information to the public, helping them make informed choices and understand potential future developments.




## Existing models:
In 2020, when machine learning (ML) was newly applied to COVID-19 prediction, several specific problems with existing solutions were evident:

1. **Immaturity of ML Models**:
   - **Lack of Established Practices**: Many ML models for COVID-19 were new and untested, leading to uncertainty about their reliability and effectiveness.
   - **Limited Training Data**: Early models had limited historical data to train on, which impacted their ability to make accurate predictions.

2. **Data Collection Issues**:
   - **Inconsistent Data Reporting**: Different countries and regions reported data in varying formats and frequencies, making it difficult to create a unified dataset.
   - **Delayed Data Updates**: There were delays in the availability of data due to reporting lags and processing times.

3. **High Variability**:
   - **Rapidly Changing Virus Dynamics**: The virus's behavior and spread changed quickly, with new variants emerging and altering transmission patterns, complicating predictions.
   - **Evolving Public Response**: Changes in public behavior, such as adherence to lockdowns or social distancing, affected the accuracy of forecasts.

4. **Model Overfitting**:
   - **Overfitting to Early Data**: Some models performed well on early data but struggled to adapt to new trends or unexpected changes in the pandemic.

5. **Computational Constraints**:
   - **Resource Limitations**: High-complexity ML models required significant computational resources, which were sometimes unavailable or infeasible for rapid deployment.

6. **Lack of Real-time Integration**:
   - **Challenges in Real-time Data Integration**: Integrating real-time data into ML models was challenging, leading to outdated predictions or a lack of timely updates.

7. **Uncertainty and Risk Management**:
   - **Uncertain Parameters**: Early models faced uncertainty regarding parameters such as infection rates, transmission dynamics, and the impact of interventions.
   - **Lack of Standardization**: There was no standard approach to model evaluation, making it difficult to compare the effectiveness of different ML models.

8. **Public and Policy Misunderstandings**:
   - **Misinterpretation of Results**: Predictions were sometimes misinterpreted by the public or policymakers, leading to confusion or inappropriate responses.
   - **Transparency Issues**: Limited transparency in how ML models generated predictions sometimes undermined public trust.

These issues highlight the challenges faced in using ML for COVID-19 prediction during the early stages of the pandemic and underscore the importance of refining models, improving data quality, and enhancing communication.



# Mounika's Part:


## Proposed System:
- This study uses machine learning (ML) to predict COVID-19 outcomes: new cases, deaths, and recoveries over 10 days.  
- Four models were tested:  
  - Linear Regression (LR)  
  - LASSO  
  - Support Vector Machine (SVM)  
  - Exponential Smoothing (ES)  
- **Key Findings:**  
  - Exponential Smoothing (ES) is the most accurate model.  
  - LR and LASSO also perform well in predicting key metrics.  
  - SVM performs poorly in all scenarios.  
- The study shows ML models, especially ES, are useful for managing the COVID-19 pandemic.  


## Advantages of proposed system:


**Advantages of the Project:**

**Performance Evaluation Metrics:**

1. **R-squared**:  
   - Measures how much of the data's variation the model can explain.  
   - **Why Introduced**: To check how well the model fits the data.  
   - **Advantage**: Higher values mean better prediction accuracy.  

2. **Adjusted R-squared**:  
   - Similar to R-squared, but adjusts for the number of factors in the model.  
   - **Why Introduced**: To avoid overfitting when using many predictors.  
   - **Advantage**: More accurate when dealing with complex models.  

3. **Mean Square Error (MSE)**:  
   - Averages the squared differences between predicted and actual values.  
   - **Why Introduced**: To measure prediction errors.  
   - **Advantage**: Focuses on large errors and helps identify big mistakes.  

4. **Mean Absolute Error (MAE)**:  
   - Averages the absolute differences between predicted and actual values.  
   - **Why Introduced**: To measure accuracy simply.  
   - **Advantage**: Less affected by large errors, making it easier to understand.  

5. **Root Mean Square Error (RMSE)**:  
   - The square root of MSE, making it easier to interpret.  
   - **Why Introduced**: To present errors in the same units as the data.  
   - **Advantage**: Balances the sensitivity to errors and interpretability.  

**Why Use These Metrics?**  
These metrics help evaluate how well the models perform and ensure they make accurate predictions.  

**Advantages:**  
- They give a clear picture of how good a model is.  
- They help compare different models to find the best one.  
- They guide improvements to make predictions more accurate.  



## System architecture:
![image](https://github.com/user-attachments/assets/e3af5f20-2e0d-456c-abe2-2b4ca5bb2144)
This diagram shows how **Sentiment Analysis** works in two main steps: **Training** and **Prediction**:

### **1. Training Phase**  
   - **Input Text**: The system uses labeled text data (with tags like Positive, Neutral, Negative).  
   - **Feature Extraction**: Important patterns and characteristics are extracted from the text.  
   - **Machine Learning Algorithm**: These features are fed into an algorithm to create a model. This model learns how to classify text based on sentiment.

### **2. Prediction Phase**  
   - **Input Text**: New, unlabeled text is processed.  
   - **Feature Extraction**: The same extraction process is applied to find patterns in the new text.  
   - **Classified Model**: The trained model predicts the sentiment of the text and assigns a tag (Positive, Neutral, or Negative).

In essence, the system learns from tagged examples and then applies that learning to classify new data.

# Rashmitha's part:

## Description of these:



### Linear Regression (LR)
#### Definition: Linear Regression finds the best straight line that predicts an outcome based on one or more input variables.
Example: If you want to predict the number of new COVID-19 cases based on past data, Linear Regression will fit a line to the historical data points to estimate future cases.

### Least Absolute Shrinkage and Selection Operator (LASSO)
#### Definition: LASSO is a type of regression that not only predicts outcomes but also selects the most important variables by reducing the impact of less important ones.
Example: To predict death rates, LASSO will use past data but focus on the most significant factors, such as age or underlying health conditions, and ignore less relevant ones.

### Support Vector Machine (SVM)
#### Definition: SVM finds the best boundary (or hyperplane) that separates different classes of data, often used for classification tasks.
 Example: To classify whether a region will have a high or low number of COVID-19 cases, SVM creates a boundary to distinguish between these categories based on factors like population density and previous case numbers.

### Exponential Smoothing (ES)
#### Definition: Exponential Smoothing gives more weight to recent observations to predict future values, making it good for time-series data.
Example: To forecast the number of recoveries over the next week, ES will focus more on recent recovery rates and use them to predict future recoveries, adjusting quickly to recent trends.



## Results








