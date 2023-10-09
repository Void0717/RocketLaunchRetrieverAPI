# Imports
from flask import Flask, jsonify
from flask_cors import CORS
import time
import requests
# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Global variables
current_date = time.strftime("%Y-%m-%d")
cache_file = 'launch_data_cache.json'
cache_duration = 3600  # Cache duration in seconds (1 hour)


# Routes
@app.route('/launches/upcoming')
def get_upcoming_launches():
    url = 'https://ll.thespacedevs.com/2.2.0/launch/upcoming'
    response = requests.get(url)
    if response.status_code == 200:
        launches = response.json()
    return jsonify(launches)

@app.route('/launches/previous')
def get_previous_launches():
    url = 'https://ll.thespacedevs.com/2.2.0/launch/previous'
    response = requests.get(url)
    if response.status_code == 200:
        launches = response.json()
    return jsonify(launches)

if __name__ == '__main__':
    app.run(debug=True)
