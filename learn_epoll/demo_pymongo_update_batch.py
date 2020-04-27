import datetime

from pymongo import MongoClient
from pymongo.results import BulkWriteResult
from pymongo.operations import UpdateOne

_client = MongoClient("mongodb://127.0.0.1:27017", connect=False)


def main():
    print(_client)
    print(_client.list_database_names())
    for _db in _client.list_databases():
        print(_db, _client[_db.get("name")].list_collection_names())
        # print()
    # print(_client["test"].list_collection_names())
    _cursor = _client["test"]["test"].find()
    print(list(_cursor))
    return
    _list = []
    for p in _cursor:
        _list.append(
            UpdateOne(
                {"_id": p.get("_id")}, {"$set": {"tagname": p.get("tagname") + "--"}}
            )
        )

    _list.append(
        UpdateOne(
            {"_id": 3},
            {"$set": {"created_at": datetime.datetime.now(), "tagname": "小"}},
            upsert=True,
        )
    )

    _r: BulkWriteResult = _client["test"]["test"].bulk_write(_list)
    print(_r.acknowledged, _r.matched_count)
    print(_r.inserted_count, _r.modified_count, _r.deleted_count)


if __name__ == "__main__":
    main()
