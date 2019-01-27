from django import forms

class format_tel_numbers_input_form(forms.Form):
    inputText = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
   # joinBy = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}), initial=',')
    