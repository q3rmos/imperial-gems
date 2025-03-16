from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.core.validators import validate_email
import re


@deconstructible
class UsernameValidator:
    def __call__(self, value):
        if not re.match(r"^[a-z0-9]+$", value.strip().lower()):
            raise ValidationError(
                "Username can only contain lowercase letters and numbers, without spaces."
            )


@deconstructible
class TextValidator:
    def __init__(
        self, pattern=r"^[A-Za-zА-Яа-яЁё\s]+$", error_message="Only letters allowed"
    ):
        self.pattern = pattern
        self.error_message = error_message

    def __call__(self, value):
        if not re.match(self.pattern, value.strip()):
            raise ValidationError(self.error_message)


@deconstructible
class EmailValidator:
    def __call__(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError(
                "Please enter a valid email address (e.g., example@mail.com)"
            )


@deconstructible
class PhoneValidator:
    def __call__(self, value):
        if not re.match(r"^\d{10,15}$", value.strip()):
            raise ValidationError("Phone number must contain 10-15 digits.")


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"[a-z]", password):
            raise ValidationError(
                "Password must contain at least one lowercase letter."
            )
        if not re.search(r"\d", password):
            raise ValidationError("Password must contain at least one digit.")

    def get_help_text(self):
        return (
            "Your password must be at least 8 characters long, "
            "contain at least one uppercase letter, one lowercase letter, and one digit."
        )


username_validator = UsernameValidator()
text_validator = TextValidator()
email_validator = EmailValidator()
phone_validator = PhoneValidator()
