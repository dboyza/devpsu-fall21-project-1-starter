from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json

# Use this file as the flask app source if selected
app = Flask(__name__)

# Enable CORS
CORS(app)

# Handle Routing for the app
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)

@app.route('/parks')
def read_users():

    # Read the parks.json file and store it as parks
    with open('parks.json', 'r') as f:
        parks = json.load(f)

    return render_template('parks.html', parks=parks)


# Add a route to a return a json response like an API
#####################################################
@app.route('/api')
def read_collegs():
    c1 = ['Name: Penn State University', 'Location: State College, PA', 'Students: 46,800']
    c2 = ['Name: Universtiy of Pittsburgh', 'Location: Piitsburgh, PA', 'Students: 19,197']
    c3 = ['Name: Carnegie Mellon University', 'Location: Piitsburgh, PA', 'Students: 7,073']
    clist = [c1, c2, c3]
    return jsonify("CollegeList", clist)

# If this file is executed, run the app
if __name__ == "__main__":
    app.run()
