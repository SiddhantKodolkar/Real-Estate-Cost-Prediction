import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import pickle

app=Flask(__name__)
# housing_Mumbai = pd.read_csv("Mumbai_2022.csv")
pipe_Mumbai = pickle.load(open("XGB_Mumbai.pkl","rb"))
# housing_Bangalore = pd.read_csv("Bangalore_2022.csv")
pipe_Bangalore = pickle.load(open("XGB_Bangalore.pkl","rb"))

pipe_Chennai = pickle.load(open("XGB_Chennai.pkl","rb"))

pipe_Delhi = pickle.load(open("XGB_Delhi.pkl","rb"))


@app.route('/') #default route i.e first page to load (home tab)
def index():
    # locations_Mumbai = sorted(housing_Mumbai["location"].unique())
    # locations_Bangalore = sorted(housing_Bangalore["location"].unique())
    # city = request.form.get("city") # gives None first load
    # print(city)
    # if city == "Mumbai":
    #     locations = locations_Mumbai
    # elif city == "Bangalore":
    #     locations = locations_Bangalore
    # elif city == None:
    #     locations = locations_Bangalore 
    # print("location changed to : ", locations)
    return render_template("index.html")



@app.route("/predict",methods=["POST"]) # to get form data and apply ML model for prediction.
def predict():

    city = request.form.get("city")
    location = request.form.get("location")
    bhk = request.form.get("bhk")
    area  = request.form.get("total_sqft")
    print(city, location, bhk, area) # print the form data on terminal
    
    if city=="Mumbai" :
        input = pd.DataFrame([[location,area,bhk]],columns=["location","area","bhk"])        
        prediction = pipe_Mumbai.predict(input)[0]
        return  str(prediction)

    elif city=="Bangalore":
        input = pd.DataFrame([[location,area,bhk]],columns=["location","area","bhk"])
        prediction = pipe_Bangalore.predict(input)[0]
        return  str(prediction)
    
    elif city=="Chennai":
        input = pd.DataFrame([[location,area,bhk]],columns=["location","area","bhk"])
        prediction = pipe_Chennai.predict(input)[0]
        return  str(prediction)
    
    elif city=="Delhi":
        input = pd.DataFrame([[location,area,bhk]],columns=["location","area","bhk"])
        prediction = pipe_Delhi.predict(input)[0]
        return  str(prediction)
    


@app.route("/map") # map tab
def map():
    return render_template("map.html")
    
if __name__ == "__main__":
    app.run(debug=True)