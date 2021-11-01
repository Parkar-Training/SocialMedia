from rest_framework import serializers
from frndlst.models import frnd_list



class Frnd_listClass(serializers.ModelSerializer):
    #FuserId = serializers.CharField(required=False)
    #FrndId = serializers.CharField(max_length=3,required=False)
    #Stat = serializers.CharField(max_length=3,required=False)

    class Meta:
        model = frnd_list
        fields = '__all__'
        #fields = ('UId','FrndId','Stat')