from multiprocessing import Pool, Value
import os
import time
import sys
from ctypes import c_char_p


def get_content():
    with open("../2.txt", mode="r", encoding="utf-8") as f:
        return f.read()


vvv = get_content()


def worker(task_n):
    con = vvv
    _i, _si, _ref_count = id(sys.intern(con)), id(con), sys.getrefcount(con)
    _pid = os.getpid()
    print(_pid, task_n, _i, _si, _ref_count)
    return _pid


def main():
    # _content = get_content()
    # _shared_value = Value("ctypes.c_char_p", _content)
    # print(_content)
    _pool = Pool(2)

    _fl = []
    for i in range(20):
        _f = _pool.apply_async(worker, args=(i,))
        _fl.append(_f)
    _pool.close()
    _pool.join()
    for i in _fl:
        rr = i.get()
        # print(rr)
    time.sleep(3000)


if __name__ == "__main__":
    main()
