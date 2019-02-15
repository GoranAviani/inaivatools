from formattelnumbers import cleaningTelNum


#Fix telephone format
def fix_telephone_format(telephoneNo):
    telephoneNo = cleaningTelNum.remove_first_space_from_tel(telephoneNo)
    telephoneNo = cleaningTelNum.remove_plus_from_tel(telephoneNo)
    telephoneNo = cleaningTelNum.remove_country_code(telephoneNo)
    telephoneNo = cleaningTelNum.place_zero_at_first(telephoneNo)
    telephoneNo = cleaningTelNum.remove_all_characters(telephoneNo)
    return telephoneNo



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

            #print("Cell on position: {} has value: {}".format(cell_name, currentSheet[cell_name].value))


def find_specific_cell(currentSheet):
    for row in range(1, currentSheet.max_row + 1):
        for column in "ABCDEFGHIJKL":  # Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            if currentSheet[cell_name].value == "telephone":
                #print("Specific cell on position: {} has value: {}".format(cell_name, currentSheet[cell_name].value))
                return cell_name

def get_column_letter(specificCellLetter): #gets just cell letter from cell name (ex gets f from f1)
    letter = specificCellLetter[0:-1]
    print(letter)
    return letter



#################
#Checking if the uploaded file is safe to work with
def checkIfFileIsSafe(documentName):
    fileExtenstion = str(documentName)[-4:]

    if fileExtenstion in ('xlsx','xlsm'):
        return 'safe_to_work'
    else:
        return 'not_safe_to_work'