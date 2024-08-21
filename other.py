from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient

def get_api_secret_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    return api_key

def get_db_url():
    load_dotenv()
    db_url = os.getenv("DB_URL")

    return db_url

def connect_to_db():
    load_dotenv()
    db_password = os.getenv("DB_PASSWORD")
    cluster = MongoClient("mongodb+srv://josephoe13:" + db_password + "@cluster0.ulrova0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = cluster["eat-good"]

    return db