from tsheets_api.helpers import to_int_list
from tsheets_api.helpers import get_seven_days

class Timesheet(object):

    def get_by_id(self, ids):
        """Retrieves a list of all timesheets associated with your company, with filters to narrow down the results."""
        ids = to_int_list(ids)
        resource = 'timesheets'
        return self._get_pages(resource, ids=ids)


    def get_by_date(self, on_the_clock=None, start_date=None, end_date=None, last_modified=None,
                              user_id=None):
        """
        Retrieves a list of all timesheets associated with your company, with filters to narrow down the results.

        Defaults to on the last seven days of on the clock timesheets.

        :param user_id:
        :param on_the_clock:
        :param start_date:
        :param end_date:
        :param last_modified:
        :return:
        """
        if not (start_date or end_date or last_modified):
            start_date, end_date = get_seven_days()
            on_the_clock = True

        """Retrieves a list of all timesheets associated with your company, with filters to narrow down the results."""
        resource = 'timesheets'
        return self._get_pages(resource, start_date=start_date, end_date=end_date, on_the_clock=on_the_clock)