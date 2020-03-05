import datetime

def get_seven_days():
    end_date = datetime.date.today()
    offset = datetime.timedelta(days=7)
    start_date = end_date - offset
    return start_date.isoformat(), end_date.isoformat()
