from django.contrib import admin
from .models import BasicDetails,StateMaster,CityMaster,EducationDetail,WorkExperiences,Languages,Technologies,RefranceContact,Preference
# Register your models here.

from django.contrib.auth.models import Group




admin.site.unregister(Group)

class BasicDetailsAdmin(admin.ModelAdmin):
    list_key=['firstname','lastname','designation','address1','address2','email','city','state','gender',' zipcode','relation_status','dob']
    list_filter=['firstname','lastname','designation1']
    list_display=['firstname','lastname','designation1','email']
    list_editable=['email']
admin.site.register(BasicDetails,BasicDetailsAdmin)


class StateAdmin(admin.ModelAdmin):
    list_key=['State_name']
    search_fields=['state_name']

admin.site.register(StateMaster,StateAdmin)



class CityAdmin(admin.ModelAdmin):
    list_key=['city_name','StateId']
    # title=['city_name','stateId']

admin.site.register(CityMaster,CityAdmin)



class AcademicAdmin(admin.ModelAdmin):
    list_key=['student_id','course_name','board_name','passing_year','percentage']

admin.site.register(EducationDetail,AcademicAdmin)



class WorkAdmin(admin.ModelAdmin):
    list_key=['student_id','company_name','designation','start_date','end_date']

admin.site.register(WorkExperiences,WorkAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_key=['student_id','language','read_status','write_status','speak_status']

admin.site.register(Languages,LanguageAdmin)

class TechnologyAdmin(admin.ModelAdmin):
    list_key=['student_id','tech_name','star']

admin.site.register(Technologies,TechnologyAdmin)

class RefranceAdmin(admin.ModelAdmin):
    list_key=['student_id','ref_name','ref_contact','relation']

admin.site.register(RefranceContact,RefranceAdmin)


class PrefranceAdmin(admin.ModelAdmin):
    list_key=['student_id','prefered_location','expected_ctc','current_ctc','notice_period','department']

admin.site.register(Preference,PrefranceAdmin)


