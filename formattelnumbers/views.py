from django.shortcuts import render

# Create your views here.
from .forms import format_tel_numbers_input_form

#turn tel numbers into a list
def turn_textdata_to_list(textdata):
    listTextData = textdata.split("\r\n")
    return listTextData

# fixing telephone numbers


#turn list into rows
def turn_listTextData_to_row(listTextData):     
    rowTextData = "\r\n".join(str(x) for x in listTextData)
    return rowTextData



# Create your views here.
def format_tel_numbers_input(request):
    if request.method == 'POST':
        numbersToFormat = format_tel_numbers_input_form(request.POST)
        if numbersToFormat.is_valid():


            textdata = numbersToFormat['inputText'].value()
            
            #turn tel numbers into a list
            listTextData = turn_textdata_to_list(textdata)

            #turn list into rows
            rowTextData = turn_listTextData_to_row(listTextData)






            data = {'inputText': rowTextData}
            numbersToFormat = format_tel_numbers_input_form(initial=data)


            return render(request, 'formatTelNumbers/formattelnumers.html', {'numbersToFormat': numbersToFormat})

    else:
        numbersToFormat = format_tel_numbers_input_form()
        return render(request, 'formatTelNumbers/formattelnumers.html', {'numbersToFormat': numbersToFormat})

