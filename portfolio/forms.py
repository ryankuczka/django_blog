from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 80}))
    cc_myself = forms.BooleanField(required=False, label='Send yourself a copy')
