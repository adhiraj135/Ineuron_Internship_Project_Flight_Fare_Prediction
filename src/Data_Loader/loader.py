import pandas as pd
from src.logger import log


class loader:
    def __init__(self):
        self.path='Dataset/DATABASE_INPUT_FILE.csv'
        self.prediction_path='Dataset/prediction_file.csv'
        self.file=open('src/logs/training_logs/data_loader_log.txt',"a+")
        self.log=log()
        self.prediction_file_object=open('src/logs/prediction_logs/prediction_data_loader_log.txt','a+')

    def load(self):
        self.log.log(self.file, "data loading started")
        try:
            df=pd.read_csv(self.path)
            self.log.log(self.file,"data successfully loaded")
            return df

        except Exception as e:
            self.log.log(self.file,"exception occurred while data loading: %s" %e)
            self.log.log(self.file,"data loading unsuccessful")
            raise e

    def prediction_data_loader(self):
        self.log.log(self.prediction_file_object,"prediction data which was created using the input by users on webpage operation started")
        try:
            pred_df=pd.read_csv(self.prediction_path)
            self.log.log(self.prediction_file_object, "prediction data successfully loaded")
            return pred_df
        except Exception as e:
            self.log.log(self.file, "error in prediction data loading : %s"%e)
            self.log.log(self.file, "prediction data loading is unsuccessful")
            raise e