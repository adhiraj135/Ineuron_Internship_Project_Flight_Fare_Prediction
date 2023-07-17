from src.Database.database_builder import database
from src.logger import log
from src.Data_Loader.loader import loader
from src.Feature_Engineering.preprocessing import preprocessor
from src.Feature_Engineering.encoding import encoder
from src.Modelling.model_selection import model_selection
from src.utils import utils
from sklearn.model_selection import train_test_split


class training:
    def __init__(self):
        self.log=log()
        self.file=open("src/logs/training_logs.txt", "a+")
        self.utils=utils(self.file,self.log)
        self.database = database(self.file,self.log)
        self.load = loader(self.file,self.log)
        self.encoder = encoder(file_object=self.file,log=self.log)
        self.preprocessor = preprocessor(file_object=self.file,log=self.log)
        self.model = model_selection(self.file,self.log)


    def train(self):
        self.log.log(self.file,"training process started!!")
        try:
            self.log.log(self.file,"cassandra database builder operation started")
            df=self.database.data_load()
            columns,DataType=self.database.extract_columns_and_datatype(df)
            print(columns,DataType)
            self.database.database_table_creation(columns=columns,data_type=DataType)
            self.database.database_inserion(df,columns=columns)
            self.database.extract_data_form_database_into_lacal()
            self.log.log(self.file, "cassandra database builder operation successful")
            self.log.log(self.file, "Dataset loading Started!!")
            data = self.load.load()
            data=df
            data.drop(columns=["ID"], inplace=True)
            print(data)
            self.log.log(self.file, "Dataset loading completed!!")
            self.log.log(self.file, "Feature Engineering Started!!")
            data = self.preprocessor.drop_null_values(data)
            column_list = ['Date_of_Journey', 'Dep_Time', 'Arrival_Time']
            data = self.preprocessor.change_dtype_to_datetime(data, column_list)
            data = self.preprocessor.separate_date_columns(data, column_name='Date_of_Journey')
            data = self.preprocessor.separate_time_columns(data, col_list=['Dep_Time', 'Arrival_Time'])
            data = self.preprocessor.duration_column_processor(data, "Duration")
            data = self.preprocessor.drop_unneccessary_columns(data, col_list=['Additional_Info', 'Route',
                                                                               'Date_of_Journey_year'])
            data = self.encoder.one_hot(data, 'Source')
            data = self.encoder.mean_encoding(data, column=['Airline', 'Destination'])
            data = self.encoder.manual_encoding(data, 'Total_Stops')
            data = self.preprocessor.drop_unneccessary_columns(data, col_list=['Source', 'Duration'])
            data.to_csv("Dataset/input_file.csv",header=True,index=False)
            self.log.log(self.file, "Feature Engineering Completed!!")
            x = data.drop(columns=['Price'], axis=1)
            y = data['Price']
            print(x,y)
            x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.25)
            self.log.log(self.file, "Best model selection Started!!")
            model_name, model = self.model.best_model(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test)
            self.log.log(self.file, "Best model selection Completed!!")
            self.utils.model_saver(model_name, model)
            self.log.log(self.file, "Training Successful!!")


        except Exception as e:
            self.log.log(self.file,"exception occurred while training operation : %s"%e)
            self.log.log(self.file,"training operation unsuccessful")
            raise e

