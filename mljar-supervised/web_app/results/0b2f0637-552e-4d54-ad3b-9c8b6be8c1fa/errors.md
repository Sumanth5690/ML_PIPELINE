## Error for 2_DecisionTree

could not convert string to float: '2021-08-23'
Traceback (most recent call last):
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\algorithms\sklearn.py", line 39, in fit
    self.model.fit(X, y, sample_weight=sample_weight)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\base.py", line 1365, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\tree\_classes.py", line 1024, in fit
    super()._fit(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\tree\_classes.py", line 252, in _fit
    X, y = validate_data(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py", line 2966, in validate_data
    X = check_array(X, input_name="X", **check_X_params)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py", line 1053, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\_array_api.py", line 757, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 2168, in __array__
    arr = np.asarray(values, dtype=dtype)
ValueError: could not convert string to float: '2021-08-23'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 2_Default_Xgboost

could not convert string to float: '2021-08-23'
Traceback (most recent call last):
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\algorithms\xgboost.py", line 166, in fit
    dtrain = xgb.DMatrix(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\xgboost\core.py", line 729, in inner_f
    return func(**kwargs)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\xgboost\core.py", line 885, in __init__
    handle, feature_names, feature_types = dispatch_data_backend(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\xgboost\data.py", line 1382, in dispatch_data_backend
    return _from_numpy_array(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\xgboost\data.py", line 269, in _from_numpy_array
    data, _ = _ensure_np_dtype(data, data.dtype)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\xgboost\data.py", line 239, in _ensure_np_dtype
    data = data.astype(dtype, copy=False)
ValueError: could not convert string to float: '2021-08-23'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 3_Default_NeuralNetwork

could not convert string to float: '2021-08-23'
Traceback (most recent call last):
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\model_framework.py", line 192, in train
    ].fit_and_transform(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\preprocessing\preprocessing.py", line 271, in fit_and_transform
    scale.fit(X_train)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\preprocessing\scale.py", line 20, in fit
    X[c] = X[c].astype(float)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 6662, in astype
    new_data = self._mgr.astype(dtype=dtype, copy=copy, errors=errors)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\internals\managers.py", line 430, in astype
    return self.apply(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\internals\managers.py", line 363, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\internals\blocks.py", line 784, in astype
    new_values = astype_array_safe(values, dtype, copy=copy, errors=errors)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\dtypes\astype.py", line 237, in astype_array_safe
    new_values = astype_array(values, dtype, copy=copy)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\dtypes\astype.py", line 182, in astype_array
    values = _astype_nansafe(values, dtype, copy=copy)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\dtypes\astype.py", line 133, in _astype_nansafe
    return arr.astype(dtype, copy=True)
ValueError: could not convert string to float: '2021-08-23'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 4_Default_RandomForest

could not convert string to float: '2021-08-23'
Traceback (most recent call last):
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 1183, in _fit
    trained = self.train_model(params)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\base_automl.py", line 388, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\model_framework.py", line 249, in train
    learner.fit(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\supervised\algorithms\sklearn.py", line 122, in fit
    self.model.fit(X, np.ravel(y), sample_weight=sample_weight)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\base.py", line 1365, in wrapper
    return fit_method(estimator, *args, **kwargs)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\ensemble\_forest.py", line 359, in fit
    X, y = validate_data(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py", line 2971, in validate_data
    X, y = check_X_y(X, y, **check_params)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py", line 1368, in check_X_y
    X = check_array(
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py", line 1053, in check_array
    array = _asarray_with_order(array, order=order, dtype=dtype, xp=xp)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\_array_api.py", line 757, in _asarray_with_order
    array = numpy.asarray(array, order=order, dtype=dtype)
  File "C:\Users\suman\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 2168, in __array__
    arr = np.asarray(values, dtype=dtype)
ValueError: could not convert string to float: '2021-08-23'


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

