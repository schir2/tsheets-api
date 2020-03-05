import requests
from urllib.parse import urljoin
from tsheets_api import settings

TOKEN = settings.TSHEETS_TOKEN


class RestAdapter:
    """Adapter for communicating with TSheets API"""

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
        more = kwargs.get('more')  # Check if there are additional pages to retrieve
        page = 1
        while more is not False:
            result = self._get(*args, **kwargs)
            more = result.get('more', False)
            page += 1
            kwargs['page'] = page
            yield result

    def get_current_user(self):
        """Retrieves the user object for the currently authenticated user. This is the user that authenticated to
        TSheets during the OAuth2 authentication process. """
        resource = 'current_user'
        return self._get(resource)

    def get_user_id(self, username=None, first_name=None, last_name=None):
        resource = 'users'
        return self._get(resource, usernames=username, first_name=first_name, last_name=last_name)