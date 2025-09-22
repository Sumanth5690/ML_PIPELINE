# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model          |   Weight |
|:---------------|---------:|
| 2_DecisionTree |        1 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.548734 |  nan        |
| auc       | 0.62     |  nan        |
| f1        | 0.666667 |    0.3      |
| accuracy  | 0.7      |    0.411765 |
| precision | 1        |    0.411765 |
| recall    | 1        |    0.3      |
| mcc       | 0.5      |    0.411765 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.548734 |  nan        |
| auc       | 0.62     |  nan        |
| f1        | 0.571429 |    0.411765 |
| accuracy  | 0.7      |    0.411765 |
| precision | 1        |    0.411765 |
| recall    | 0.4      |    0.411765 |
| mcc       | 0.5      |    0.411765 |


## Confusion matrix (at threshold=0.411765)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                5 |                0 |
| Labeled as 1 |                3 |                2 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
