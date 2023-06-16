import os
from src.Data_Loader.loader import loader
from src.Feature_Engineering.preprocessing import preprocessor
from src.Feature_Engineering.encoding import encoder
from src.utils import utils
from src.logger import log


class prediction:
    def __init__(self):
        self.log=log()
        self.prediction_file_object=open('src/logs/prediction_logs.txt','a+')
        self.model_path='src/saved_model'
        self.utils=utils(file_object=self.prediction_file_object,log=self.log)
        self.preprocessor = preprocessor(file_object=self.prediction_file_object,log=self.log)
        self.encoder = encoder(file_object=self.prediction_file_object,log=self.log)
        self.load = loader(file_object=self.prediction_file_object,log=self.log)


    def predict(self):
        self.log.log(self.prediction_file_object, "prediction started!!")
        try:
            self.log.log(self.prediction_file_object,"prediction Data loading started!!")
            data=self.load.prediction_data_loader()
            self.log.log(self.prediction_file_object, "input Data loading completed!!")
            self.log.log(self.prediction_file_object, "Prediction Feature Engineering started!!")
            data=self.preprocessor.drop_null_values(data)
            column_list=['Date_of_Journey','Dep_Time','Arrival_Time']
            data=self.preprocessor.change_dtype_to_datetime(data,column_list)
            data=self.preprocessor.separate_date_columns(data,column_name='Date_of_Journey')
            data=self.preprocessor.separate_time_columns(data,col_list=['Dep_Time','Arrival_Time'])
            data=self.preprocessor.duration_column_processor(data,"Duration")
            data=self.preprocessor.drop_unneccessary_columns(data,col_list=['Additional_Info','Route','Date_of_Journey_year'])
            print(data.values)
            df=self.load.load()
            data=self.encoder.dict_value(train_data=df,pred_data=data,column='Airline')
            data=self.encoder.dict_value(train_data=df, pred_data=data, column='Destination')
            data=self.encoder.manual_encoding(data,'Total_Stops')
            final_train_data=self.load.input_load()
            data=self.encoder.source_column_addition(train_data=final_train_data,pred_data=data)
            self.encoder.one_hot(data,'Source')
            data = self.preprocessor.drop_unneccessary_columns(data, col_list=['Source', 'Duration'])
            self.log.log(self.prediction_file_object, "Prediction Feature Engineering started!!")
            self.log.log(self.prediction_file_object, "model loading started!!")
            name = os.listdir(self.model_path)[0]
            model = self.utils.model_loader(model_name=name)
            self.log.log(self.prediction_file_object, "model : %s loaded successfully" % name)
            result = model.predict(data.values)
            self.log.log(self.prediction_file_object, "prediction completed!!")
            return result[0]

        except Exception as e:
            self.log.log(self.prediction_file_object, "error in prediction : %s"%e)
            self.log.log(self.prediction_file_object, "prediction unsuccessful")
            raise e