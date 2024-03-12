from datetime import datetime, timedelta
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, format)
    dt2 = datetime.strptime(t2, format)
    difference = abs(int((dt2 - dt1).total_seconds()))
    return difference

