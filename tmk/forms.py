from django import forms;
from .models import Contact;

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['email','message']
    #
    # def clean_email(self):
    #     email=self.cleaned_data.get('email')
    #     # if not "@" in email:
    #     #     raise forms.ValidationError("please deqat!")
    #     return email