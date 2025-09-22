# Summary of 3_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **num_class**: 3
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

10.1 seconds

### Metric details
|           |   Overcast |   Rain |   Sunny |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|-----------:|-------:|--------:|-----------:|------------:|---------------:|----------:|
| precision |          1 |      1 |       1 |          1 |           1 |              1 | 0.0785638 |
| recall    |          1 |      1 |       1 |          1 |           1 |              1 | 0.0785638 |
| f1-score  |          1 |      1 |       1 |          1 |           1 |              1 | 0.0785638 |
| support   |          5 |      5 |       5 |          1 |          15 |             15 | 0.0785638 |


## Confusion matrix
|                     |   Predicted as Overcast |   Predicted as Rain |   Predicted as Sunny |
|:--------------------|------------------------:|--------------------:|---------------------:|
| Labeled as Overcast |                       5 |                   0 |                    0 |
| Labeled as Rain     |                       0 |                   5 |                    0 |
| Labeled as Sunny    |                       0 |                   0 |                    5 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients

### Coefficients learner #1
|             |   Overcast |       Rain |      Sunny |
|:------------|-----------:|-----------:|-----------:|
| intercept   |  -0.131343 |  0.0582112 |  0.0731321 |
| Temperature |   0.899651 | -1.8835    |  0.98385   |
| Windy       |   0.146937 |  0.0871354 | -0.234072  |
| PlayTennis  |   1.49314  | -0.0330503 | -1.46009   |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
