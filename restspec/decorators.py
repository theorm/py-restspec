# -*- coding: utf-8 -*-
from .exceptions import ValidationException
from functools import wraps
from jsonschema import validate as schema_validate, ValidationError


class ValidatorDecorator(object):
    def __init__(self, schema_or_schema_parameter_name):
        self.schema_or_schema_parameter_name = schema_or_schema_parameter_name

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            instance = args[0]

            if isinstance(self.schema_or_schema_parameter_name, str):
                schema = getattr(instance, self.schema_or_schema_parameter_name)
            else:
                schema = self.schema_or_schema_parameter_name

            try:
                schema_validate(self.object(), schema)
                return f(*args, **kwargs)
            except ValidationError as e:
                raise ValidationException(e.message, e.instance)
        return wrapper

    def object(self):
        raise NotImplementedError()
