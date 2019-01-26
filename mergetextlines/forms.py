from django import forms

class merge_text_input_form(forms.Form):
    link_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    link_url = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
   