from django.shortcuts import render

# Create your views here.
from .forms import split_text_input_form

# Create your views here.
def split_text_input(request):
    if request.method == 'POST':
        textToSplit = split_text_input_form(request.POST)
        if textToSplit.is_valid():

            textdata = textToSplit['inputText'].value()
            splitBy = textToSplit['splitBy'].value()
            
            #replacing inputed character with \r\n
            textdata = textdata.replace(splitBy, "\r\n")

            data = {'inputText': textdata, 'splitBy': splitBy}
            textToSplit = split_text_input_form(initial=data)
            
            return render(request, 'splitTextLines/splitlines.html', {'textToSplit': textToSplit})

    else:
        textToSplit = split_text_input_form()
        return render(request, 'splitTextLines/splitlines.html', {'textToSplit': textToSplit})


