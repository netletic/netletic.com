import re
from collections import Counter
from pathlib import Path
from pprint import pprint
from typing import List
from typing import Optional
from typing import Tuple
from urllib.request import urlretrieve


tmp = Path("/tmp")
github = "https://raw.githubusercontent.com"
t1_url = f"{github}/netletic/netletic.com/main/find_the_loop/t1.txt"
t2_url = f"{github}/netletic/netletic.com/main/find_the_loop/t2.txt"
t1_file = tmp / "t1.txt"
t2_file = tmp / "t2.txt"

if not t1_file.exists():
    urlretrieve(t1_url, t1_file)
if not t2_file.exists():
    urlretrieve(t2_url, t2_file)


def get_rx_bytes(file: Path) -> Counter:
    with open(file) as fp:
        pattern = re.compile(
            r"Chassis/Slot/Port\s(\d+/\d+/\d+).*?Bytes Received  :\s*(\d{1,})",
            re.DOTALL,
        )
        matches = re.findall(pattern, fp.read())
        rx = {port: int(bytes_rx) for port, bytes_rx in matches}
    return Counter(rx)


def delta(t1: Counter, t2: Counter, limit: Optional[int] = 5) -> List[Tuple[str, int]]:
    return (t2 - t1).most_common(limit)


def main() -> int:
    t1 = get_rx_bytes(t1_file)
    t2 = get_rx_bytes(t2_file)
    pprint(delta(t1, t2))
    return 0


if __name__ == "__main__":
    exit(main())
