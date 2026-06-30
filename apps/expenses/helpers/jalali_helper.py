from jdatetime import datetime as jdatetime


def to_jalali(date):
    """تبدیل تاریخ میلادی به شمسی"""
    if not date:
        return ''
    jalali = jdatetime.fromgregorian(datetime=date)
    return jalali.strftime('%Y/%m/%d')


def from_jalali(jalali_str):
    """تبدیل تاریخ شمسی (رشته) به شیء datetime میلادی"""
    if not jalali_str or not jalali_str.strip():
        return None
    try:
        jalali = jdatetime.strptime(jalali_str.strip(), '%Y/%m/%d')
        return jalali.togregorian()
    except (ValueError, TypeError):
        return None