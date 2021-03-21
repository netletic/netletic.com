from datetime import datetime
from datetime import timedelta


def yesterday() -> datetime:
    return datetime.today() - timedelta(days=1)
