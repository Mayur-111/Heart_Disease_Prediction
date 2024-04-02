from flask import Flask,request,render_template
import pickle

app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("frontend_page.html")


@app.route("/test_data")
def test_data():
    
    load_model=pickle.load(open(r"heart_model.pkl","rb"))

    target=["you are Normal","you have heart disease"]

# Age: age of the patient [years]
# RestingBP: resting blood pressure [mm Hg]
# Cholesterol: serum cholesterol [mm/dl]
# MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
# Oldpeak: oldpeak = ST [Numeric value measured in depression]
# HeartDisease: output class [0: Normal,1: heart disease]

    Age = 40
    RestingBP = 140
    Cholesterol = 289
    MaxHR = 172
    Oldpeak = 0.0

    result=load_model.predict([[Age,RestingBP,Cholesterol,MaxHR,Oldpeak]])
    
    return f"{target[result[0]]}"

@app.route("/get_user_data",methods=["POST"])
def get_user_data():

    load_model=pickle.load(open(r"heart_model.pkl","rb"))
    data=request.form

    target=["you are Normal","you have heart disease"]

    Age = eval(data["Age"])
    RestingBP = eval(data["RestingBP"])
    Cholesterol = eval(data["Cholesterol"])
    MaxHR = eval(data["MaxHR"])
    Oldpeak = eval(data["Oldpeak"])

    result=load_model.predict([[Age,RestingBP,Cholesterol,MaxHR,Oldpeak]])
    
    return f"result : {target[result[0]]}"

if __name__=="__main__":
    app.run(debug=True)