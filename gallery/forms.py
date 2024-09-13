from django import forms

class ContactForm(forms.Form):
  subject = forms.CharField(max_length=100)
  name = forms.CharField(required=False, label='Your name')
  email = forms.EmailField(required=False, label='Your e-mail address')
  message = forms.CharField(widget=forms.Textarea)
  cc_myself = forms.BooleanField(required=False)
  realsubject = forms.CharField(max_length=100)
  realname = forms.CharField(required=False, label='Your name')
  realemail = forms.EmailField(required=False, label='Your e-mail address')
  realmessage = forms.CharField(widget=forms.Textarea)
  realcc_myself = forms.BooleanField(required=False)

  1 
