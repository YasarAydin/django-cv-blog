from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def contact(request):
    if request.method == "POST":
        contactForm = forms.ContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            return redirect('index')
    else:
        contactForm = forms.ContactForm()
    return render(request, "contact.html", context={
        "contactForm": contactForm
    })
