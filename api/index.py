from flask import Flask
from flask_cors import CORS
from flask import request, Response, jsonify, render_template
from monitor.LogisticRegressionServer import *

logistic = logistic()

app = Flask(__name__)
CORS(app)

@app.route('/api/start')
def startApp():
    logistic.start()


app.run(host= "localhost", port= 8000)