# -*- coding: utf-8 -*-

class ValidationException(Exception):
    def __init__(self, message, fields):
        super(ValidationException, self).__init__(message)
        self.message = message
        self.fields = fields

