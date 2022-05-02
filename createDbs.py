from sqlalchemy import MetaData, Table, Column, Integer, String, Date
from src.database import DataBase
import click

@click.command()
def createDatabases():
    db = DataBase()
    meta = MetaData()

    Table(
        'coins_history', meta, 
        Column('coin_id', String, primary_key = True, nullable=False), 
        Column('usd_price', Integer, nullable=False), 
        Column('date', Date, primary_key = True, nullable=False),
        Column('data', String)
    )
    db.saveMetaData(meta)
    db.close()

createDatabases()