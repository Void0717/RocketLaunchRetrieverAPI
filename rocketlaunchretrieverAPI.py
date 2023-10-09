#imports
from flask import Flask, jsonify
import time
#globals
app = Flask(__name__)
current_date = time.strftime("%Y-%m-%d")

#{"id": ('#'), "name": "(mission name)", "rocket": "(rocket name)", "date": "(date)"}

#RocketLaunchRetrieverAPI
launches = [
    {"id": 1, "name": "THEOS-2, Triton & others", "rocket": "Vega", "date": "2023-10-09"},
    {"id": 2, "name": "Starlink Group 6-22", "rocket": "Falcon 9 Block 5", "date": "2023-10-09"},
    {"id": 3, "name": "Starlink Group 7-4", "rocket": "Falcon 9 Block 5", "date": "2023-10-09"},
]

@app.route('/launches/upcoming')
def get_upcoming_launches():
    # Return a JSON response with upcoming launches
    upcoming_launches = [launch for launch in launches if launch["date"] >= "2023-10-04"]
    return jsonify(upcoming_launches)

@app.route('/launches/previous')
def get_previous_launches():
    # Return a JSON response with previous launches
    previous_launches = [launch for launch in launches if launch["date"] < "2023-10-04"]
    return jsonify(previous_launches)

if __name__ == '__main__':
    app.run(debug=True)