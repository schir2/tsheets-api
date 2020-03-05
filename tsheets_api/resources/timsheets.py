from functools import wraps

from tsheets_api.models.timesheet import Timesheet
from tsheets_api.resource import Resource
from tsheets_api import field

import datetime

from tsheets_api.helpers import get_seven_days

start, end = get_seven_days()


def get_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(kwargs)

    return wrapper


class Timesheets(Resource):
    model = Timesheet
    resource = 'timesheet'

    ids = field.List(name='ids', required=True)
    start_date = field.DateTime(name='start_date', required=True)
    end_date = field.DateTime(name='start_date', required=True)
    jobcode_ids = field.List(name='jobcode_ids')
    payroll_ids = field.List(name='payroll_ids')
    user_ids = field.List(name='user_ids')
    group_ids = field.List(name='group_ids')
    on_the_clock = field.CustomBool(name='on_the_clock', default=False)
    jobcode_type = field.Str(name='jobcode_type')
    modified_before = field.DateTime(name='modified_before', required=True)
    supplemental_data = field.Bool(name='supplemental_data')
    per_page = field.Int(name='per_page', default=50, min_value=1, max_value=50)
    page = field.Int(name='page', default=1, min_value=1)

    @classmethod
    @get_decorator
    def get(cls, ids=ids.default, start_date=start_date.default, end_date=end_date.default,
            jobcode_ids=jobcode_ids.default, payroll_ids=payroll_ids.default, user_ids=user_ids.default,
            group_ids=group_ids.default, on_the_clock=on_the_clock.default, jobcode_type=jobcode_type.default,
            modified_before=modified_before.default, supplemental_data=supplemental_data.default,
            per_page=per_page.default, page=page.default):
        if not (ids or start_date or end_date or modified_before):
            raise Exception(
                'None of the required arguments were supplied: ids, start_date, end_date or modified_before')
        print(cls.get.__code__.co_consts)


Timesheets.get(start_date=5)
