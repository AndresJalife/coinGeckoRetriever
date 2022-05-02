from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

class CoinsHistory(Base):
    """Model for the history of coins retreiving data"""
    __tablename__ = 'coins_history'

    coinId = Column('coin_id', String, primary_key = True, nullable=False) 
    usdPrice = Column('usd_price', Integer, nullable=False)
    date =Column('date', Date, primary_key = True, nullable=False)
    data = Column('data', String)