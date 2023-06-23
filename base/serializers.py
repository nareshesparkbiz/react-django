
from rest_framework import serializers
from .models import BasicDetails, EducationDetail, WorkExperiences, Languages, Technologies,RefranceContact,Preference,StateMaster,CityMaster,SelectMaster,OptionMaster,WorkExperiences


class BasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =BasicDetails
        fields='__all__'



class EducationDetailSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=EducationDetail
        fields='__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkExperiences
        fields='__all__'

class LanguageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Languages
        fields='__all__'

class TechnologyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Technologies
        fields='__all__'

class RefranceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=RefranceContact
        fields='__all__'

class PreferenceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Preference
        exclude=['student_id']


class StateMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=StateMaster
        fields=['state_name']

class CityMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CityMaster
        fields=['city_name'] 

class SelectMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=SelectMaster
        fields=['id']

class OptionMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=OptionMaster
        fields=['option_value']



    