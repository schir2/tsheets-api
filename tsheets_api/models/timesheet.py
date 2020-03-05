from tsheets_api import field
from tsheets_api import model


class Timesheet(model.Model):
    id = field.Int(name='id', required=True)
    user_id = field.Int(name='user_id')