import time
import datetime
import os
import sys
import atexit
import signal
from multiprocessing import Pool
from threading import Thread


class HappyScrum:
    def __init__(
        self,
        pid_path,
        pool_size=4,
        busy_wait=90,
        idle_wait=300,
        say_hi_wait=1800,
        is_debug=False,
    ):
        self.pid_path = pid_path
        self.busy_wait = busy_wait
        self.idle_wait = idle_wait
        self.say_hi_wait = say_hi_wait
        self.exception_wait = 300
        self.pool_size = pool_size
        self.is_debug = is_debug

        if self.is_debug:
            self.busy_wait = 5
            self.idle_wait = 5
            self.say_hi_wait = 8

        self.round = 0
        self.is_busy = True
        self.born_utc = datetime.datetime.utcnow()
        self.born = datetime.datetime.now()

        self.daemon_t = Thread(target=self.sen, daemon=True)
        self.dev = lambda x: x
        self.po = lambda x: x

    def sen(self):
        while True:
            time.sleep(self.say_hi_wait)
            if self.round >= 10000:
                print(
                    f"-DOG [{os.getpid()}]:", datetime.datetime.now(), file=sys.stderr
                )
                self.round = 0

    def run_forever(self):
        if os.path.exists(self.pid_path):
            raise ValueError(f"pid_file已存在: {PID_FILE}")

        with open(self.pid_path, mode="w", encoding="utf-8") as f:
            f.write(str(os.getpid()))

        print(
            f"==================\nMAIN [{os.getpid()}]: 启动", file=sys.stderr, flush=True
        )
        self.daemon_t.start()
        while True:
            self.round += 1
            try:
                self.run_round()
            except Exception as ex:
                print(
                    f"MAIN [{os.getpid()}]: HS_ERR: {str(ex)}",
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(self.exception_wait)

    def run_round(self):
        if self.is_busy:
            print(
                f"MAIN [{os.getpid()}]: ROUND: {self.round} BUSY {datetime.datetime.now()}",
                file=sys.stderr,
            )
            time.sleep(self.busy_wait)
        else:
            print(
                f"MAIN [{os.getpid()}]: ROUND: {self.round} IDLE {datetime.datetime.now()}",
                file=sys.stderr,
            )
            time.sleep(self.idle_wait)
        _task_list = self.po()
        if len(_task_list) == 0:
            self.is_busy = False
            return

        self.do_work(_task_list)

    def do_work(self, task_list):
        _feature_list = []
        _pool = Pool(self.pool_size)
        for i in task_list:
            _f = _pool.apply_async(self.dev, args=(i,))
            _feature_list.append(_f)
        _pool.close()
        _pool.join()
        for r in _feature_list:
            print(f"MAIN[{os.getpid()}]: HS_DOD", r.get())
            pass

    def register_po(self, po_tpl):
        self.po = po_tpl

    def register_dev(self, dev_tpl):
        self.dev = dev_tpl

    @classmethod
    def register_dispose(cls, func_dispose):
        atexit.register(func_dispose)
        signal.signal(signal.SIGTERM, func_dispose)
        signal.signal(signal.SIGINT, func_dispose)
        signal.signal(signal.SIGQUIT, func_dispose)
