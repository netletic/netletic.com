from datetime import datetime
from datetime import timedelta


def yesterday(asof: datetime) -> datetime:
    return asof - timedelta(days=1)
