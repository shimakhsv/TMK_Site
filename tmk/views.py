from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            new_patron = f.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

        return render(request,"base.html",{})