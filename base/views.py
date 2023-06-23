from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from base.serializers import BasicDetailSerializer, EducationDetailSerializer, WorkExperienceSerializer, RefranceDetailSerializer, PreferenceDetailSerializer, LanguageDetailSerializer, TechnologyDetailSerializer,StateMasterSerializer,CityMasterSerializer,SelectMasterSerializer,OptionMasterSerializer


from base.models import BasicDetails, EducationDetail, WorkExperiences, RefranceContact, Preference, Languages, Technologies,StateMaster,CityMaster,SelectMaster,OptionMaster


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None


def education(id, formresponse):
    academicData = EducationDetail.objects.filter(student_id=id)

    eduForm = len(formresponse['board_name'])
    eduID = len(academicData)
    print(eduForm, eduID)
    for i in range(max(eduForm, eduID)):

        if i > eduID and i <= eduForm:
            EducationDetail.objects.filter(student_id=id).delete()

        else:
            exec = {
                'course_name': str(formresponse['course_name'][i]),
                'board_name': str(formresponse['board_name'][i]),
                'passing_year': str(formresponse['passing_year'][i]),
                'percentage': formresponse['percentage'][i]
            }

            if i < eduID:
                eduserializer = EducationDetailSerializer(
                    academicData[i], data=exec,partial=True)
            else:
                exec['student_id']=id
                eduserializer = EducationDetailSerializer(data=exec)
               

            if eduserializer.is_valid():

                eduserializer.save()
            else:
                print(eduserializer.errors)
    return "ok"


def work(id, formresponse):
    work = WorkExperiences.objects.filter(student_id=id)
    workForm1 = len(formresponse['company_name'])
    workId = len(work)

    for i in range(max(len(formresponse['company_name']), workId)):
        if i > workId and i < len(formresponse['company_name']):
            WorkExperiences.objects.filter(student_id=id).delete()

        else:
            print("efrsefsdfsdfsdfsdfsdfsdfsdf")

            exec = {
                'company_name': str(formresponse['company_name'][i]),
                'designation': str(formresponse['designation'][i]),
                'start_date': str(formresponse['start_date'][i]),
                'end_date': str(formresponse['end_date'][i]),
            }

            if i < workId:

                workserializer = WorkExperienceSerializer(work[i], data=exec,partial=True)

            else:
                exec['student_id']=id
                workserializer = WorkExperienceSerializer(data=exec)
                
                if workserializer.is_valid():
                   
                    workserializer.save()

                else:
                    print(workserializer.errors)

    return 'ok'


def refrence(id, formresponse):
    refranceDetail = RefranceContact.objects.filter(student_id=id)
    refForm = len(formresponse['ref_name'])

    for i in range(max(len(formresponse['ref_name']), len(refranceDetail))):
        print("loop")
        if i > len(refranceDetail) and i < refForm:
            print("loop11")

            RefranceContact.objects.filter(student_id=id).delete()
        else:

            exec = {'ref_name': str(formresponse['ref_name'][i]),
                    'ref_contact': str(formresponse['ref_contact'][i]),
                    'relation': str(formresponse['relation'][i]),
    

                    }
            if i < len(refranceDetail):

                refranceserializer = RefranceDetailSerializer(
                    refranceDetail[i], data=exec,partial=True)
       
            else:
                exec['student_id'] = id
                refranceserializer = RefranceDetailSerializer(data=exec)
                print(exec,"refranceserializer")
                
              
            if refranceserializer.is_valid():
                
                refranceserializer.save()

            else:
                print(refranceserializer.errors)
        
                    


             
          
    return 'ok'


def language(id, formresponse):
    languageDetail = Languages.objects.filter(student_id=id)

    for i in range(max(len(formresponse['language']), len(languageDetail))):
        print("lang iw wed we")

        if i > len(languageDetail) and i < len(formresponse['language']):
            

            Languages.objects.filter(student_id=id).delete()

        else:
                langFun = {'language': str(formresponse['language'][i])}

                if 'read_status' in formresponse:
                    if formresponse['language'][i] in formresponse['read_status']:
                        langFun['read_status'] = 1

                if 'write_status' in formresponse:

                    if formresponse['language'][i] in formresponse['write_status']:
                        langFun['write_status'] = 1

                if 'speak_status' in formresponse:
                    if formresponse['language'][i] in formresponse['speak_status']:
                        langFun['speak_status'] = 1

                if i < len(languageDetail):

                    languageSerializer = LanguageDetailSerializer(languageDetail[i],data=langFun,partial=True)
                else:
                    langFun['student_id'] = id
                    languageSerializer = LanguageDetailSerializer(data=langFun)
                 

                if languageSerializer.is_valid():
                        
                    
                        languageSerializer.save()
                else:
    
                        print(languageSerializer.errors)
    return 'ok'


