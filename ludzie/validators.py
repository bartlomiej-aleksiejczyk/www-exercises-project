import re
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import date
import calendar

DNI_MIESIACA = list(calendar.month_name)

def czy_nie_przyszlosc_miesiac(miesiac):
    if miesiac not in DNI_MIESIACA:
        raise ValidationError(f"{miesiac} is not a valid month name.")
    current_month = date.today().strftime("%B")
    if DNI_MIESIACA.index(miesiac) > DNI_MIESIACA.index(current_month):
        raise ValidationError(f"{miesiac} jest pozniejszy niz terazniejszy miesiac - {current_month}.")

def czy_literki(string):
    if not re.search("^[^a-zA-Z]+$", string):
        raise ValidationError(
            _("%(value)s is not alphanumeric"),
            params={"value": string},
        )