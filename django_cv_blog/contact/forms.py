from django import forms
from django.forms import widgets
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            "your_firstname",
            "your_lastname",
            "your_email",
            "your_message"
        ]

        labels = {
            'your_firstname': "Adınız",
            'your_lastname': "Soyadınız",
            'your_email': "E-Mail Adres",
            'your_message': "Mesajınız",
        }

        widgets = {
            "your_firstname": widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'Adınız'}),
            "your_lastname": widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'Soyadınız'}),
            "your_email": widgets.TextInput(attrs={"class": "form-control", 'placeholder': 'Email'}),
            "your_message": widgets.Textarea(attrs={"class": "form-control", 'placeholder': 'Mesaj'})
        }
