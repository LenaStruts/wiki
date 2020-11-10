from django import forms

class NewEntry(forms.Form):
    title = forms.CharField(label='Entry Title')
    content = forms.CharField(label='Entry text', widget=forms.Textarea(attrs={'placeholder': 'Write your entry text here ...'}))