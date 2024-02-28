from pymongo import MongoClient


# This class is used to connect to the database
class ConnectDB:

    def __init__(self):

        self.connection = None
        self.collection = None
        self.env = "prod"

    # This function is used to connect to the database
    def connect_db(self, db='', collection=''):

        if self.env == "prod":
            connection = MongoClient(host="localhost",
                                     username="root",
                                     password="=WshareH@2022",
                                     authSource="admin",
                                     authMechanism="SCRAM-SHA-1")
        else:
            connection = MongoClient(host="localhost")

        self.connection = connection["test_db"]
        return self.connection