def technology(id,formresponse):
      
      technologyform=Technologies.objects.filter(student_id=id)

      for i in range(max(len(formresponse['tech_name']),len(technologyform))):
                if i>len(technologyform) and i<len(formresponse['tech_name']):
                     print("if inside ie, technology")
                     Technologies.objects.filter(student_id=id).delete()
                else:
                    print("else inside ie, technology")
                     
                    exec = {'tech_name': str(formresponse['tech_name'][i])}
                    technology = formresponse['tech_name'][i]

                    if technology in formresponse:
                        exec['star'] = str(formresponse[technology][0])

                    if i<len(technologyform):
                        technoserializer = TechnologyDetailSerializer(technologyform[i],data=exec,partial=True)
                    else:
                        exec['student_id'] = id
                        technoserializer = TechnologyDetailSerializer(data=exec)
                    
                    if technoserializer.is_valid():
                    
                        technoserializer.save()
                    else:
                        print(technoserializer.errors)
      return "ok"
                         

                          
              





class BasicDetailView(APIView):

    def post(self, request):
        serializer = BasicDetailSerializer(data=request.data)

        formresponse = request.data

        if serializer.is_valid():

            data = serializer.save()
            print(data,type(data))

            for i in range(len(formresponse['course_name'])):

                exec = {
                    'course_name': str(formresponse['course_name'][i]),
                    'board_name': str(formresponse['board_name'][i]),
                    'passing_year': str(formresponse['passing_year'][i]),
                    'percentage': formresponse['percentage'][i],
                    'student_id':data.id
                }
                
                eduserializer = EducationDetailSerializer(data=exec)
                if eduserializer.is_valid():
                    # eduserializer.validated_data['student_id'] = data
                    eduserializer.save()
                else:
                    print(eduserializer.errors)

            for i in range(len(formresponse['company_name'])):
                exec = {
                    'company_name': str(formresponse['company_name'][i]),
                    'designation': str(formresponse['designation'][i]),
                    'start_date': str(formresponse['start_date'][i]),
                    'end_date': str(formresponse['end_date'][i]),
                     'student_id':data.id
                }
                print(exec)
                workserializer = WorkExperienceSerializer(data=exec)

                if workserializer.is_valid():
                    # workserializer.validated_data['student_id'] = data
                    workserializer.save()

            for i in range(len(formresponse['language'])):

                langFun = {'language': str(formresponse['language'][i])}

                if 'read_status' in formresponse:
                    if formresponse['language'][i] in formresponse['read_status']:
                        langFun['read_status'] = 1

                if 'write_status' in formresponse:

                    if formresponse['language'][i] in formresponse['write_status']:
                        langFun['write_status'] = 1

                if 'speak_status' in formresponse:
                    if formresponse['language'][i] in formresponse['speak_status']:
                        langFun['speak_status'] = 1

                print(langFun, "---------------------------------------------")
                langFun['student_id']=data.id
                languageSerializer = LanguageDetailSerializer(data=langFun)

                if languageSerializer.is_valid():
                    # languageSerializer.validated_data['student_id'] = data
                    languageSerializer.save()
                else:
                    print(languageSerializer.errors)

            for i in range(len(formresponse['tech_name'])):
                exec = {'tech_name': str(formresponse['tech_name'][i])}
                technology = formresponse['tech_name'][i]

                if technology in formresponse:
                    exec['star'] = str(formresponse[technology][0])

                exec['student_id']=data.id
                technoserializer = TechnologyDetailSerializer(data=exec)

                if technoserializer.is_valid():
                    # technoserializer.validated_data['student_id'] = data
                    technoserializer.save()

            for i in range(len(formresponse['ref_name'])):
                exec = {'ref_name': str(formresponse['ref_name'][i]),
                        'ref_contact': str(formresponse['ref_contact'][i]),
                        'relation': str(formresponse['relation'][i]),
                         'student_id':data.id

                        }
                refranceserializer = RefranceDetailSerializer(data=exec)

                if refranceserializer.is_valid():
                    # refranceserializer.validated_data['student_id'] = data
                    refranceserializer.save()

                else:
                    print(refranceserializer.errors)

            preferenceserializer = PreferenceDetailSerializer(
                data=request.data)
            if preferenceserializer.is_valid():
                preferenceserializer.validated_data['student_id'] = data
                preferenceserializer.save()

                return Response({'msg': "Form Submitted successfully"}, status=status.HTTP_201_CREATED)

            else:
                return Response({
                    'education': eduserializer.errors,
                    'work': workserializer.errors,
                    'language': languageSerializer.errors,
                    'technology': technoserializer.errors,
                    'refrance': refranceserializer.errors,
                    'preference': preferenceserializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        if pk is not None:

            stu = get_or_none(BasicDetails, id=pk)

            if stu is not None:
                serializer = BasicDetailSerializer(stu)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response({'msg': f"Data for id={pk} doesn't exists "}, status=status.HTTP_204_NO_CONTENT)

        stu_data = BasicDetails.objects.all()
        serializer = BasicDetailSerializer(stu_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        formResponse = request.data
        basicData=get_or_none(BasicDetails,id=pk)
        serializer=BasicDetailSerializer(basicData,formResponse,partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        
        edu1 = education(pk, formResponse)
        work1 = work(pk, formResponse)
        refrence1=refrence(pk, formResponse)
        language1=language(pk, formResponse)
        technology1=technology(pk, formResponse)
        preferenceData=get_or_none(Preference,student_id=pk)
        prefSerializer=PreferenceDetailSerializer(preferenceData,data=formResponse,partial=True)
        if prefSerializer.is_valid():
                 prefSerializer.validated_data['student_id']:pk
                 prefSerializer.save()
                 pref="ok"
        

        if edu1 == 'ok' and work1 == 'ok' and refrence1 == 'ok' and language1 == 'ok' and technology1 == 'ok' and pref == 'ok' :
            return Response({'success': "update"})
        return Response({'Failure': "fail"})
    

    def delete(self,request,pk=None):
        basicdata=get_or_none(BasicDetails,id=pk)
        if basicdata is  not None:
            basicdata.delete()
            return Response({'msg':'Data deleted successfully'},status=status.HTTP_200_OK)
        return Response({'msg':f"Data for id={pk} is not found"},status=status.HTTP_404_NOT_FOUND)
    

class DataView(APIView):

    def get(self, request,pk):
        basicdata=get_or_none(BasicDetails,id=pk)
        if basicdata is  not None:
            educationdata=EducationDetail.objects.filter(student_id=pk)
            workdata=WorkExperiences.objects.filter(student_id=pk)
            refdata=RefranceContact.objects.filter(student_id=pk)
            langdata=Languages.objects.filter(student_id=pk)
            techdata=Technologies.objects.filter(student_id=pk)
            prefdata=Preference.objects.filter(student_id=pk)

            basicSerializer=BasicDetailSerializer(basicdata)
            eduSerializer=EducationDetailSerializer(educationdata,many=True)
            workSerializer=WorkExperienceSerializer(workdata,many=True)
            refSerializer=RefranceDetailSerializer(refdata,many=True)
            lanSerializer=LanguageDetailSerializer(langdata,many=True)
            techSerializer=TechnologyDetailSerializer(techdata,many=True)
            prefSerializer=PreferenceDetailSerializer(prefdata,many=True)

            return Response({'Data':{
                'basic':basicSerializer.data,
                'education':eduSerializer.data,
                'work':workSerializer.data,
                'ref':refSerializer.data,
                'lang':lanSerializer.data,
                'techname':techSerializer.data,
                'pref':prefSerializer.data
            }},status=status.HTTP_200_OK)
        else:
             return Response({'msg':f"Data for id={pk} is not found"},status=status.HTTP_404_NOT_FOUND)




class getState(APIView):
    def get(self,request):
        stateData=StateMaster.objects.all()

        seralizer=StateMasterSerializer(stateData,many=True)
        return Response(seralizer.data,status=status.HTTP_200_OK)


class getCity(APIView):
    def get(self,request,pk):
        print(pk,"id")
        stateId=get_or_none(StateMaster,state_name=pk)
        print(stateId)

        if stateId is not  None:
            cityData=CityMaster.objects.filter(stateID_id=stateId)
            serializer=CityMasterSerializer(cityData,many=True)

            return Response(serializer.data,status=status.HTTP_200_OK)
    

class GETDATA(APIView):

    def get(self, request,pk):
        selectedData=get_or_none(SelectMaster,select_name=pk)
     
        serializer=SelectMasterSerializer(selectedData)
     
        optiondata=OptionMaster.objects.filter(selectId_id=serializer.data['id'])
     
        optionSerializer=OptionMasterSerializer(optiondata,many=True)

        return Response(optionSerializer.data,status=status.HTTP_200_OK)


