from collections import Counter
from pprint import pprint


def get_rx_bytes(filename: str) -> Counter:
    rx = {}
    with open(filename) as fp:
        for line in fp.readlines():
            if "Chassis/Slot/Port" in line:
                _, port, _ = line.split()
                continue
            if "Bytes Received" in line:
                _, bytes_rx, *_ = line.split(":")
                bytes_rx = bytes_rx.replace(", Unicast Frames ", "")
                bytes_rx = bytes_rx.lstrip()
                rx[port] = int(bytes_rx)
    return Counter(rx)


def delta(t1: Counter, t2: Counter) -> list[tuple[str, int]]:
    return (t2 - t1).most_common(5)


def main():
    t1 = get_rx_bytes("t1.txt")
    t2 = get_rx_bytes("t2.txt")
    pprint(delta(t1, t2))


if __name__ == "__main__":
    exit(main())
