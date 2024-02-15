from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    url = f"http://api.weatherapi.com/v1/current.json?key=17a6b3fd8a5645c3976174809232008&q={city}"
    r = requests.get(url)
    w_dic = json.loads(r.text)

    try:
        weather_data = {
            "city": w_dic['location']['name'],
            "state": w_dic['location']['region'],
            "country": w_dic['location']['country'],
            "local_time": w_dic['location']['localtime'],
            "temperature": f"{w_dic['current']['temp_c']} °C"
        }
    except KeyError:
        weather_data = {"error": "Invalid city name"}

    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=True)
