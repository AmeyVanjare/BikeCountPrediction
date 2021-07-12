from flask import Flask, request , jsonify, render_template
import utils

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("./client/app.html")

@app.route('/hello')
def hello():
    return "Hiii"

@app.route('/predict_casual_count', methods=['POST'])
def predict_casual_count():
    season = int(request.form['season'])
    workingday = int(request.form['workingday'])
    temp = float(request.form['temp'])
    atemp = float(request.form['atemp'])
    humidity = float(request.form['humidity'])
    windspeed = float(request.form['windspeed'])
    response = jsonify({
        'estimated_count': utils.get_estimated_count(season,workingday,temp,atemp,humidity,windspeed)
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Bike count prediction server started")
    app.run()