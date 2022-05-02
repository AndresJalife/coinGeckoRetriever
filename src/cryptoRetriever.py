import requests
from src.cryptoRetrieverException import CryptoRetrieverException
from src.util import validateDate

_API_BASE_URL = "https://api.coingecko.com/api/v3"

class CryptoRetriever:
    """Class to fetch data from coingecko."""
    def getDataFromDateAndId(self, date, identifier):
        """Returns the information for a specific date and a specific coin from coinGecko API."""
        return self._callGetRequest(date, identifier)

    def _callGetRequest(self, date, identifier):
        validateDate(date)            
        jsonResponse = requests.get(self._getUrlFromDateAndId(date, identifier)).json()
        self._validateResponse(jsonResponse)
        return jsonResponse

    def _getUrlFromDateAndId(self, date, identifier):
        return _API_BASE_URL + f"/coins/{identifier}/history?date={date}"

    def _validateResponse(self, response):
        if "error" in response:
            raise CryptoRetrieverException(response["error"])
