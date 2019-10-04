from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status    
#from apirelay.serializers import TelNumberSerializer
from formattelnumbers.views import process_numbers
from apirelay import dataProcessing

def render_api_docs(request):
    return render(
    request,
    'apiRelay/api_docs.html'
)

class format_tel_numbers_api(APIView):
 # serializer_class = TelNumberSerializer

    def get(self, request):     
      
  #      listOfTelNumbers=[]
 #       telCountry = {}
#        telNumberList = {}

        #dict= request._request.GET #geting the data from QueryDict
        #dict = dict.dict() #QueryDict to Python dict
      
        
        qpdict= self.request.query_params.dict()
        try:
           telCountry = qpdict["country_code"]
        except:
            try:
               telNumberList = qpdict["telephone_numbers"]
            except:
               return Response({'status': "FAILED ", "message": "No country code and no telephone numbers"})
            return Response({'status': "FAILED ", "message": "No country code"})

        try:
           telNumberList = qpdict["telephone_numbers"]
        except:
           return Response({'status': "FAILED ", "message": "No telephone numbers"})

        telCountry = qpdict["country_code"]
        result = dataProcessing.check_country_code(telCountry)
        if result == "non_existing_country":
           data = {'status': "FAILED", "message": "Unknown country code"}
           return Response(data, status=status.HTTP_200_OK)
          
        telNumberList = qpdict["telephone_numbers"]
        listOfTelNumbers = telNumberList.split(",")
      
        #Caling a view from another app
        listResult = process_numbers(listOfTelNumbers, telCountry)
        #print(listResult)

        listResultChar = ",".join(listResult)
        #print(listResultChar)

        data = {'status': "SUCCESS", "country_code": telCountry, 'telephone_numbers': listResultChar}
        return Response(data, status=status.HTTP_200_OK)



    