from django.shortcuts import render
from .forms import compare_lists_input_form


# Create your views here.
def compare_lists(request):
    
    '''
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
    '''
    listsToCompare = compare_lists_input_form()
    return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})
