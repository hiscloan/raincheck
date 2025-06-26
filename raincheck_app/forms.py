from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Phone Number', required=False)
    message = forms.CharField(widget=forms.Textarea, label='Message')