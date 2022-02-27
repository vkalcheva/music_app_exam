import re

from django.core.exceptions import ValidationError

VALIDATE_USERNAME_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_username(value):
    if not re.match("^[A-Za-z0-9_-]*$", value):
        raise ValidationError(VALIDATE_USERNAME_MESSAGE)