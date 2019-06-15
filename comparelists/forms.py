from django import forms

class compare_lists_input_form(forms.Form):
    inputText1 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
    inputText2 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
    resultFoundInList2 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
    resultMissingInList2 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))

    
