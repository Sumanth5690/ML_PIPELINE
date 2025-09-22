# Summary of 3_Linear

[<< Go back](../README.md)


## Linear Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True

## Optimized metric
rmse

## Training time

9.9 seconds

### Metric details:
| Metric   |          Score |
|:---------|---------------:|
| MAE      | 1282.57        |
| MSE      |    2.28949e+06 |
| RMSE     | 1513.11        |
| R2       |   -0.0699987   |
| MAPE     |    7.36202     |



## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature   |   Learner_1 |
|:----------|------------:|
| V25       |  0.0908465  |
| V26       |  0.0857661  |
| V16       |  0.0757411  |
| V11       |  0.0662835  |
| V12       |  0.0484719  |
| V13       |  0.0360582  |
| V2        |  0.0349168  |
| V24       |  0.0323894  |
| V23       |  0.0323108  |
| V27       |  0.0204339  |
| V21       |  0.0190998  |
| V8        |  0.014318   |
| V5        |  0.0141311  |
| V20       |  0.0136654  |
| V14       |  0.012807   |
| intercept |  0.0105172  |
| V7        |  0.00672383 |
| V22       |  0.00641448 |
| Time      |  0.00426694 |
| V17       | -0.00236397 |
| V15       | -0.00246543 |
| V10       | -0.0242216  |
| V1        | -0.0335037  |
| V9        | -0.0370957  |
| V6        | -0.0373648  |
| V4        | -0.0430787  |
| V18       | -0.0474564  |
| V28       | -0.0508795  |
| V3        | -0.0549587  |
| V19       | -0.075781   |
| Class     | -0.167533   |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions (Fold 1)
![SHAP worst decisions from fold 1](learner_fold_0_shap_worst_decisions.png)
### Top-10 Best decisions (Fold 1)
![SHAP best decisions from fold 1](learner_fold_0_shap_best_decisions.png)

[<< Go back](../README.md)
