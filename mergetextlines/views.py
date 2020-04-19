from django.shortcuts import render
#from django.shortcuts import redirect
from .forms import merge_text_input_form

# Create your views here.
def merge_text_input(request):
    if request.method == 'POST':
        textToJoin = merge_text_input_form(request.POST)
        if textToJoin.is_valid():

            textdata = textToJoin['inputText'].value()
            mergeBy = textToJoin['joinBy'].value()
            
            #replacing \r\n with a inputed character
            textdata = textdata.replace("\r\n", mergeBy)
            data = {'inputText': textdata, 'joinBy': mergeBy}
            textToJoin = merge_text_input_form(initial=data)
            
            return render(request, 'mergeTextLines/mergelines.html', {'textToJoin': textToJoin})

    else:
        textToJoin = merge_text_input_form()
        return render(request, 'mergeTextLines/mergelines.html', {'textToJoin': textToJoin})
