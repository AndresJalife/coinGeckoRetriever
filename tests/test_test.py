from src.cryptoRetriever import CryptoRetriever, CryptoRetrieverException

retriever = CryptoRetriever()

def test_getDataFromDateAndIdShouldReturnDataForBitcoin():
    """Verifies that the application y getting valid information"""
    data = retriever.getDataFromDateAndId("12-12-2020", "bitcoin")
    assert "error" not in data
    assert data["id"] == "bitcoin"

def test_getDataFromDateAndIdShouldThrowErrorForInvalidDate():
    """Verifies that if an invalid date is passed, it raises an exception"""
    try:
        retriever.getDataFromDateAndId("12-122020", "bitcoin")
    except CryptoRetrieverException as err:
        assert str(err) == "Invalid Date"
