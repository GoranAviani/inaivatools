from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status    
from apirelay.serializers import TelNumberSerializer

class format_tel_numbers_api(APIView):
    serializer_class = TelNumberSerializer

    def post(self, request):
        telCountry = request.data.get("telCountry")
        telNumberList = request.data.get("telNumberList")

        stringOfTestList = telNumberList.split(",")
        for x in stringOfTestList:
            print(str(x))
        data = {'responseMessage': "Success", "telCountry": telCountry, 'telNumberList': telNumberList}
        serializer = TelNumberSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)