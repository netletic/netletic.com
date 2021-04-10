from collections import Counter
from pathlib import Path
from pprint import pprint
from typing import List
from typing import Tuple
from urllib.request import urlretrieve


tmp = Path("/tmp")
t1_url = (
    "https://raw.githubusercontent.com/netletic/netletic.com/main/find_the_loop/t1.txt"
)
t2_url = (
    "https://raw.githubusercontent.com/netletic/netletic.com/main/find_the_loop/t2.txt"
)
t1_file = tmp / "t1.txt"
t2_file = tmp / "t2.txt"

if not t1_file.exists():
    urlretrieve(t1_url, t1_file)
if not t2_file.exists():
    urlretrieve(t2_url, t2_file)


def get_rx_bytes(file: Path) -> Counter:
    rx = {}
    with open(file) as fp:
        for line in fp.readlines():
            if "Chassis/Slot/Port" in line:
                _, port, _ = line.split()
                continue
            elif "Bytes Received" in line:
                _, bytes_rx, *_ = line.split(":")
                bytes_rx = bytes_rx.replace(", Unicast Frames ", "").lstrip()
                rx[port] = int(bytes_rx)
    return Counter(rx)


def delta(t1: Counter, t2: Counter) -> List[Tuple[str, int]]:
    return (t2 - t1).most_common(5)


def main() -> int:
    t1 = get_rx_bytes(t1_file)
    t2 = get_rx_bytes(t2_file)
    pprint(delta(t1, t2))
    return 0


if __name__ == "__main__":
    exit(main())
