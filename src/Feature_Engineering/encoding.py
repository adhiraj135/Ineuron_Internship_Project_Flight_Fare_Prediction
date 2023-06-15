from src.logger import log

class encoder:
    def __init__(self):
        self.log=log()
        self.file_object=open('src/logs/training_logs/encoding_log.txt','a+')
        self.prediction_file_object = open('src/logs/prediction_logs/encoding_log.txt', 'a+')

    def one_hot(self,data,column):
        self.log.log(self.file_object,"One Hot encoding operation started")
        try:
            for city in data[column].unique():
                data[column+"_"+city]=data[column].apply(lambda x:1 if x==city else 0)
            self.log.log(self.file_object, "One Hot encoding successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "Error while One Hot encoding operation : %s"%e)
            self.log.log(self.file_object, "One Hot encoding operation unsuccessful")
            raise e

    def mean_encoding(self,data,column):
        self.log.log(self.file_object,"mean encoding operation started")
        try:
            for col in column:
                values=data.groupby([col])['Price'].mean().sort_values().index
                dictionary={key:value for value,key in enumerate(values)}
                data[col]=data[col].map(dictionary)
            self.log.log(self.file_object, "mean encoding operation successful")
            return data
        except Exception as e:
            self.log.log(self.file_object, "Error while mean encoding operation : %s"%e)
            self.log.log(self.file_object, "mean encoding operation unsuccessful")
            raise e

    def dict_value(self,train_data,pred_data,column):
        self.log.log(self.file_object,"dict value operation started")
        try:
           values=train_data.groupby([column])['Price'].mean().sort_values().index
           dictionary={key:value for value,key in enumerate(values)}
           pred_data.replace(list(pred_data[column])[0],dictionary[list(pred_data[column])[0]],inplace=True)
           self.log.log(self.file_object, "Dict value operation successful")
           return pred_data

        except Exception as e:
            self.log.log(self.file_object, "error in dict value operation : %s"%e)
            self.log.log(self.file_object, "dict value operation unsuccessful")
            raise e


    def source_column_addition(self,train_data,pred_data):
        self.log.log(self.file_object, "source column addition operation started")
        try:
           column=train_data.drop(columns='Price',axis=1)
           for col in list(column.columns):
               if col not in list(pred_data.columns):
                   pred_data[col]=0
           self.log.log(self.file_object, "source column addition operation successful")
           return pred_data

        except Exception as e:
            self.log.log(self.file_object, "erro in source column addition operation : %s"%e)
            self.log.log(self.file_object, "source column addition operation unsuccessful")
            raise



    def manual_encoding(self,data,column):
        self.log.log(self.file_object, "manual encoding operation started")
        try:
           stops={'non-stop':0, '2 stops':2, '1 stop':1, '3 stops':3, '4 stops':4}
           data[column]=data[column].map(stops)
           self.log.log(self.file_object, "manual encoding operation successful")
           return data
        except Exception as e:
            self.log.log(self.file_object, "error in manual encoding operation : %s"%e)
            self.log.log(self.file_object, "manual encoding operation unsuccessful")
            raise e


