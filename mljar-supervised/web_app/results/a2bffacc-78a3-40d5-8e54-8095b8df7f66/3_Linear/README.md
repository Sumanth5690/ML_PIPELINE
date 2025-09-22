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

4.1 seconds

### Metric details:
| Metric   |      Score |
|:---------|-----------:|
| MAE      |  20.6346   |
| MSE      | 617.619    |
| RMSE     |  24.8519   |
| R2       |  -0.15133  |
| MAPE     |   0.379018 |



## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature     |    Learner_1 |
|:------------|-------------:|
| temperature |  0.102033    |
| intercept   | -7.26757e-17 |
| longitude   | -0.00827961  |
| wind_speed  | -0.0180245   |
| latitude    | -0.0376766   |


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
