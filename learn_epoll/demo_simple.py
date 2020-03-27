import os
import select


def main():
    efo = select.epoll()
    with open("a.txt", mode='r') as f:
        fno = f.fileno()

        efo.register(fno, select.EPOLLIN)
        while True:
            try:
                events = efo.poll(10)
                print(f"there is {len(events)}")
                for fd, evt in events:
                    print(fd)
                pass
            except KeyboardInterrupt as kbi:
                print(str(kbi))
                break

        efo.unregister(fno)
        efo.close()


if __name__ == "__main__":
    main()
