from DataBase import db
from datetime import date
from datetime import datetime

op = db.optimization
resultModel = db.resultModel


def saveSolution(dic):
    obj = dic['obj']
    cap = dic['cap']
    solution = {"Date": datetime.now(), "bomba1": abs(cap[0]), "bomba2": abs(cap[1]), "bomba3": abs(cap[2]), "bomba4": abs(cap[3]),
                    "Obj1": obj[0], "obj2" : obj[1], "obj3": obj[2], "obj" : obj[3]}

    try:
        op.insert_one(solution)
    except Exception as e:
        print ("Unexpected error:", type(e), e)

def resultsExecuteModel(n):
    result = {"Date": datetime.now(), "state": n}
    try:
        resultModel.insert_one(result)
    except Exception as e:
        print ("Unexpected error:", type(e), e)

def getResults():
    curs= resultModel.find()
    list = []
    for fut in curs:
        list.append({"Date ": fut['Date'] , "state": fut['state']})
    list.reverse()
    list = list[0:10]
    return list

def getSolutions():
    curs= op.find()
    list = []
    for fut in curs:
        list.append({"bomba1": fut["bomba1"], "bomba2": fut["bomba2"], "bomba3": fut["bomba3"], "bomba4": fut["bomba4"]})
    list.reverse()
    list = list[0:6]
    return list