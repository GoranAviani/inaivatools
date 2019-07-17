from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status    
from apirelay.serializers import TelNumberSerializer
from formattelnumbers.views import process_numbers
from apirelay import dataProcessing
"""
class format_tel_numbers_api(APIView):
    serializer_class = TelNumberSerializer

    def post(self, request):
        telCountry = request.data.get("telCountry")
        telNumberList = request.data.get("telNumberList")

        listOfTelNumbers = telNumberList.split(",")
        listResult = process_numbers(listOfTelNumbers)
        #print(listResult)

        listResultChar = ",".join(listResult)
        #print(listResultChar)

        data = {'responseMessage': "Success", "telCountry": telCountry, 'telNumberList': listResultChar}
        serializer = TelNumberSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

 #if self.request.method == 'GET':



class format_tel_numbers_api(APIView):
    serializer_class = TelNumberSerializer


    def get(self, request):      
        
        listOfTelNumbers=[]
        #telNumberList =""
        telCountry = {}
        telNumberList = {}

        dict= request._request.GET #geting the data from QueryDict
        dict = dict.dict() #QueryDict to Python dict
        #print("EVOOOO "+ str(dict))
        if bool(dict) is not False: # is dict is not empty then look for these fields
            telCountry = dict["telCountry"]

             

            telNumberList = dict["telNumberList"]
            listOfTelNumbers = telNumberList.split(",")
            
            result = dataProcessing.check_country_code(telCountry)
            if result == "non_existing_country":
                data = {'responseMessage': "Failure. Unknown country", "telCountry": "Unknown country code", 'telNumberList': "This field may not be blank."}
                serializer = TelNumberSerializer(data=data)
                if serializer.is_valid():
                    return Response(serializer.data, status=status.HTTP_200_OK)
                

        #Caling a view from another app
        listResult = process_numbers(listOfTelNumbers)
        #print(listResult)

        listResultChar = ",".join(listResult)
        #print(listResultChar)

        data = {'responseMessage': "Success", "telCountry": telCountry, 'telNumberList': listResultChar}
        serializer = TelNumberSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    