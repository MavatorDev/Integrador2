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

