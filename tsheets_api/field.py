import datetime
import dateparser
from tsheets_api.settings import TZ


class Field(object):
    """Base field object for generating fields for models"""

    def __init__(self, name: str, default=None, required: bool = False):

        self.name = name
        self.default = default
        self.required = required

    def __str__(self) -> str:
        return f'{self.name}'

    def __unicode__(self) -> str:
        return f'{self.name}'

    def validate(self, value=None):
        """Method for value checking and conversions"""
        if value is None:
            if self.required is True:
                raise Exception('Required value not supplied')
            return self.default
        else:
            return value

    def convert(self, value):
        """Convert value to proper format"""
        raise NotImplemented

    def to_python(self, value=None) -> str:
        """Takes a value, validates it and the converts it ot the proper format"""
        value = self.validate(value)
        value = self.convert(value)
        return value

    def to_filter(self, value=None) -> str:
        """Takes a value, validates it and the converts it ot the proper format"""
        value = self.validate(value)
        value = self.convert(value)
        return value


class Int(Field):

    def __init__(self, name: str, default=None, required: bool = False, max_value: int = None, min_value: int = None):
        super().__init__(name, default, required)
        self.max_value = max_value
        self.min_value = min_value

    def validate(self, value=None):
        """Method for value checking and conversions"""
        if value is None:
            if self.required is True:
                raise Exception('Required value not supplied')
            return self.default
        else:
            if self.max_value is not None:
                if int(value) > self.max_value:
                    raise Exception('Value is greater than max_value')
            if self.min_value is not None:
                if int(value) < self.min_value:
                    raise Exception('Value is lower than min_value')
            return value

    def convert(self, value):
        if type(value) == int:
            return str(value)
        return value


class DateTime(Field):

    def convert(self, value):
        if type(value) == str:  # Checks if value is string and converts it to datetime object.
            value = dateparser.parse(value)
        if type(value) == datetime.datetime:
            pass
        if not value.tzinfo:
            value.replace(tzinfo=TZ)  # Adds timezone encoding
        return value.isoformat()


class Str(Field):

    def convert(self, value):
        return str(value)


class List(Field):

    def convert(self, value):
        if type(value) == list:
            return ','.join(value)
        if ',' not in value:
            return ','.join(value.split(' '))
        return value


class Bool(Field):
    def convert(self, value):
        if value in (True, 'true', 't', 'T', 'yes', 'Yes'):
            return 'yes'
        elif value in (False, 'false', 'f', ' F', 'yes', 'Yes'):
            return 'no'


class CustomBool(Field):
    def convert(self, value):
        if value in (True, 'true', 't', 'T', 'yes', 'Yes'):
            return 'yes'
        elif value in (False, 'false', 'f', ' F', 'yes', 'Yes'):
            return 'no'
        return 'both'


class Float(Field):

    def convert(self, value):
        return str(value)


class Q(Field):
    pass


if __name__ == '__main__':
    """Testing Field Methods"""

    id = IntField(name='id', required=False)
    id.to_python()
    dt = DateTime(name='dt', required=False, default=datetime.datetime.now())
    dt.to_python()
