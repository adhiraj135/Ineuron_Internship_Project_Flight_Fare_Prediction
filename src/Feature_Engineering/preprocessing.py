from src.logger import log
import pandas as pd



class preprocessor:
    def __init__(self,file_object,log):
        self.log=log
        self.file_object=file_object
        self.prediction_file_object = open('src/logs/prediction_logs/encoding_log.txt', 'a+')


    def drop_null_values(self, data):
        self.log.log(self.file_object,"dropping null values operation started")
        try:
           data.dropna(inplace=True)
           self.log.log(self.file_object,"dropping null values operation successful")
           return data
        except Exception as e:
            self.log.log(self.file_object, "Error while  dropping null values operation : %s"%e)
            self.log.log(self.file_object, "dropping null values operation unsuccessful")
            raise e

    def change_dtype_to_datetime(self,data,column_list):
        self.log.log(self.file_object,"Changing dtype to datetime operation started")
        try:
           for column_name in column_list:
               data[column_name]=pd.to_datetime(data[column_name])
           self.log.log(self.file_object, "Changing dtype to datetime operation successful")
           return data
        except Exception as e:
            self.log.log(self.file_object, "error in Changing dtype to datetime operation : %s"%e)
            self.log.log(self.file_object, "Changing dtype to datetime operation successful")
            raise e

    def separate_date_columns(self,data,column_name):
        self.log.log(self.file_object, "Separating Date columns operation started")
        try:
            data[column_name+"_day"]=data[column_name].dt.day
            data[column_name+"_month"]=data[column_name].dt.month
            data[column_name+"_year"]=data[column_name].dt.year
            data.drop(columns=column_name,axis=1,inplace=True)
            self.log.log(self.file_object, "Separating Date columns operation successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "Error in Error in Separating Date columns operation : %s"%e)
            self.log.log(self.file_object, "Separating Date columns operation unsuccessful")
            raise e

    def separate_time_columns(self,data,col_list):
        self.log.log(self.file_object, "Separating Time columns operation started")
        try:
            for col in col_list:
               data[col+"_hour"]=data[col].dt.hour
               data[col+"_minute"]=data[col].dt.minute
            data.drop(columns=col_list, axis=1, inplace=True)
            self.log.log(self.file_object, "Separating Time columns operation successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "Separating Time columns operation : %s"%e)
            self.log.log(self.file_object, "Separating Time columns operation unsuccessful")
            raise e


    def prepocess_duration(self, x):
        if 'h' not in x:
            x = '0h ' + x
        elif 'm' not in x:
            x = x + ' 0h'
        return x

    def duration_column_processor(self, data, col_name):
        self.log.log(self.file_object,"extraction from duration column started")
        try:
            data[col_name] = data[col_name].apply(self.prepocess_duration)
            data['duration_hours'] = data[col_name].apply(lambda x: int(x.split(' ')[0][0:-1]))
            data['duration_minutes'] = data[col_name].apply(lambda x: int(x.split(' ')[1][0:-1]))
            self.log.log(self.file_object, "extraction from duration column successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "extraction from duration column started")
            self.log.log(self.file_object, "extraction from duration column started")
            raise e


    def drop_unneccessary_columns(self, data,col_list):
        self.log.log(self.file_object,"dropping unnecessary columns operation started")
        try:
            data.drop(columns=col_list, axis=1, inplace=True)
            self.log.log(self.file_object, "dropping unnecessary columns operation successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "error while dropping unnecessary columns : %s"%e)
            self.log.log(self.file_object, "dropping unnecessary columns operation sunsuccessful")
            raise e