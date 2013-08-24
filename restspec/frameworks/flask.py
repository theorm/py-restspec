# -*- coding: utf-8 -*-
from __future__ import absolute_import 
from ..decorators import ValidatorDecorator

try:
    from flask import request
    __all__ = [
        'validate_query',
        'validate_payload'
    ]
except ImportError, e:
    __all__ = []

class validate_query(ValidatorDecorator):
    def object(self):
        return request.args

class validate_payload(ValidatorDecorator):
    def object(self):
        return request.json()
