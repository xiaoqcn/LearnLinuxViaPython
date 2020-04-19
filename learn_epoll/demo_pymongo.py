from pymongo import MongoClient
from multiprocessing import Pool
import os

# create client before fork will raise warning
"""
UserWarning: MongoClient opened before fork. Create MongoClient only after forking. See PyMongo's documentation for details: http://api.mongodb.org/python/current/faq.html#is-pymongo-fork-safe
  "MongoClient opened before fork. Create MongoClient only "
"""
# 1. 设置connect = False
# 或者 2. create at sub process
_client = MongoClient("mongodb://127.0.0.1:27017", connect=False)


def main():
    print(_client)
    print(_client.list_database_names())
    for _db in _client.list_databases():
        print(_db, _client[_db.get("name")].list_collection_names())
        # print()
    # print(_client["test"].list_collection_names())
    _cursor = _client["test"]["test"].find()
    for p in _cursor:
        print(p)


def worker(name):
    # print("worker", name, os.getpid())
    doc = _client["test"]["test"].find_one({"_id": int(name) + 1})
    print("worker", name, os.getpid(), doc)


def master():
    pool = Pool(4)
    for i in range(2):
        pool.apply_async(worker, args=(str(i),))
    pool.close()
    pool.join()
    print("done")


if __name__ == "__main__":
    master()
    # main()
