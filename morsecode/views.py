from django.shortcuts import render

# Create your views here.
from .forms import morse_code_form
from .constants import MORSE_CODE_DICT

def code_decode(**kwargs):
    try:
        inputText = kwargs["inputText"]
        codeOrDecode = kwargs["codeOrDecode"]
    except:
        return "error", "Can not fetch morse code data from the users input"

    #check if all letters are in the morse alphabet. if not return a message to user
    textToProcess = list(inputText)
    for x in textToProcess:
        if x.upper() not in MORSE_CODE_DICT:
            return "error", "Text or parts of text do not belong to international morse code alphabet"

    resultText = ""
    if codeOrDecode == "code":
        for x in textToProcess:
            if x.upper() in MORSE_CODE_DICT:
                resultText += MORSE_CODE_DICT[x.upper()]
    elif codeOrDecode == "decode":
        return "error", "Decoding Morse code to text not built."
    return "success", resultText

def morse_coder_decoder(request):
    templateLocation = "morseCode/morsecode.html"
    if request.method == 'POST':
        morseCodeData = morse_code_form(request.POST)
        if morseCodeData.is_valid():
            inputText = morseCodeData['inputText'].value()
            codeOrDecode = morseCodeData['codeOrDecode'].value()

            # coding or decoding
            morseData = {"inputText": inputText, "codeOrDecode": codeOrDecode}
            morseStatus, morseResult = code_decode(**morseData)

            #Display error message if coding or decoding failed
            if morseStatus == "error":
                data = {'inputText': inputText, 'resultText': morseResult, 'codeOrDecode': codeOrDecode}
                morseCodeData = morse_code_form(initial=data)
                return render(request, templateLocation, {'morseCodeData': morseCodeData})
            #display succesfull text
            data = {'inputText': inputText,'resultText': morseResult, 'codeOrDecode': codeOrDecode}
            morseCodeData = morse_code_form(initial=data)
            return render(request, templateLocation, {'morseCodeData': morseCodeData})
        else:
            morseCodeData = morse_code_form()
            return render(request, templateLocation, {'morseCodeData': morseCodeData})
    else:
        morseCodeData = morse_code_form()
        return render(request, templateLocation, {'morseCodeData': morseCodeData})

