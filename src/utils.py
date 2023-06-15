import os
import pickle


class utils:
    def __init__(self,file_object,log):
        self.path="src/saved_model"
        self.log=log
        self.file_object=file_object


    def model_saver(self,model_name,model):
        self.log.log(self.file_object,"model saving operation started")
        try:
           path = os.path.join(self.path, model_name)
           if not os.path.isdir(path):
               os.makedirs(path, exist_ok=True)

           with open(path+"/"+model_name+'.pkl',"wb") as f:
               pickle.dump(model,f)
               f.close()
           self.log.log(self.file_object, "model saving operation successful")
        except Exception as e:
            self.log.log(self.file_object, "error while model saving operation : %s"%e)
            self.log.log(self.file_object, "model saving operation unsuccessful")
            raise e

    def model_loader(self,model_name):
        self.log.log(self.file_object, "model loading operation started")
        try:
           with open(self.path+"/"+model_name+"/"+model_name+'.pkl', "rb") as f:
               self.log.log(self.file_object, "model loading operation successful")
               return pickle.load(f)

        except Exception as e:
            self.log.log(self.file_object, "error in model loading operation : %s"%e)
            self.log.log(self.file_object, "model loading operation unsuccessful")
            raise e