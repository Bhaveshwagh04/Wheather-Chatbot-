import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
import requests


load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]
        return {
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "pressure": main["pressure"],
            "weather": weather["description"],
            "wind_speed": wind["speed"],
        }
    else:
        return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    data = request.json
    city = data.get("city")
    if city:
        weather_data = get_weather(city)
        if weather_data:
            return jsonify({"status": "success", "data": weather_data})
        else:
            return jsonify({"status": "error", "message": "City not found"})
    else:
        return jsonify({"status": "error", "message": "City not provided"})


if __name__ == "__main__":
    app.run(debug=True)
