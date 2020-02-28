import os
import requests
from urllib.parse import urljoin

from .helpers import TZ
from .helpers import to_bool
from .helpers import to_date
from .helpers import to_int_list
from .helpers import get_seven_days

from .settings import TSHEETS_TOKEN

TOKEN = os.environ.get(TSHEETS_TOKEN, None)


class RestAdapter:
    """Adapter for communicating with Zubie API"""

    def __init__(self, token=TOKEN):
        self.base_url = 'https://rest.tsheets.com/api/v1/'
        self._token = token
        self._headers = {'Authorization': f'Bearer {self._token}'}
        self._params = {}

    def _get(self, resource: str, **kwargs) -> dict:
        """Base get method used for all api calls"""
        params = self._params.copy()  # Sets default parameters
        params.update(kwargs)  # Adds provided keyword arguments to the call
        print(params)
        url = urljoin(self.base_url, resource)
        return requests.get(url=url, headers=self._headers, params=params).json()

    def _get_pages(self, *args, **kwargs) -> iter:
        """Get function for getting pagination data"""
        cursor = kwargs.get('cursor')  # Cursor should be set to none initially
        while cursor is not False:
            result = self._get(*args, **kwargs)
            cursor = result.get('cursor', False)
            yield result

    def get_current_user(self):
        """Retrieves the user object for the currently authenticated user. This is the user that authenticated to
        TSheets during the OAuth2 authentication process. """
        resource = 'current_user'
        return self._get(resource)

    def get_timesheet_by_id(self, ids):
        """Retrieves a list of all timesheets associated with your company, with filters to narrow down the results."""
        ids = to_int_list(ids)
        resource = 'timesheets'
        return self._get_pages(resource, ids=ids)

    def get_timesheet_by_date(self, on_the_clock=None, start_date=None, end_date=None, last_modified=None):
        """
        Retrieves a list of all timesheets associated with your company, with filters to narrow down the results.

        Defaults to on the last seven days of on the clock timesheets.

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


if __name__ == '__main__':
    ra = RestAdapter()
    current_user = ra.get_current_user()
    timesheet_by_id = ra.get_timesheet_by_id('266713178,266713838')
    timesheet_by_date = ra.get_timesheet_by_date()
