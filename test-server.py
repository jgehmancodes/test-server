

from flask import Flask, request, jsonify

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to the test server. Please choose from the following menu:</h1><br><h2><a href="/api/v1/resources/tests/all">Test resources</a>'

tests = [
        {'id':0,
        'Test type': 'API',
        'Test automation': 'Yes',
        'Test performance': 'Yes'},
        {'id':1,
        'Test type': 'Performance',
        'Test automation': 'Yes',                                                                                                                                               'Test performance': 'Yes'}
]

@app.route('/api/v1/resources/tests/all', methods=['GET'])
def api_all():
    return jsonify(tests)

app.run()

