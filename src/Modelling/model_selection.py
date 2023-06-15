from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.metrics import r2_score
from src.logger import log

class model_selection:
    def __init__(self):
        self.log=log()
        self.file_object=open("src/training_logs/model_logs.txt","a+")

    def best_param_for_random_forest(self,x,y):
        self.log.log(self.file_object,"best parameters for random forest regressor extraction started")
        try:
           param_grid_random={
            "n_estimators": [int(x) for x in np.linspace(start=1000, stop=1200, num=6)],
            "max_features": ["auto", "sqrt"],
            "max_depth": [int(x) for x in np.linspace(start=5, stop=40, num=4)],
            "min_samples_split": [5, 10, 15, 100]
           }
           random_grid=GridSearchCV(estimator=RandomForestRegressor(),param_grid=param_grid_random,cv=3,verbose=2,n_jobs=-1)
           random_grid.fit(x,y)

           n_estimators=random_grid.best_params_['n_estimators']
           max_features=random_grid.best_params_['max_features']
           max_depth=random_grid.best_params_['max_depth']
           min_samples_split=random_grid.best_params_['min_samples_split']

           self.random=RandomForestRegressor(n_estimators=n_estimators,max_features=max_features,max_depth=max_depth,min_samples_split=min_samples_split)
           self.random.fit(x,y)
           self.log.log(self.file_object,"best param for random fores are" + "\t" + "max_depth : %s" % max_depth + "\t" + "n_estimators : %s" % n_estimators + "\t" + "min_samples_split : %s" % min_samples_split + "\t"  + "max_features : %s" % max_features)
           self.log.log(self.file_object, "best parameters for random forest regressor extraction successful")
           return self.random

        except Exception as e:
            self.log.log(self.file_object, "error while parameters for random forest regressor extraction : %s"%e)
            self.log.log(self.file_object, "best parameters for random forest regressor extraction unsuccessful")
            raise e

    def get_param_for_xgboost(self,x,y):
        self.log.log(self.file_object, "best parameters for xgbosst regressor extraction started")
        try:
           xgb_param={
            "learning_rate": [0.01, .1, 0.5, .001],
            "max_depth": [3, 5, 10, 16],
            "n_estimators": [10, 50, 100, 200]
            }
           grid_xgb = GridSearchCV(estimator=XGBRegressor(objective='reg:linear'), param_grid=xgb_param, verbose=3,
                                        cv=5)
           grid_xgb.fit(x,y)

           learning_rate = grid_xgb.best_params_['learning_rate']
           max_depth = grid_xgb.best_params_['max_depth']
           n_estimators = grid_xgb.best_params_['n_estimators']

           self.xgb = XGBRegressor(objective='reg:linear', learning_rate=learning_rate, max_depth=max_depth, n_estimators=n_estimators)
           self.xgb.fit(x,y)
           self.log.log(self.file_object,"best param for random fores are" + "\t" + "max_depth : %s" % max_depth + "\t" + "n_estimators : %s" % n_estimators + "\t" + "learning_rate : %s" % learning_rate)
           self.log.log(self.file_object, "best parameters for xgbosst regressor extraction successful")
           return self.xgb

        except Exception as e:
            self.log.log(self.file_object, "error in best parameters for xgbosst regressor extraction : %s"%e)
            self.log.log(self.file_object, "best parameters for xgbosst regressor extraction started")
            raise e

    def best_model(self,x_train,y_train,x_test,y_test):
        self.log.log(self.file_object, "best model operation started")
        try:
           random_forest_reg=self.best_param_for_random_forest(x=x_train,y=y_train)
           prediction_random=random_forest_reg.predict(x_test)
           random_score=r2_score(y_test,prediction_random)
           print(random_score)


           xgb_reg=self.get_param_for_xgboost(x=x_train,y=y_train)
           prediction_xgb=xgb_reg.predict(x_test)
           xgb_score=r2_score(y_test,prediction_xgb)
           print(xgb_score)

           if random_score<xgb_score:
               self.log.log(self.file_object, "best model to be selected is XGboost")
               return 'xgboost',xgb_reg
           else:
               self.log.log(self.file_object, "best model to be selected is Random forest")
               return 'random_forest',random_forest_reg

        except Exception as e:
            self.log.log(self.file_object, "error while best model selection : %s"%e)
            self.log.log(self.file_object, "best model selection unsuccessful")
            raise e
