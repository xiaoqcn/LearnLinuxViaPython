import select
import sys
import os


def main():
    with open("../init.sh") as f:
        l = f.readline()
        print(
            f.fileno(), sys.stdin.fileno(), sys.stdout.fileno(), sys.stderr.fileno(),
        )
        dd = os.fstat(f.fileno())
        print(type(dd), dd)

        print(f.tell(), os.lseek(f.fileno(), 0, os.SEEK_CUR))


if __name__ == "__main__":
    main()
