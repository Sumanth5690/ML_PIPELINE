## Error for 18_CatBoost_GoldenFeatures

Golden Features not created. No continous features.
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\preprocessing.py", line 189, in fit_and_transform
    self._golden_features.fit(X_train[numeric_cols], y_train)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\goldenfeatures_transformer.py", line 145, in fit
    raise AutoMLException("Golden Features not created. No continous features.")
supervised.exceptions.AutoMLException: Golden Features not created. No continous features.


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 15_CatBoost_GoldenFeatures

Golden Features not created due to error (please check errors.md). Golden Features not created. No continous features. Input data shape: (32, 0), (32,)
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\preprocessing.py", line 189, in fit_and_transform
    self._golden_features.fit(X_train[numeric_cols], y_train)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\goldenfeatures_transformer.py", line 137, in fit
    raise AutoMLException(
supervised.exceptions.AutoMLException: Golden Features not created due to error (please check errors.md). Golden Features not created. No continous features. Input data shape: (32, 0), (32,)


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 4_Default_CatBoost_GoldenFeatures

Golden Features not created due to error (please check errors.md). Golden Features not created. No continous features. Input data shape: (32, 0), (32,)
Traceback (most recent call last):
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\preprocessing.py", line 189, in fit_and_transform
    self._golden_features.fit(X_train[numeric_cols], y_train)
  File "C:\Users\suman\OneDrive\Desktop\mljar\mljar-supervised\supervised\preprocessing\goldenfeatures_transformer.py", line 137, in fit
    raise AutoMLException(
supervised.exceptions.AutoMLException: Golden Features not created due to error (please check errors.md). Golden Features not created. No continous features. Input data shape: (32, 0), (32,)


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

