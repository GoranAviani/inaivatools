from django import forms

class split_text_input_form(forms.Form):
    inputText = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
    splitBy = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}), initial="','")
    