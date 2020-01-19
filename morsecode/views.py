from django.shortcuts import render

# Create your views here.
from .forms import morse_code_form



def morse_coder_decoder(request):
    if request.method == 'POST':
        morseCodeData = morse_code_form(request.POST)
        if morseCodeData.is_valid():
            inputText = morseCodeData['inputText'].value()
            codeOrDecode = morseCodeData['codeOrDecode'].value()

            # replacing inputed character with \r\n
            textdata = textdata.replace(splitBy, "\r\n")

            data = {'inputText': textdata, 'splitBy': splitBy}
            textToSplit = split_text_input_form(initial=data)

            return render(request, 'splitTextLines/splitlines.html', {'textToSplit': textToSplit})

    else:
        morseCodeData = morse_code_form()
        return render(request, 'morseCode/morsecode.html', {'morseCodeData': morseCodeData})

