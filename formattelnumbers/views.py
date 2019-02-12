from django.shortcuts import render, redirect
from formattelnumbers import cleaningTelNum, cleaningTelNumPreparation
#format uploaded files
#from openpyxl import *
import openpyxl
# Create your views here.

from .forms import format_tel_numbers_input_form, uploaded_documents_form
from .models import uploaded_documents

#turn tel numbers into a list
def turn_textdata_to_list(textdata):
    listTextData = textdata.split("\r\n")
    return listTextData

# fixing telephone numbers


#turn list into rows
def turn_list_to_row(numberList):     
    rowTextData = "\r\n".join(str(x) for x in numberList)
    return rowTextData

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
                number = cleningTelNumPreparation.fix_telephone_format(number)
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
          
            documentName = form['document'].value()
                        
            form.save()

            theFile = openpyxl.load_workbook("media/format_tel_number/" + str(documentName))
            allSheetNames = theFile.sheetnames

#            print("\n\nAll sheet names {} " .format(allSheetNames)) 
            for sheet in allSheetNames:
                #print("\n\nCurrent sheet name is ******* {} \n" .format(sheet))
                currentSheet = theFile[sheet]
                specificCellLetter = (cleaningTelNumPreparation.find_specific_cell(currentSheet))
                letter = cleaningTelNumPreparation.get_column_letter(specificCellLetter)


                cleaningTelNumPreparation.get_all_values_by_cell_letter(letter, currentSheet)

            
            theFile.save("media/format_tel_number/" + str(documentName))

            return redirect('index')
    else:
        form = uploaded_documents_form()
    return render(request, 'formatTelNumbers/format_tel_numbers_upload.html', {
        'form': form
    })

