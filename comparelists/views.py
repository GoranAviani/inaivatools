from django.shortcuts import render
from .forms import compare_lists_input_form


# Create your views here.
def compare_lists(request):
    
    
    if request.method == 'POST':
        listsToCompare = compare_lists_input_form(request.POST)
        if listsToCompare.is_valid():

            inputList1 = listsToCompare['inputText1'].value()
            inputList2 = listsToCompare['inputText2'].value()
            foundInList2 = ""
            missingInList2 = ""

##            mergeBy = listsToCompare['joinBy'].value()
            
            #for displaying as result:
            originalInputList1 = inputList1
            originalInputList2 = inputList2

            #replacing \r\n with a "," character and then create lists from inputLists strings
            inputList1 = inputList1.replace("\r\n", ",")
            inputList2 = inputList2.replace("\r\n", ",")
            inputList1 = list(inputList1.split(","))
            inputList2 = list(inputList2.split(","))
            
            #Process the lists and get the result
             
            
            #Display the result data
            data = {'inputText1': originalInputList1, 'inputText2': originalInputList2, 'resultFoundInList2': foundInList2, 'resultMissingInList2': missingInList2}
            listsToCompare = compare_lists_input_form(initial=data)
            
            return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})

    else:
        listsToCompare = compare_lists_input_form()
        return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})
