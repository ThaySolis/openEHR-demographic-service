import datetime
import iso8601
import dateutil.parser

def parse_datetime(value : str) -> datetime.datetime:
    return dateutil.parser.parse(value)

def time_now() -> datetime.datetime:
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

def test_time(time : str) -> None:
    try:
        iso8601.parse_date(time)
    except Exception as e:
        print("Not a valid ISO 8601 format of data/time.")
        raise e

def is_after(desired_time : str, record_time : str) -> bool:
    test_time(desired_time)
    test_time(record_time)
    desired_time = dateutil.parser.parse(desired_time)
    record_time = dateutil.parser.parse(record_time)
    if desired_time > record_time:
        #The desired record exists in the given time
        return True
    else:
        #The desired record does not exist in the given time
        return False

def is_before(x : str, y : str) -> bool:
    return is_after(y, x)

