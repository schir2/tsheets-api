import os
import pytz

TSHEETS_TOKEN = os.environ.get('TSHEETS_TOKEN', None)
TIMEZONE = 'America/New_York'
TZ = pytz.timezone(TIMEZONE)
