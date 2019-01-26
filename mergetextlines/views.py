from django.shortcuts import render
#from django.shortcuts import redirect
from .forms import merge_text_input_form

# Create your views here.
def merge_text_input(request):
    if request.method == 'POST':
        textToJoin = merge_text_input_form(request.POST)
        if textToJoin.is_valid():
          #  form = textToJoin.save(commit=False)
          #  form.link_user = request.user
            #Check does the link have http or https in the beginning
         #   form.link_url = add_HTTP_to_linkurl(form.link_url)
         #   form.save()
            print("ssssss")
        #  messages.success(request, 'Link saved!',extra_tags='link_create')
        #return redirect('dashboard')
    else:
        textToJoin = merge_text_input_form()
        return render(request, 'mergeTextLines/mergelines.html', {'textToJoin': textToJoin})

