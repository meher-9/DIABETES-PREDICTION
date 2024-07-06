from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np

model = pickle.load(open('startup.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   a = request.form["Pregnancies"]
   b = request.form["Glucose"]
   c = request.form["BloodPressure"]
   d = request.form["SkinThickness"]
   e = request.form["Insulin"]
   f = request.form["BMI"]
   g = request.form["DiabetesPedigreeFunction"]
   h = request.form["Age"]

   

   t =  [[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h)]]
   output =model.predict(t)
   
   if(output==1.0):
       output="Oops!!You Have Diabates"
   elif(output==0.0):
       output="Great!!You Dont Have Diabetes"

   return render_template("index.html", y = str((output)))
#    return render_template("front.html")

if __name__ == '__main__' :
    app.run(debug=True)
          





