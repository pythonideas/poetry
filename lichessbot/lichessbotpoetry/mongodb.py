from os import environ as env

from pymongo import MongoClient

import requests
import json
import time


# pprint library is used to make the output look more pretty
# from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >>
# to reflect your own connection string
client = MongoClient(env.get("MONGODB_URI"))
# db = client.admin
# Issue the serverStatus command and print the results
# serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)


class Token:
    def __init__(self):
        self.token = None
        self.username = None
        self.created_at = None

    def set(self, token):
        self.token = token
        headers = {"Authorization": f"Bearer {token}"}
        url = f"https://lichess.org/api/account"

        r = requests.get(url, headers=headers)
        blob = json.loads(r.text)
        self.username = blob["username"]
        print("setting token for", self.username)
        self.created_at = round(time.time() * 1000)

    def json(self):
        return {
            "token": self.token,
            "username": self.username,
            "created_at": self.created_at
        }

    def __repr__(self):
        return f"{self.json()}"


bulk_db = client.bulk

tokens_coll = bulk_db.tokens

token = Token()

token.set(env.get("RUSTBOT_TOKEN"))

filter = {"token": token.token}
set = {"$set": token.json()}
update_result = tokens_coll.update_one(filter, set, upsert=True)
print("matched", update_result.matched_count,
      "updated", update_result.modified_count)

find = tokens_coll.find()

for doc in find:
    print("doc", doc)