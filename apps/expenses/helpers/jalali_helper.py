from jdatetime import datetime as jdatetime


def to_jalali(date):
    """تبدیل تاریخ میلادی به شمسی"""
    if not date:
        return ''
    jalali = jdatetime.fromgregorian(datetime=date)
    return jalali.strftime('%Y/%m/%d')