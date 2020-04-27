import os
import sys
import traceback
import datetime

from happy import HappyScrum
from pymongo import MongoClient
from bson.json_util import dumps


def po_work() -> list:
    _client = MongoClient("mongodb://127.0.0.1:27017")
    _cursor = _client["test"]["test"].find()
    _list = list(_cursor)

    print(f"==== PO  [{os.getpid()}] : 任务数：", len(_list))
    print(f"--PO [{os.getpid()}]: 任务数", len(_list), file=sys.stderr, flush=True)
    return _list
    # return [i for i in range(6)]


def dev_work(task_dict):
    try:
        # 或者 2. create at sub process
        _client = MongoClient("mongodb://127.0.0.1:27017")
        _coll = _client["test"]["test"]
        _coll.update_one(
            {"_id": task_dict.get("_id")},
            {"$set": {"updated_at": datetime.datetime.now()}},
            upsert=True,
        )
        # _cursor = _client["test"]["test"].find()
        print(f"DEV [{os.getpid()}]", dumps(task_dict, ensure_ascii=False))
        return f"DEV {task_dict.get('_id')}"
    except Exception as ex:
        print(f"DEV [{os.getpid()}]ERROR", ex, file=sys.stderr)
        traceback.print_exc()


PID_FILE = os.path.join(os.path.expanduser("~"), "demo.pid")


def global_sig(sig_flag=None, sig_frame=None):
    if sig_flag:
        print(
            f"MAIN [{os.getpid()}]: 信号",
            sig_flag,
            sig_frame,
            file=sys.stderr,
            flush=True,
        )
    if os.path.exists(PID_FILE):
        print(
            f"MAIN [{os.getpid()}]: 停止",
            f"删除pid_file: {PID_FILE}",
            file=sys.stderr,
            flush=True,
        )
        os.remove(PID_FILE)
    sys.exit(0)


if __name__ == "__main__":
    _hf = HappyScrum(PID_FILE, is_debug=True)
    _hf.register_po(po_work)
    _hf.register_dev(dev_work)
    _hf.register_dispose(global_sig)
    _hf.run_forever()
