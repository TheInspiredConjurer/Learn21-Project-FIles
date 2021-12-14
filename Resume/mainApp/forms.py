from django import forms

class ContactUsForm(forms.Form):
  name = forms.CharField(label="Name")
  email = forms.EmailField(label="Email")
  subject = forms.CharField(label="Subject")
  message = forms.CharField(label="Message", widget=forms.Textarea)
