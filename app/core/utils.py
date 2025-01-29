from datetime import datetime


def get_month_range(month: str):
    start_date = datetime.strptime(month, "%Y-%m")
    end_date = datetime(start_date.year + (start_date.month // 12), ((start_date.month % 12) + 1), 1)
    return start_date, end_date
