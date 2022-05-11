from sqlalchemy import Column, Float, Integer
from db.base_class import Base

class StatisticsCountries(Base):
    id = Column(Integer,primary_key=True,index=True)
    total_time = Column(Float)
    mean_time = Column(Float)
    min_time = Column(Float)
    max_time = Column(Float)