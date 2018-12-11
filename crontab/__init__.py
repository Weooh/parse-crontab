# coding: utf-8
from ._crontab import CronTab

__all__ = ['CronTab', 'is_in_crontab_range']


def _is_in_crontab_range(start_ct, end_ct):
    if not end_ct.next():
        return False

    if not start_ct.next() and end_ct.next():
        return True

    if start_ct.next() < end_ct.next():
        return False

    return True


def is_in_crontab_range(start, end, tz=None):
    """Check now is in crontab range fron start to end
        Args:
            start (T[str, CronTab]): cron job string or CronTab class
            end (T[str, CronTab]): cron job string or CronTab class
        Return:
            Bool
    """
    start_ct = CronTab(start, tz) if isinstance(start, str) else start
    end_ct = CronTab(end, tz) if isinstance(end, str) else end
    return _is_in_crontab_range(start_ct, end_ct)

