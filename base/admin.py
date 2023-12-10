
from django.contrib import admin
from .models import*
from import_export.admin import ImportExportModelAdmin
admin.site.register(Task)
admin.site.register(Fertigation)
admin.site.register(Fertile)
admin.site.register(Userpassword)



@admin.register(Amon,Map,Sulf,Calc,Nitr,Uree,Kimia)
class ViewAdmin(ImportExportModelAdmin):
          pass



