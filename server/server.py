from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route("/")
def hello():
    return {'message' : "Hi"}

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations' :util.get_all_locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price", methods = ['POST'])
def predict_home_price():
    sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.predict_price(location = location, sqft= sqft, bath=bath, bhk=bhk)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Server for Price Prediction")
    app.run()