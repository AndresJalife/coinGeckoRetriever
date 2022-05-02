import json

_BASE_RESPONSE_DIR = "/home/andresjalife/Desktop/response/"

class FileWritter:
    """
        Class that writes to a file.
    """
    def writeJsonDataForDate(self, json, date, id):
        """
            Method to write a JSON to a file. 

            Names the file as {id}_{date}.json
        """
        name = f"{id}_{date}.json"
        file = self._createFile(name)
        self._writeJson(json, file)
        file.close()
        return name

    def _createFile(self, name):
        return open(_BASE_RESPONSE_DIR + name, "w")
    
    def _writeJson(self, data, file):
        json.dump(data, file)