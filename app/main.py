from flask import Flask, request
import requests

app = Flask(__name__)

# define 7timer API request URI tokens
APIROOT = "http://www.7timer.info/bin/api.pl?"
PRODUCT = "astro"
OUTPUT = "json"

# sample 7timer API request
# http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=xml

# Test Coordinates
# Longitude = 113.17
# Latitude = 23.09

# Debugging route
@app.route("/")
def debug():
    return "<p>Hello, World!</p>"

# Health-check route for other services to monitor
@app.route("/health")
def health_check():
    return {"status": "ok"}

# Main API endpoint
# e.g. /weather?longitude=113.17&latitude=23.09
@app.route("/weather")
def get_weekly_forecast():

    # collect querystring parameters that we care about
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    print(f"Request params: Latitude - {latitude} | Longitude - {longitude}")

    # build URL to proxy to real weather API
    endpoint = f"{APIROOT}lon={longitude}&lat={latitude}&product={PRODUCT}&output={OUTPUT}"

    # get weather forecast
    return requests.get(endpoint).json()

# start webserver
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')