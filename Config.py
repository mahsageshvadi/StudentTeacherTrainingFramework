
class Config:

    def __init__(self):

        self.config_values["stu_model"] = "llama"
        self.config_values["teacher_model"] = "GPT"
        self.config_values["stu_model_endpoint"] = None
        self.config_values["teacher_model_endpoint"] = None
    
    def get_student_model(self):

        return self.config_values["stu_model"]
    
    def get_teacher_model(self):

        return self.config_values["teacher_model"]

    



    
