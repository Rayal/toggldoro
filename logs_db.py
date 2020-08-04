from os import getenv
from uuid import uuid4

from pymongo import MongoClient


class LogsDbInterface:
    def __init__(self, collection='logs'):
        uri = getenv('MONGODB_URI')
        self.client = MongoClient(uri, retryWrites=False)
        self.db = self.client.get_default_database()
        self.logs = self.db[collection]

    def add_log(self, uid: uuid4, title: str, start_time: float, duration: float) -> None:
        log = {
            'uuid': uid,
            'title': title,
            'start': start_time,
            'duration': duration
        }
        self.logs.insert_one(log)

    def get_log(self, uid: uuid4) -> tuple:
        query = {
            'uuid': uid
        }
        return self.logs.find_one(query)

    def get_logs(self, look_from: float, look_to: float) -> list:
        query = {
            'start': {
                '$gte': look_from,
                '$lte': look_to
            }
        }
        return self.logs.find(query)

    def purge(self) -> None:
        self.db.drop_collection(self.logs)

    def terminate(self) -> None:
        self.client.close()
