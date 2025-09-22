# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model          |   Weight |
|:---------------|---------:|
| 2_DecisionTree |        1 |

### Metric details
|           |   5394 |   5621 |   20074 |   accuracy |   macro avg |   weighted avg |     logloss |
|:----------|-------:|-------:|--------:|-----------:|------------:|---------------:|------------:|
| precision |      1 |      1 |       1 |          1 |           1 |              1 | 1.19209e-07 |
| recall    |      1 |      1 |       1 |          1 |           1 |              1 | 1.19209e-07 |
| f1-score  |      1 |      1 |       1 |          1 |           1 |              1 | 1.19209e-07 |
| support   |      5 |      5 |       5 |          1 |          15 |             15 | 1.19209e-07 |


## Confusion matrix
|                  |   Predicted as 5394 |   Predicted as 5621 |   Predicted as 20074 |
|:-----------------|--------------------:|--------------------:|---------------------:|
| Labeled as 5394  |                   5 |                   0 |                    0 |
| Labeled as 5621  |                   0 |                   5 |                    0 |
| Labeled as 20074 |                   0 |                   0 |                    5 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
