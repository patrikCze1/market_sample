from django import forms

class SendMessageAboutOfferForm(forms.Form):
    text = forms.TextField()