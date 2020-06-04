from flask import Flask
from flask_cors import CORS
from flask import request, Response, jsonify, render_template
from flask_apscheduler import APScheduler
from monitor.LogisticRegressionServer import *
from models.temperature import getTemperatures
from models.optimization import getSolutions
from models.optimization import getResults

#from scheduler import Scheduler
logistic = logistic()
logistic.chargeDataInitial()
app = Flask(__name__)
#scheduler = APScheduler()
CORS(app)

@app.route('/api/start/<n>', methods = ['GET'])
def startApp(n):
    print(n)
    logistic.start(n)
    actuallyJob = scheduler.add_job(id = 'Scheduler_app', func = logistic.takeState, trigger='interval', seconds = 10)
    return jsonify({"conf":True})


@app.route('/api/restart/')
def restart():
    actuallyJob = scheduler.add_job(id = 'Scheduler_app', func = logistic.takeState, trigger='interval', seconds = 10)
    print('ready')

@app.route('/api/stop/')
def stop():
    scheduler.remove_job('Scheduler_app')
    pass

@app.route('/api/temperatures/')
def temperatures():
    tem = getTemperatures()
    envio = jsonify(tem)
    print(envio)
    return jsonify(tem)

@app.route('/api/states/')
def states():
    re = getResults()
    return jsonify(re)

@app.route('/api/solutions/')
def solutions():
    sol = getSolutions()
    return jsonify(sol)



if __name__ == '__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(port= 8000)