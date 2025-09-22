# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                  |   Weight |
|:-----------------------|---------:|
| 1_Baseline             |        3 |
| 2_DecisionTree         |        1 |
| 6_Default_RandomForest |        2 |

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.678106 |  nan        |
| auc       | 0.590909 |  nan        |
| f1        | 0.777778 |    0.461848 |
| accuracy  | 0.68     |    0.461848 |
| precision | 1        |    0.648989 |
| recall    | 1        |    0.366272 |
| mcc       | 0.416598 |    0.461848 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.678106 |  nan        |
| auc       | 0.590909 |  nan        |
| f1        | 0.777778 |    0.461848 |
| accuracy  | 0.68     |    0.461848 |
| precision | 0.636364 |    0.461848 |
| recall    | 1        |    0.461848 |
| mcc       | 0.416598 |    0.461848 |


## Confusion matrix (at threshold=0.461848)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |                3 |                8 |
| Labeled as 1 |                0 |               14 |

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
