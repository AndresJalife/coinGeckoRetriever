from sqlalchemy import create_engine
from src.model.coin_aggregated import CoinAggregated
from src.model.coins_history import CoinsHistory
from src.util import dateFromString
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
import json

_DATABASE_URL = "postgresql://andy:postgres@localhost:5432/postgres"

class DataBase:
    """Class for a SQLAlchemy database"""
    def __init__(self):
        self._engine = create_engine(_DATABASE_URL, echo = True)
        self._engine.connect()
        Session = sessionmaker(bind=self._engine)
        self._session = Session()


    def saveMetaData(self, meta):
        """Saves the metadata to the database"""
        meta.create_all(self._engine)

    def close(self):
        """Closes the Database."""
        self._engine.dispose()

    def mergeAndCommit(self, object):
        """Merges the object given by param and commits"""
        self._session.merge(object)
        self._session.commit()

    def storeFromCryptoData(self, data, identifier, date):
        """Stores the coin history and coin aggregation to its tables"""
        ## DISCLAIMER: This could go to another class more adecuated for its purpose, but in this case I'll leave it here ##
        realDate = dateFromString(date)
        usdPrice = usdPrice=data["market_data"]["current_price"]["usd"]
        self._storeCoinHistory(data, identifier, realDate, usdPrice)
        self._storeCoinAggregation(identifier, realDate, usdPrice)

    def _storeCoinHistory(self, data, identifier, date, usdPrice):
        historyEntry = CoinsHistory(coinId=identifier, usdPrice=usdPrice, date=date, data=json.dumps(data))
        self.mergeAndCommit(historyEntry)

    def _storeCoinAggregation(self, identifier, date, usdPrice):
        [maximum, minimum] = self._getMaxAndMinForDate(identifier, date, usdPrice)
        aggregationEntry = CoinAggregated(coinId=identifier, year=date.year, month=date.month, maximum=maximum, minimum=minimum)
        self.mergeAndCommit(aggregationEntry)

    def _getMaxAndMinForDate(self, identifier, date, actualPrice):
        query = self._getRowForDate(identifier, date)
        maximum = actualPrice
        minimum = actualPrice
        if query.count() > 0 :
            query = query.one()
            maximum = query.maximum

            if actualPrice > maximum:
                maximum = actualPrice

            minimum = query.minimum
            if actualPrice < minimum:
                minimum = actualPrice

        return [maximum, minimum]
        
    def _getRowForDate(self, identifier, date):
        return self._session.query(CoinAggregated).filter(CoinAggregated.coinId == identifier, CoinAggregated.year==date.year, CoinAggregated.month==date.month)
