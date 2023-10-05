import os
from peewee import SqliteDatabase
from dotenv import load_dotenv
from db.models.statistics import StatisticsCountries
load_dotenv()

database = SqliteDatabase('sqlite_database.db')

def run_migrations():
    try:
        database.connect()
        database.create_tables([StatisticsCountries])
        print("Table creation process executed successfully")
    except Exception as e:
        print(e)


