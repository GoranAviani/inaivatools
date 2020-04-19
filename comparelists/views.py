from django.shortcuts import render
from .forms import compare_lists_input_form

def display_results_in_rows(foundInList2, missingInList2):
    forDisplayFoundInList2 = ""
    forDisplayMissingInList2 = ""

    for x in foundInList2:
        addToResult = x+"\r\n"
        forDisplayFoundInList2 += addToResult 
    for x in missingInList2:
        addToResult = x+"\r\n"
        forDisplayMissingInList2 += addToResult

    return forDisplayFoundInList2, forDisplayMissingInList2

def process_comparison_of_lists(inputList1, inputList2):
    foundInList2 = []
    missingInList2 = []

    for x in inputList1: #for every x in list 1
        if x in inputList2: # find it in list 2 and save in found 1
            foundInList2.append(x)
        else: # if x in not found in list 2 save it in missing 2
            missingInList2.append(x)

    forDisplayFoundInList2, forDisplayMissingInList2 = display_results_in_rows(foundInList2, missingInList2)

    return forDisplayFoundInList2, forDisplayMissingInList2




def compare_lists(request):

    if request.method == 'POST':
        listsToCompare = compare_lists_input_form(request.POST)
        if listsToCompare.is_valid():

            inputList1 = listsToCompare['inputText1'].value()
            inputList2 = listsToCompare['inputText2'].value()
            
            #for displaying as result:
            originalInputList1 = inputList1
            originalInputList2 = inputList2

            #replacing \r\n with a "," character and then create lists from inputLists strings
            inputList1 = inputList1.replace("\r\n", ",")
            inputList2 = inputList2.replace("\r\n", ",")
            inputList1 = list(inputList1.split(","))
            inputList2 = list(inputList2.split(","))
            
            #Process the lists and get the result
            foundInList2, missingInList2 = process_comparison_of_lists(inputList1, inputList2)

            
            #Display the result data
            data = {'inputText1': originalInputList1, 'inputText2': originalInputList2, 'resultFoundInList2': foundInList2, 'resultMissingInList2': missingInList2}
            listsToCompare = compare_lists_input_form(initial=data)
            
            return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})
    else:
        listsToCompare = compare_lists_input_form()
        return render(request, 'compareLists/comparelists.html', {'listsToCompare': listsToCompare})
