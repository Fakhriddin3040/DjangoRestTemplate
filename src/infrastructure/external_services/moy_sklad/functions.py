import datetime


def datetime_to_moy_sklad_format(dt: datetime.datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")
