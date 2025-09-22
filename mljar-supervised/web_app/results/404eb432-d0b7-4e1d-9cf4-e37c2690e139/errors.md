## Error for 1_Baseline

y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\utils\_param_validation.py", line 218, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 3240, in log_loss
    transformed_labels, y_pred = _validate_multiclass_probabilistic_prediction(
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 229, in _validate_multiclass_probabilistic_prediction
    raise ValueError(
ValueError: y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 2_DecisionTree

y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\utils\_param_validation.py", line 218, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 3240, in log_loss
    transformed_labels, y_pred = _validate_multiclass_probabilistic_prediction(
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 229, in _validate_multiclass_probabilistic_prediction
    raise ValueError(
ValueError: y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 3_Linear

This solver needs samples of at least 2 classes in the data, but the data contains only one class: 0
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\algorithms\sklearn.py", line 39, in fit
    self.model.fit(X, y, sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\base.py", line 1365, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\linear_model\_logistic.py", line 1335, in fit
    raise ValueError(
ValueError: This solver needs samples of at least 2 classes in the data, but the data contains only one class: 0


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 1_Default_Xgboost

y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 265, in train
    self.callbacks.on_iteration_end(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\callbacks\callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\callbacks\early_stopping.py", line 96, in on_iteration_end
    train_loss = self.metric(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\utils\_param_validation.py", line 218, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 3240, in log_loss
    transformed_labels, y_pred = _validate_multiclass_probabilistic_prediction(
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 229, in _validate_multiclass_probabilistic_prediction
    raise ValueError(
ValueError: y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 2_Default_NeuralNetwork

1
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 267, in train
    self.predictions(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 119, in predictions
    y_validation_columns = preproces.prepare_target_labels(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\preprocessing.py", line 509, in prepare_target_labels
    d["prediction_{}".format(labels[i])] = y[:, i]
KeyError: 1


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 3_Default_RandomForest

y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\algorithms\sklearn.py", line 143, in fit
    tr = self.log_metric(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\utils\metric.py", line 24, in logloss
    ll = log_loss(y_true, y_predicted.astype(np.float32), sample_weight=sample_weight)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\utils\_param_validation.py", line 218, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 3240, in log_loss
    transformed_labels, y_pred = _validate_multiclass_probabilistic_prediction(
  File "C:\Users\suman\OneDrive\Desktop\mljar\.venv\lib\site-packages\sklearn\metrics\_classification.py", line 229, in _validate_multiclass_probabilistic_prediction
    raise ValueError(
ValueError: y_true contains only one label (0). Please provide the list of all expected class labels explicitly through the labels argument.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

