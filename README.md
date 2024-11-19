# Mobile Device Usage and User Behavior

## Main objective and dataset description

This work aims at Analyzing Mobile Usage Patterns Across Devices and Classifying User Behavior among five levels of intensity, ranging from light to extreme usage.

The dataset have 700 rows 11 columns and contains no missing values. It provides a comprehensive analysis of mobile device usage patterns and user behavior classification. It contains 700 samples of user data, including metrics such as app usage time, screen-on time, battery drain, and data consumption. Each entry is categorized into one of five user behavior classes, ranging from light to extreme usage, allowing for insightful analysis and modeling.

Key Features:

- User ID: Unique identifier for each user.
- Device Model: Model of the user's smartphone.
- Operating System: The OS of the device (iOS or Android).
- App Usage Time: Daily time spent on mobile applications, measured in minutes.
- Screen On Time: Average hours per day the screen is active.
- Battery Drain: Daily battery consumption in mAh.
- Number of Apps Installed: Total apps available on the device.
- Data Usage: Daily mobile data consumption in megabytes.
- Age: Age of the user.
- Gender: Gender of the user (Male or Female).
- User Behavior Class: Classification of user behavior based on usage patterns (1 to 5).

The objective is to achieve to predict the User Behavior Class based on the other columns.

## Data Exploration and Preprocessing

Key exploration findings

- The dataset have a good class balance
- Device Model and Gender features are well balanced but Operating System is unbalanced toward Android users.
- None of the numerical Features have a normal distribution.
- Age is not correlated to any other numerical features or the target class.  
- The other numerical Features are very correlated to each other r is in [0.947, 0.981]
- There is an obvious relationship between Device Model and Operating System categorical Features  
- There is no relationship between the categorical features and the target class.
- We can see that classes are very well clustered making the classification easier.

Data Preprocessing steps

- The dataset have been splited in train and test set, with a test size of 20 %
- Dropped 'User ID' and 'Operating System' features because they don't add meaningfull informations
- One hot encode 'Device Model' and 'Gender'
- Tested different scalers and transformers on numeric features to achieve a normal shape
- Found out that a Quantile Transformer gives the best result

## Modeling

Every model have been trained using a 5-Fold cross validation with AUC ROC curve as the metric to maximize with one vs one strategy for handling multi class classification.

The models that have been trained are the following:

- k Nearest Kneighbors Classifier with tuning of n_neighbors parameter in values [3, 5, 7, 9, 11]
- Support Vector Machine Classifier with tuning of regularization parameter C in values [1, 0.1, 0.01, 0.001] and kernels in ['linear', 'rbf', 'sigmoid']
- Logistic Regression with tuning of regularization parameter C in values [1, 0.1, 0.01, 0.001]
- Decision Tree Classifier with tuning of the maximum depth from 1 to 10
- Random Forest Classifier with tuning of the number of estimators in [20, 50, 100, 200] of the maximum depth from 1 to 10

- Gradient Boosting Classifier with tuning of:
  - the learning rate in [0.2, 0.1, 0.01, 0.001]
  - the number of estimators in [20, 50, 100, 200]
  - the maximum depth from 1 to 5
  - the percentage of the data to use during training [1, 0.7, 0.5]

## Results and observations

Best Model from Cross Validation                                                         | Test - AUC ROC score | Test - f1-score  |
-----------------------------------------------------------------------------------------|----------------------|------------------|
SVC(C=1, kernel='linear')                                                                |                  1.0 |              1.0 |
LogisticRegression(C=1)                                                                  |                  1.0 |              1.0 |
GradientBoostingClassifier(learning_rate=0.2, max_depth=1, n_estimators=20, subsample=1) |                  1.0 |              1.0 |
RandomForestClassifier(max_depth=1, n_estimators=20)                                     |                  1.0 |         0.993328 |
DecisionTreeClassifier(max_depth=3, )                                                    |             0.996429 |         0.993712 |
KNeighborsClassifier(n_neighbors=9)                                                      |             0.996146 |         0.973377 |

Observations:

- KNN, Decision Tree Classifier and Random Forest achieved near perfect results.
- Support Vector Classifier, Multi-class Logistic Regression and Gradient Boosting achieve perfect results.

The Model that achieves both best performance and good interpretability would be the Logistic Regression:  it would be a great choice to classify User Behavior based on app usage time, screen-on time, battery drain, data consumption, with precision and assure good interpretability in case of explaining to potential stakeholders or users the result of the prediction and / or debugging in case of unexpecting results.

## Going further

One improvement that might be considered is the interpretability of the model. Although logistic regression is known to be an intuitive model, the input features have been heavily transformed, so we need to ensure that we can interpret the results of the model with regard to the original features rather than the transformed ones.
