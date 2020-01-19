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
                return HttpResponse(morseResult)


            data = {'inputText': inputText,'resultText': morseResult, 'codeOrDecode': codeOrDecode}
            morseCodeData = morse_code_form(initial=data)

            return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})

    else:
        morseCodeData = morse_code_form()
        return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})

