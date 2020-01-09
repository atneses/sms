# -*- coding: utf-8 -*-
import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

PHONE_REGEX = r'^\+?[0-9- ]{10,}'


class PhoneSerializer(serializers.Serializer):

    """
    A. 12-3456-7890 (separated by dash)
    B. 1234567890 (non separated)
    C. 12 3456 7890 (separated by spaces)
    D. +52-12-3456-7890 (with the country code separated by dash)
    E. +521234567890 (with the country code non separated)
    F. +52 12 3456 7890 (with the country code separated by spaces)

    Invalid Phone Numbers:
    A. I’m a phone number
    B. 123123 (just 6 digit length)
    C. 551049abcd
    """
    phone = serializers.CharField(max_length=20)

    def validate_phone(self, phone):
        if not re.match(PHONE_REGEX, phone):
            raise ValidationError(f'"{phone}" is not a valid phone')
        return phone
