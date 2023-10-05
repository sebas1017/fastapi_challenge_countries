import os
from peewee import SqliteDatabase
from dotenv import load_dotenv
load_dotenv()

database = SqliteDatabase('sqlite_database.db')


def run_migrations(array_objects_db):
    try:
        database.connect()
        database.create_tables(array_objects_db)
        print("Table creation process executed successfully")
    except Exception as e:
        print(e)
