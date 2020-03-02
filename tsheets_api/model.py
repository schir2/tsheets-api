class Field(object):
    """Base field object for generating fields for models"""

    def __init__(self, name: str, data_type: type, field_type: str, default=None, required: bool = False):
        self.name = name
        self.data_type = data_type
        self.field_type = field_type
        self.default = default
        self.required = required


class Model(object):
    """Base model class for resources"""
    def __init__(self, name):
        self.name = name

    def add_field(self, field: Field):
        self.__setattr__(field.name, field)
