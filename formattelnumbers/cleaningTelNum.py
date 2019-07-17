
#Sometimes the first character is space (" ")
def remove_first_space_from_tel(telephoneNo):
    if len(list(telephoneNo)) > 0:
        if telephoneNo[0] == " ":
            telephoneNo = telephoneNo[1:len(telephoneNo)]
    return telephoneNo



#Remove first + from the telephone number
def remove_plus_from_tel(telephoneNo):
    if len(list(telephoneNo)) > 0:
        if telephoneNo[0] == "+":
            telephoneNo = telephoneNo[1:len(telephoneNo)]
    return telephoneNo

#Remove Swedish country code
def remove_country_code(telephoneNo, telCountry = None):
    if telCountry == "SE":
        if len(list(telephoneNo)) > 0:
            if telephoneNo[0:2] == "46":
                telephoneNo = telephoneNo[2:len(telephoneNo)]
            elif telephoneNo[0:3] == "046":
                telephoneNo = telephoneNo[3:len(telephoneNo)]
            elif telephoneNo[0:4] == "0046":
                telephoneNo = telephoneNo[4:len(telephoneNo)]
            elif telephoneNo[0:4] == "+346": #Not sure if its used
                telephoneNo = telephoneNo[4:len(telephoneNo)]
            elif telephoneNo[0:2] == "00": #not sure if needed but it is ok bcs I add first 0 later on if its  missing
                telephoneNo = telephoneNo[2:len(telephoneNo)]
    elif telCountry == "FI":
        if len(list(telephoneNo)) > 0:
            if telephoneNo[0:2] == "58":
                telephoneNo = telephoneNo[2:len(telephoneNo)]
            elif telephoneNo[0:3] == "058":
                telephoneNo = telephoneNo[3:len(telephoneNo)]
            elif telephoneNo[0:4] == "0058":
                telephoneNo = telephoneNo[4:len(telephoneNo)]
            elif telephoneNo[0:4] == "+358": #Used according to wikipedia
                telephoneNo = telephoneNo[4:len(telephoneNo)]
            elif telephoneNo[0:2] == "00": #not sure if needed but it is ok bcs I add first 0 later on if its  missing
                telephoneNo = telephoneNo[2:len(telephoneNo)]
    return telephoneNo

#IF 0 is missing at beggining place it
def place_zero_at_first(telephoneNo):
    if len(list(telephoneNo)) > 0:
        if telephoneNo[0] != "0":
            telephoneNo = "0" + telephoneNo
    return telephoneNo

#Remove all non numeric characters from tel number
def remove_all_characters(telephoneNo):
    if len(list(telephoneNo)) > 0:
        fixedTelNo = ""
        for x in telephoneNo:
            if x.isdigit():
                fixedTelNo += x
        return fixedTelNo