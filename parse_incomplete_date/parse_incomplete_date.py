from contextlib import suppress
from datetime import datetime
from datetime import timedelta
from typing import Generator


def _find_possible_dates(
    search_range: range, incomplete_dt: str
) -> Generator[datetime, None, None]:
    for year in search_range:
        with suppress(ValueError):
            dt = datetime.strptime(f"{incomplete_dt} {year}", "%a %b %d %H:%M:%S %Y")
        date_in_future = dt > datetime.now()
        if not date_in_future:
            yield dt


def _weekdays_match(dt: datetime, incomplete_dt: str) -> bool:
    weekday_found_in_string = incomplete_dt[:3].capitalize()
    match = dt.strftime("%a") == weekday_found_in_string
    return True if match else False


def parse_date_from_incomplete_string(incomplete_dt: str) -> datetime:
    search_range = range(datetime.now().year, datetime.now().year - 12, -1)
    candidate_dates = _find_possible_dates(search_range, incomplete_dt)

    while candidate_dates:
        try:
            dt = next(candidate_dates)
        except StopIteration:
            break

        if _weekdays_match(dt, incomplete_dt):
            return dt

    return datetime.now() - timedelta(days=365 * 12)
