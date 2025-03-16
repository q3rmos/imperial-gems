from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.html import escape
from .models import Order, CustomUser
from .validators import (
    text_validator,
    email_validator,
    phone_validator,
    username_validator,
)

USERNAME_PATTERN = r"^[a-z0-9]+$"
TEXT_PATTERN = r"^[A-Za-zА-Яа-яЁё\s]+$"
EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_PATTERN = r"^\d{10,15}$"


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        validators=[username_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
                "pattern": USERNAME_PATTERN,
                "title": "Username can only contain lowercase letters and numbers, without spaces.",
            }
        ),
    )
    email = forms.EmailField(
        validators=[email_validator],
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
                "pattern": EMAIL_PATTERN,
                "title": "Please enter a valid email address (e.g., example@mail.com)",
            }
        ),
    )
    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Phone",
                "pattern": PHONE_PATTERN,
                "title": "Phone number must contain 10-15 digits.",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in {"username", "email", "phone"}:
                field.widget.attrs.update(
                    {"class": "form-control", "placeholder": field.label}
                )


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )


class OrderForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": TEXT_PATTERN,
                "title": "Only letters allowed",
            }
        ),
        validators=[text_validator],
    )

    email = forms.EmailField(
        validators=[email_validator],
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "pattern": EMAIL_PATTERN,
                "title": "Please enter a valid email address (e.g., example@mail.com)",
            }
        ),
    )

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": PHONE_PATTERN,
                "title": "Phone number must contain 10-15 digits.",
            }
        ),
    )

    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": TEXT_PATTERN,
                "title": "Only letters allowed",
            }
        ),
        validators=[text_validator],
    )

    region = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": TEXT_PATTERN,
                "title": "Only letters allowed",
            }
        ),
        validators=[text_validator],
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": TEXT_PATTERN,
                "title": "Only letters allowed",
            }
        ),
        validators=[text_validator],
    )

    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "phone",
            "country",
            "region",
            "city",
            "postal_code",
            "address",
        ]
        widgets = {
            "postal_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "pattern": r"^\d{5,6}$",
                    "title": "Enter a valid postal code (5 or 6 digits)",
                }
            ),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your name",
                "pattern": TEXT_PATTERN,
                "title": "Name can only contain letters and spaces.",
            }
        ),
        validators=[text_validator],
    )

    email = forms.EmailField(
        validators=[email_validator],
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
                "pattern": EMAIL_PATTERN,
                "title": "Please enter a valid email address (e.g., example@mail.com)",
            }
        ),
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your message",
                "rows": 4,
                "minlength": 10,
                "maxlength": 1000,
            }
        )
    )

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return escape(message)
