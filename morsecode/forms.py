from django import forms


class morse_code_form(forms.Form):
    inputText = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'merge-text-input'}))
    resultText = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'merge-text-input'}))
    codeOrDecode = forms.ChoiceField(choices=[("code", "Code to Morse"), ("decode", "Decode from Morse")])  # note: list of tuples
