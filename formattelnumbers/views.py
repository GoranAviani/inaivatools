from django.shortcuts import render, redirect
from formattelnumbers import cleaningTelNum

# Create your views here.
from .forms import format_tel_numbers_input_form, uploaded_documents_form

#turn tel numbers into a list
def turn_textdata_to_list(textdata):
    listTextData = textdata.split("\r\n")
    return listTextData

# fixing telephone numbers


#turn list into rows
def turn_list_to_row(numberList):     
    rowTextData = "\r\n".join(str(x) for x in numberList)
    return rowTextData

#Fix telephone format
def fix_telephone_format(telephoneNo):
    telephoneNo = cleaningTelNum.remove_first_space_from_tel(telephoneNo)
    telephoneNo = cleaningTelNum.remove_plus_from_tel(telephoneNo)
    telephoneNo = cleaningTelNum.remove_country_code(telephoneNo)
    telephoneNo = cleaningTelNum.place_zero_at_first(telephoneNo)
    telephoneNo = cleaningTelNum.remove_all_characters(telephoneNo)
    return telephoneNo

# Create your views here.
def format_tel_numbers_input(request):
    if request.method == 'POST':
        numbersToFormat = format_tel_numbers_input_form(request.POST)
        if numbersToFormat.is_valid():


            textdata = numbersToFormat['inputText'].value()
            
            #turn tel numbers into a list
            listTextData = turn_textdata_to_list(textdata)

            listResult = []
            for number in listTextData:
                number = fix_telephone_format(number)
                listResult.append(number)



            #turn list into rows
            rowTextData = turn_list_to_row(listResult)



            data = {'inputText': rowTextData}
            numbersToFormat = format_tel_numbers_input_form(initial=data)


            return render(request, 'formatTelNumbers/formattelnumers.html', {'numbersToFormat': numbersToFormat})

    else:
        numbersToFormat = format_tel_numbers_input_form()
        return render(request, 'formatTelNumbers/formattelnumers.html', {'numbersToFormat': numbersToFormat})



def format_tel_numbers_upload(request):
    if request.method == 'POST':
        form = uploaded_documents_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = uploaded_documents_form()
    return render(request, 'formatTelNumbers/format_tel_numbers_upload.html', {
        'form': form
    })

