from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status    
from apirelay.serializers import TelNumberSerializer
from formattelnumbers.views import process_numbers

class format_tel_numbers_api(APIView):
    serializer_class = TelNumberSerializer

    def post(self, request):
        telCountry = request.data.get("telCountry")
        telNumberList = request.data.get("telNumberList")

        listOfTelNumbers = telNumberList.split(",")
        listResult = process_numbers(listOfTelNumbers)
        print(listResult)

        
        listResultChar = ",".join(listResult)
        print(listResultChar)

        data = {'responseMessage': "Success", "telCountry": telCountry, 'telNumberList': listResultChar}
        serializer = TelNumberSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)