# Imports
from flask import Flask, jsonify
from flask_cors import CORS
import time
import requests
import json
from datetime import datetime, timedelta
import os
# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Global variables
current_date = time.strftime("%Y-%m-%d")
cache_file = 'launch_data_cache.json'
cache_duration = 3600  # Cache duration in seconds (1 hour)

# Function to fetch and cache data if needed
def fetch_launch_data():
    # Check if cached data exists and is still valid
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            cached_data = json.load(f)
        last_fetch_time = datetime.fromisoformat(cached_data.get('last_fetch_time', '1970-01-01T00:00:00'))
        current_time = datetime.now()
        if (current_time - last_fetch_time).total_seconds() < cache_duration:
            return cached_data['launches']

    # Fetch data from the API if not in cache or cache is stale
    url = 'https://ll.thespacedevs.com/2.2.0/launch'
    response = requests.get(url)
    if response.status_code == 200:
        launches = response.json()
        
        # Update the last fetch time in the cache
        current_time = datetime.now().isoformat()
        cached_data = {'launches': launches, 'last_fetch_time': current_time}
        with open(cache_file, 'w') as f:
            json.dump(cached_data, f)

        return launches
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code}")

# Routes
@app.route('/launches/upcoming')
def get_upcoming_launches():
    # Fetch and return upcoming launches
    launches = fetch_launch_data()
    upcoming_launches = [launch for launch in launches if launch["date"] >= current_date]
    return jsonify(upcoming_launches)

@app.route('/launches/previous')
def get_previous_launches():
    # Fetch and return previous launches
    launches = fetch_launch_data()
    previous_launches = [launch for launch in launches if launch["date"] < current_date]
    return jsonify(previous_launches)

if __name__ == '__main__':
    app.run(debug=True)
