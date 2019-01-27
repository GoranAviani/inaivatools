from django.shortcuts import render
#from django.shortcuts import redirect
from .forms import merge_text_input_form

# Create your views here.
def merge_text_input(request):
    if request.method == 'POST':
        textToJoin = merge_text_input_form(request.POST)
        if textToJoin.is_valid():

            texdata = textToJoin['inputText'].value()
            mergeBy = textToJoin['joinBy'].value()
            
            texdata = texdata.replace("\r\n", mergeBy)
            data = {'inputText': texdata, 'joinBy': mergeBy}
            textToJoin = merge_text_input_form(initial=data)
            
            return render(request, 'mergeTextLines/mergelines.html', {'textToJoin': textToJoin})

    else:
        textToJoin = merge_text_input_form()
        return render(request, 'mergeTextLines/mergelines.html', {'textToJoin': textToJoin})


          # 
  #          text = textToJoin['inputText']
   #         joiner = textToJoin['joinBy']

            #form = MyForm(request.POST)
        #print form['my_field'].value()
        #print form.data['my_field']

    #ili

#if myform.is_valid():
#  data = myform.cleaned_data
#  field = data['field']

#ili
 #if(request.POST):
 #       login_data = request.POST.dict()
 #       username = login_data.get("username")
 #       password = login_data.get("password")
 #      user_type = login_data.get("user_type")
 #      print(user_type, username, password)

            #text['data'].replace("\r\n", joiner['data'])
            #textToJoin['inputText']['data'] = newText

    

           # 
           #  return super(merge_text_input).form_valid(data)
            
                    
           # text = textToJoin['inputText']
             
           # return render(request, 'mergeTextLines/mergelines.html', {'form': form})


           # return render(request, 'mergeTextLines/mergelines.html', {'textToJoin': textToJoin})

          #  form = textToJoin.save(commit=False)
          #  
          # textToJoin.link_user = request.user
            #Check does the link have http or https in the beginning
         #   form.link_url = add_HTTP_to_linkurl(form.link_url)
         #   form.save()
            
           
            
        #  messages.success(request, 'Link saved!',extra_tags='link_create')
        #return redirect('dashboard')

