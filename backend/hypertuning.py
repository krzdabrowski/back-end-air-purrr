#!/usr/bin/python3.7

from datetime import datetime
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
        
def nonlinear_hyperparameters_tuning(X_daily, Y_pm25, Y_pm10):
    hyperparameters_decision_tree = {
        'max_features': ['sqrt', 'log2', None]
    }
    
    hyperparameters_random_forest = {
        'max_features': ['sqrt', 'log2', None],
        'n_estimators': [50, 100, 150, 200, 250]
    }
    
    print('\nDecision tree hyperparameters tuning results for PM25:')
    result_decision_tree_pm25 = execute_hypertuning(DecisionTreeRegressor(), hyperparameters_decision_tree, X_daily, Y_pm25)
    
    print('\nDecision tree hyperparameters tuning results for PM10:')
    result_decision_tree_pm10 = execute_hypertuning(DecisionTreeRegressor(), hyperparameters_decision_tree, X_daily, Y_pm10)
        
    
    print('\n\nRandom forest hyperparameters tuning results for PM25:')
    result_random_forest_pm25 = execute_hypertuning(RandomForestRegressor(), hyperparameters_random_forest, X_daily, Y_pm25)
    
    print('\nRandom forest hyperparameters tuning results for PM10:')
    result_random_forest_pm10 = execute_hypertuning(RandomForestRegressor(), hyperparameters_random_forest, X_daily, Y_pm10)
        
    return ((result_decision_tree_pm25, result_decision_tree_pm10), (result_random_forest_pm25, result_random_forest_pm10))
    
def xgboost_hyperparameters_tuning(X_daily, Y_pm25, Y_pm10):
    hyperparameters_xgboost = {
        'learning_rate': [0.001, 0.01, 0.1, 0.3],
        'n_estimators': [50, 100, 200, 500, 1000],
    }
    
    start_time_xgboost = datetime.now()

    print('\n\nXGBoost hyperparameters tuning results for PM25:')
    result_pm25 = execute_hypertuning(XGBRegressor(), hyperparameters_xgboost, X_daily, Y_pm25)
    
    print('\nXGBoost hyperparameters tuning results for PM10:')
    result_pm10 = execute_hypertuning(XGBRegressor(), hyperparameters_xgboost, X_daily, Y_pm10)
    
    end_time_xgboost = datetime.now() - start_time_xgboost
    print(f'Execution time for xgboost was: {end_time_xgboost} hours')
    
    return (result_pm25, result_pm10)
    
def execute_hypertuning(model, hyperparameters, X_daily, Y_daily):
    # grid search
    cv_test= KFold(n_splits=5)
    grid_search = GridSearchCV(model, hyperparameters, scoring='neg_mean_squared_error', n_jobs=-1, cv=cv_test)
    grid_result = grid_search.fit(X_daily, Y_daily)

    # summarize results
    print(f'Best hyperparameters: {grid_result.best_score_} using {grid_result.best_params_}')
    
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print(f'{mean} ({stdev}) with: {param}')
        
    return grid_result