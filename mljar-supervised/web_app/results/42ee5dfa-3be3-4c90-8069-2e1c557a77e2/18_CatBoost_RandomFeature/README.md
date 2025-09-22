# Summary of 18_CatBoost_RandomFeature

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 8
- **rsm**: 1.0
- **loss_function**: Logloss
- **eval_metric**: Logloss
- **explain_level**: 1

## Validation
 - **validation_type**: kfold
 - **k_folds**: 5
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

93.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.452628 | nan         |
| auc       | 0.83375  | nan         |
| f1        | 0.769231 |   0.186731  |
| accuracy  | 0.75     |   0.404876  |
| precision | 1        |   0.75202   |
| recall    | 1        |   0.0026778 |
| mcc       | 0.57735  |   0.75202   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.452628 |  nan        |
| auc       | 0.83375  |  nan        |
| f1        | 0.761905 |    0.404876 |
| accuracy  | 0.75     |    0.404876 |
| precision | 0.727273 |    0.404876 |
| recall    | 0.8      |    0.404876 |
| mcc       | 0.502519 |    0.404876 |


## Confusion matrix (at threshold=0.404876)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               14 |                6 |
| Labeled as 1 |                4 |               16 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
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
