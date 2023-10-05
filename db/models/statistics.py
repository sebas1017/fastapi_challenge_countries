from sqlalchemy import Column, Float, Integer
from db.base_class import Base
from ..utils_connection import database

class StatisticsCountries(Base):
    id = Column(Integer,primary_key=True,index=True)
    total_time = Column(Float)
    mean_time = Column(Float)
    min_time = Column(Float)
    max_time = Column(Float)

    class Meta:
        database = database
        table_name = 'users'    