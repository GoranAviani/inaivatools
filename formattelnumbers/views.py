from django.shortcuts import render, redirect
from formattelnumbers import cleaningTelNum
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













def get_all_values_by_cell_letter(letter, currentSheet):
    for row in range(1, currentSheet.max_row + 1):
        for column in letter:
            cell_name = "{}{}".format(column, row)
            #print(cell_name)
            #take old data and send it to fixing
            telephoneNo = fix_telephone_format(currentSheet[cell_name].value)
            #put new data in cell


            #print(letter + "1")
            if cell_name == (letter + "1"):
                #print(letter + "0")
                #print("aaaaa")
                currentSheet[cell_name].value = "telephone"
            else:
                currentSheet[cell_name].value = telephoneNo



            print("Cell on position: {} has value: {}".format(cell_name, currentSheet[cell_name].value))



def find_specific_cell(currentSheet):
    for row in range(1, currentSheet.max_row + 1):
        for column in "ABCDEFGHIJKL":  # Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            if currentSheet[cell_name].value == "telephone":
                print("Specific cell on position: {} has value: {}".format(cell_name, currentSheet[cell_name].value))
                return cell_name

def get_column_letter(specificCellLetter):
    letter = specificCellLetter[0:-1]
    print(letter)
    return letter

def format_tel_numbers_upload(request):
    if request.method == 'POST':
        form = uploaded_documents_form(request.POST, request.FILES)
        if form.is_valid():
          
          #  documentName = form['document'].value()
          #  documentFullLocation = "format_tel_number/" + str(documentName)
          
            obj = (uploaded_documents.objects.latest('uploaded_at'))
            print("\n\n evo ga:\n")
            print(obj)
            print("\n\n evo ga:\n")

            print(obj.document)            
            print("\n\n evo ga:\n")

            print(obj.uploaded_at)

            form.save()
            theFile = openpyxl.load_workbook(obj.document)
            allSheetNames = theFile.sheetnames

            print("All sheet names {} " .format(allSheetNames)) 
            for sheet in allSheetNames:
                print("\n\nCurrent sheet name is ******* {} \n" .format(sheet))
                currentSheet = theFile[sheet]
                specificCellLetter = (find_specific_cell(currentSheet))
                letter = get_column_letter(specificCellLetter)


            get_all_values_by_cell_letter(letter, currentSheet)

            theFile.save("media1/" + str(obj.document))


            return redirect('index')
    else:
        form = uploaded_documents_form()
    return render(request, 'formatTelNumbers/format_tel_numbers_upload.html', {
        'form': form
    })

