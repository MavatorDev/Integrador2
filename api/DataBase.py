import pymongo
from pymongo import MongoClient

conexion = MongoClient('localhost', 27017)
db = conexion.dataIntegrador