from tsheets_api.field import Field
import types


class Resource(object):
    """Resource for with read, write methods"""
    model = NotImplemented
    url = NotImplemented

    @classmethod
    def generate_fields(cls):
        for field, value in cls.model.__dict__.items():
            if isinstance(value, Field):
                if value.__dict__.get('is_filter', False):
                    setattr(cls, value.filter_name, value)

    @classmethod
    def get(cls, *args, **kwargs):
        raise NotImplementedError
