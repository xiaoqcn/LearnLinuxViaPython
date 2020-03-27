import os

import psutil


def main():

    pid = os.getpid()
    ps = psutil.Process(pid)
    print(ps.cwd())
    print(ps.exe())

    print(ps.username())

    print(ps.num_fds())
    # print(ps.io_counters())
    # print(ps.cpu_num())
    with open('.python-version') as f:
        print(f.readline())
        print(ps.open_files())

    print(ps.memory_info())
    print(ps.memory_full_info())
    # print(help(psutil))
    # print(dir(psutil))


if __name__ == "__main__":
    main()
