# Summary of 3_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

3.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.891185 | nan         |
| auc       | 0.4      | nan         |
| f1        | 0.666667 |   0.0834537 |
| accuracy  | 0.7      |   0.495343  |
| precision | 1        |   0.495343  |
| recall    | 1        |   0.0834537 |
| mcc       | 0.5      |   0.495343  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.891185 |  nan        |
| auc       | 0.4      |  nan        |
| f1        | 0.571429 |    0.495343 |
| accuracy  | 0.7      |    0.495343 |
| precision | 1        |    0.495343 |
| recall    | 0.4      |    0.495343 |
| mcc       | 0.5      |    0.495343 |


## Confusion matrix (at threshold=0.495343)
|                 |   Predicted as Cold |   Predicted as Hot |
|:----------------|--------------------:|-------------------:|
| Labeled as Cold |                   5 |                  0 |
| Labeled as Hot  |                   3 |                  2 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature    |   Learner_1 |
|:-----------|------------:|
| Outlook    |   0.623359  |
| intercept  |  -0.0063323 |
| PlayTennis |  -0.336054  |
| Windy      |  -0.435705  |


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



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold 1)
![SHAP worst decisions class 0 from Fold 1](learner_fold_0_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold 1)
![SHAP best decisions class 0 from Fold 1](learner_fold_0_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 1)
![SHAP worst decisions class 1 from Fold 1](learner_fold_0_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold 1)
![SHAP best decisions class 1 from Fold 1](learner_fold_0_shap_class_1_best_decisions.png)

[<< Go back](../README.md)
