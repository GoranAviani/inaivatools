from django import forms

class compare_lists_input_form(forms.Form):
    inputList1 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
    inputList2 = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
    
