class Field(object):
    """Base field object for generating fields for models"""

    def __init__(self, name: str, field_type: str, default=None, required: bool = False):
        self.name = name
        self.field_type = field_type
        self.default = default
        self.required = required

    def __str__(self) -> str:
        return f'{self.name}'

    def __unicode__(self) -> str:
        return f'{self.name}'

    def validate(self, value=None):
        """Method for value checking and conversions"""
        if not value:
            if self.default:
                return self.default
        elif self.required:
            raise Exception('Required value not supplied')
        else:
            return value

    def convert(self):
        """Converts the value to the proper output format"""
        raise NotImplementedError

    def to_python(self):
        raise NotImplementedError


class IntField(Field):
    pass


class DateTime(Field):
    pass


class Str(Field):
    pass


class AlphaNum(Field):
    pass


class List(Field):
    pass


class IntList(Field):
    pass


class Bool(Field):
    pass


class Float(Field):
    pass


class Dict(Field):
    pass
