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

# Datos a insertar
data_to_insert = [
    {"publisher_name": "termostato_v1", "attribute_name": "temperatura", "attribute_value": 29.11, "timestamp": "02:01:58 2024-05-05"},
    {"publisher_name": "electricidad_v1", "attribute_name": "corriente", "attribute_value": 4.73, "timestamp": "02:01:58 2024-05-05"},
    {"publisher_name": "termostato_v1", "attribute_name": "temperatura", "attribute_value": 17.37, "timestamp": "02:02:03 2024-05-05"},
    {"publisher_name": "electricidad_v1", "attribute_name": "corriente", "attribute_value": 9.83, "timestamp": "02:02:03 2024-05-05"}
]

# Eliminar todos los documentos de la colección
try:
    libray_IoT.delete_many({})
    print('Documentos eliminados')
except:
    print('Error al eliminar los documentos')
