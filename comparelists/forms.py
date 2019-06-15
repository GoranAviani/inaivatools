from django import forms

class compare_lists_input_form(forms.Form):
    inputText1 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'compare-lists-input'}))
    inputText2 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'compare-lists-input'}))
    resultFoundInList2 = forms.CharField(label='',required=False, widget=forms.Textarea(attrs={'class':'compare-lists-input'}))
    resultMissingInList2 = forms.CharField(label='',required=False, widget=forms.Textarea(attrs={'class':'compare-lists-input'}))

    
