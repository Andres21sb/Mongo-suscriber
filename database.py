'''
autor: Andrés Méndez Solano
fecha: 2020-05-08
    
        Este script se encarga de hacer consultas a la base de datos de MongoDB
'''
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv() 


# Cliente
client = MongoClient(os.getenv('MONGODB_URI'))

# Base de datos
db = client[os.getenv('MONGODB_DB')]

# libray-IoT coleccion
libray_IoT = db[os.getenv('MONGODB_COLLECTION')]

print('Conexión exitosa a la base de datos')

# Insertar datos en la base de datos
def insert_data(data):
    libray_IoT.insert_one(data)
    print('Datos insertados en la base de datos')