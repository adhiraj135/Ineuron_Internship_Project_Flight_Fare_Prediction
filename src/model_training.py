from src.Database.database_builder import database
from src.logger import log
from src.Data_Loader.loader import loader

class training:
    def __init__(self):
        self.log=log()
        self.database=database()
        self.load=loader()
        self.file=open("src/logs/training_logs/training_logs.txt","a+")


    def train(self):
        self.log.log(self.file,"training process started!!")
        try:
            self.log.log(self.file,"cassandra database builder operation started")
            data=self.database.data_load()
            columns,DataType=self.database.extract_columns_and_datatype(data)
            self.database.database_table_creation(columns=columns,data_type=DataType)
            self.database.database_inserion(data,columns=columns)
            self.database.extract_data_form_database_into_lacal(columns=columns)
            self.log.log(self.file, "cassandra database builder operation successful")
            self.log.log(self.file, "Dataset loading Started!!")
            data = self.load.load()
            self.log.log(self.file, "Dataset loading completed!!")
            self.log.log(self.file, "Data Preprocessing Started!!")



        except Exception as e:
            self.log.log(self.file,"exception occurred while training operation : %s"%e)
            self.log.log(self.file,"training operation unsuccessful")
            return e
