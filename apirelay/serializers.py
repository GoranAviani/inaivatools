from rest_framework import serializers

class TelNumberSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   responseMessage = serializers.CharField()
   telCountry = serializers.CharField(required=False, allow_null=True)
   telNumberList = serializers.CharField(required=False, allow_blank=True)
    #testList = serializers.ListField()