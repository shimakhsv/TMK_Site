from django.contrib import admin
from .forms import ContactForm
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ["email"]
    form = ContactForm

admin.site.register(Contact,ContactAdmin)
