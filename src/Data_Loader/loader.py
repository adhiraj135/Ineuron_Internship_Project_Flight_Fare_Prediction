import pandas as pd



class loader:
    def __init__(self,file_object,log):
        self.path='Dataset/DATABASE_INPUT_FILE.csv'
        self.prediction_path='Dataset/prediction_file.csv'
        self.input_path="Dataset/input_file.csv"
        self.file_object=file_object
        self.log=log

    def load(self):
        self.log.log(self.file_object, "data loading started")
        try:
            df=pd.read_csv(self.path)
            self.log.log(self.file_object,"data successfully loaded")
            return df

        except Exception as e:
            self.log.log(self.file_object,"exception occurred while data loading: %s" %e)
            self.log.log(self.file_object,"data loading unsuccessful")
            raise e

    def input_load(self):
        self.log.log(self.file_object, "input data loading started")
        try:
            df = pd.read_csv(self.input_path)
            self.log.log(self.file_object, "input data successfully loaded")
            return df

        except Exception as e:
            self.log.log(self.file_object, "exception occurred while input data loading: %s" % e)
            self.log.log(self.file_object, "input data loading unsuccessful")
            raise e

    def prediction_data_loader(self):
        self.log.log(self.file_object,"prediction data which was created using the input by users on webpage operation started")
        try:
            pred_df=pd.read_csv(self.prediction_path)
            self.log.log(self.file_object, "prediction data successfully loaded")
            return pred_df
        except Exception as e:
            self.log.log(self.file_object, "error in prediction data loading : %s"%e)
            self.log.log(self.file_object, "prediction data loading is unsuccessful")
            raise e