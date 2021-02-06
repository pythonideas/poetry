from os import environ as env

from pymongo import MongoClient

# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >>
# to reflect your own connection string
client = MongoClient(env.get("MONGODB_URI"))
#db = client.admin
# Issue the serverStatus command and print the results
#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)

class Token():
    def __init__(self):
        self.token = None
        self.username = None

bulk_db = client.bulk

tokens_coll = bulk_db.tokens