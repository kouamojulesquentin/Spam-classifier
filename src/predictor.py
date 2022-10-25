class Predictor:
    def __init__(self, model):
        self.models=model
    def predict(self, message):
        pred=self.models.predict([message])[0]
        
        if (pred==0):
            return{"Class":"spam"}
        else:
            return{"Class":"ham"}
