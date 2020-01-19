from django.shortcuts import render

# Create your views here.
from .forms import morse_code_form
from django.http import HttpResponse


def code_decode(**kwargs):
    try:
        inputText = kwargs["inputText"]
        codeOrDecode = kwargs["codeOrDecode"]
    except:
        return "error", "Can not fetch morse code data from the users input"
    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

    #check if all letters are in the morse alphabet. if not return a message to user
    textToProcess = list(inputText)
    for x in textToProcess:
        if x.upper() not in MORSE_CODE_DICT:
            return "error", "Text or parts of text do not belong to international morse code alphabet"

    resultText = ""
    if codeOrDecode == "code":
        textToProcess = list(inputText)
        for x in textToProcess:
            pass
    elif codeOrDecode == "decode":
        pass



    return "success", "result text"

def morse_coder_decoder(request):
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
                return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})

            data = {'inputText': inputText,'resultText': morseResult, 'codeOrDecode': codeOrDecode}
            morseCodeData = morse_code_form(initial=data)
            return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})
        else:
            morseCodeData = morse_code_form()
            return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})
    else:
        morseCodeData = morse_code_form()
        return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})

