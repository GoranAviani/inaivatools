from django import forms
from .models import uploaded_documents



class format_tel_numbers_input_form(forms.Form):
    inputText = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'merge-text-input'}))
   # joinBy = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}), initial=',')
    


class uploaded_documents_form(forms.ModelForm):
    class Meta:
        model = uploaded_documents
        fields = ('description', 'document')