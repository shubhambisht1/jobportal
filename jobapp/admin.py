from django.contrib import admin
from jobapp.models import delhijob,signup,feedback
class delhijobAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','email','phoneno']
class signupAdmin(admin.ModelAdmin):
    list_display=['name','email','phoneno']
class feedbackAdmin(admin.ModelAdmin):
    list_display=['name','email','feedback']
# Register your models here.
admin.site.register(delhijob,delhijobAdmin)
admin.site.register(signup,signupAdmin)
admin.site.register(feedback,feedbackAdmin)
