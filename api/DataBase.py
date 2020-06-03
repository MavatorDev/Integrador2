import pymongo
from pymongo import MongoClient

#conexion = MongoClient('localhost', 27017)
#db = conexion.dataIntegrador
client = pymongo.MongoClient("mongodb+srv://dbuser:integrador@cluster0-g9e4u.mongodb.net/dataIntegrador?retryWrites=true&w=majority")
db = client.dataIntegrador