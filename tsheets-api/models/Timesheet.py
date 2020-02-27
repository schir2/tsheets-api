class Field(object):
    def __init__(self, name: str, required=False, blank=False, null=False, default=''):
        self.default = default
        self.null = null
        self.required = required
        self.name = name
        self.blank = blank

        self.validate()

    def validate(self):
        self.check_name()

    def check_name(self):
        assert type(self.name) == str, 'Name: Invalid Data Type, should be string.'
        assert self.name[0].isalpha(), 'Name: should start with a letter.'
        assert self.name.isalpha(), 'Name: should contain only alphanumeric characters.'

    def to_python(self, value):
        pass


class IntField(Field):

    def to_python(self, value):
        assert type(value) == int, 'Value: should be type int.'
        return value


class Timesheet(object):
    id = IntField(name='dog')



timesheet = Timesheet
timesheet.id.to_python(10)
timesheet.id.to_python('H')
