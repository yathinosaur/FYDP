from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

# Sample get method
@app.route('/angle', methods=['GET'])
def angle(): 
    torque = 3
    angle = torque * 2
    return jsonify({'angle': angle})


if __name__ == '__main__':
    app.run(debug=True)