from tsheets_api.field import Field


class Model(object):
    """Base model class for resources"""

    def __init__(self, name):
        self.name = name

    def add_field(self, field: Field):
        self.__setattr__(field.name, field)