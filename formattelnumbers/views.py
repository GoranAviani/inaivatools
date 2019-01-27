from django.shortcuts import render

# Create your views here.
from .forms import format_tel_numbers_input_form

# Create your views here.
def format_tel_numbers_input(request):
    if request.method == 'POST':
        numbersToFormat = format_tel_numbers_input_form(request.POST)
        if numbersToFormat.is_valid():

            data = {'inputText': "aaa"}
            form = format_tel_numbers_input_form(initial=data)
            return render(request, 'formatTelNumbers/formattelnumbers.html', {'form': form})
            #return render(request, 'formatTelNumbers/mergelines.html', {'numbersToFormat': numbersToFormat})

    else:
        numbersToFormat = format_tel_numbers_input_form()
        return render(request, 'formatTelNumbers/formattelnumers.html', {'numbersToFormat': numbersToFormat})

