from django import forms
from .models import User
from django.core.validators import RegexValidator
from datetime import date


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "password": "Password",
            "user_address": "Your Address",
            "user_mobile": "Phone Number",
            "user_email": "Your Email"
        }
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_name", "password"]


class MonthYearWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        months = [
            ('', 'Month'),
            (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
            (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
            (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
        ]
        years = [(str(year), str(year)) for year in range(2022, 2030)]

        widgets = [
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years)
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.month, value.year]
        return [None, None]

    def format_output(self, rendered_widgets):
        return '<div class="select-month-year">{}</div>'.format(''.join(rendered_widgets))

    def value_from_datadict(self, data, files, name):
        month, year = super().value_from_datadict(data, files, name)
        if month and year:
            return date(year=int(year), month=int(month), day=1)
        return None

class PaymentForm(forms.Form):
    account_number = forms.CharField(
        label='Account Number',
        max_length=16,
        validators=[RegexValidator(r'^[0-9]{16}$', 'Account number must be 16 digits')]
    )
    expiry_date = forms.DateField(
        label='Expiry Date',
        widget=MonthYearWidget,
        input_formats=['%m %Y']
    )
    cvv = forms.CharField(
        label='CVV',
        max_length=3,
        validators=[RegexValidator(r'^[0-9]{3}$', 'CVV must be 3 digits')]
    )
