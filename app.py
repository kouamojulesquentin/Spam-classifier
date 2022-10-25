from crypt import methods
from gettext import install
import numpy as np
import json
from flask import Flask, request, render_template
import pickle

from src.predictor import Predictor

app= Flask(__name__)
pred=None
model=pickle.load(open ("models/mail_spam_model.sav", 'rb'))
@app.route("/", methods=[ "GET"])
def default_page():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_spam():
    
    pred =Predictor(model)
    message = request.form['comment']
    result=pred.predict(message)
    return render_template("index.html", prediction_text=' This email is a : {}'.format(result))


if __name__ == "__main__":
    
    app.run(host="", port=5000, debug=True)