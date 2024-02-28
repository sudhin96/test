from pymongo import MongoClient


# This class is used to connect to the database
class ConnectDB:

    def __init__(self):

        self.connection = None
        self.collection = None

    # This function is used to connect to the database
    def connect_db(self, db='', collection=''):

        # Establishing connection the local mongodb server
        connection = MongoClient(host="localhost")

        # Setting the connection to the database
        self.connection = connection["hello_world_db"]

        # Returning the connection
        return self.connection
