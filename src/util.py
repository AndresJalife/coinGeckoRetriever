from src.cryptoRetrieverException import CryptoRetrieverException
from datetime import date, timedelta, datetime
import click

DATE_FORMAT = "%d-%m-%Y"

def getDatesFromRange(fromDate, toDate):
    """
        Returns the dates between two dates given by params.
        Throws exception if any date given is invalid.
    """
    validateDate(fromDate)
    validateDate(toDate)
    start_date = dateFromString(fromDate)
    end_date = dateFromString(toDate)
    delta = end_date - start_date
    days = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        days.append(day.strftime(DATE_FORMAT))
    return days

def validateDate(date):
    """
        Basic validation for a date. 
        It must contain a "-" character and length = 10.
    """
    if "-" not in date or len(date) != 10:
        raise CryptoRetrieverException("Invalid Date")


def dateFromString(date):
    """ Parses a string date to Date object"""
    return datetime.strptime(date, DATE_FORMAT)