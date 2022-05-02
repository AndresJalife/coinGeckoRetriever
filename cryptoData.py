import click
from psycopg2 import DatabaseError

from src.fileWritter import FileWritter
from src.cryptoRetriever import CryptoRetriever
from src.cryptoRetrieverException import CryptoRetrieverException
from src.util import getDatesFromRange
from src.database import DataBase

cryptoRetriever = CryptoRetriever()
fileWritter = FileWritter() 

@click.command()
@click.argument('identifier') #, help="Coin to fetch"
@click.argument('date', required=False)
@click.option("--from", "fromDate", required=False, help="Start of the dates to store.")
@click.option("--to", "toDate", required=False, help="End of the dates to store.")
@click.option("--store", "store", required=False, help="Boolean to enable storing the data in a database.")

def storeCryptoData(identifier, date, fromDate, toDate, store):
    """ 
        Command line application to store the history of a crypto coin for a specific date (or dates).

        If you only want to fetch one day, pass a date. 

            E: cryptoData.py bitcoin 12-12-2012

        If you want to fetch a range of days, dont pass a date and pass --from and --to options

            E: cryptoData.py bitcoin --from=10-12-2012 --to=12-12-2012

        IDENTIFIER: The coin to fetch.
        DATE: Date to fetch. Only neccesary for one day fetch. Format = "dd-mm-yyyy"
    """
    try:
        db = None
        if (store and store.lower() == "true"):
            db = DataBase()

        if date != None:
            click.echo(f"Retrieving \"{identifier}\" data for date: \"{date}\"")
            _storeData(date, identifier, db)
        else:
            if fromDate != None and toDate != None:
                click.echo(f"Retrieving \"{identifier}\" data from: \"{fromDate}\" to: \"{toDate}\"")
                for actualDate in getDatesFromRange(fromDate, toDate):
                    _storeData(actualDate, identifier, db)
            else:
                raise CryptoRetrieverException("Missing Arguments")

    except CryptoRetrieverException as err:
        click.echo(f"ERROR: {err}")

def _storeData(date, identifier, db):
    """Fetches {identifier} data from date {date} from CoinGecko and stores it in a file."""
    data = cryptoRetriever.getDataFromDateAndId(date, identifier)
    fileName = fileWritter.writeJsonDataForDate(data, date, identifier)
    if db != None:
        db.storeFromCryptoData(data, identifier, date)
    click.echo("Finished retrieving data. File saved: " + fileName)

if __name__ == '__main__':
    storeCryptoData()