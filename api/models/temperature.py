from DataBase import db
from datetime import date
from datetime import datetime

tem = db.temperature


def saveGeneratedTemperature(dataframe):
    temp = {"Date": datetime.now(), "muestra": dataframe}

    try:
        tem.insert_one(temp)
    except Exception as e:
        print ("Unexpected error:", type(e), e)
