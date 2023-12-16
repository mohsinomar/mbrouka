
from django.contrib import admin
from .models import*
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class PostResource(resources.ModelResource):
                  class Meta:
                    models=Amon
                    fields = ( 'domaine','date', 's_initial','entree','sortie', 'destination','s_restant') 
          

admin.site.register(Task)
admin.site.register(Fertigation)
admin.site.register(Fertile)
admin.site.register(Userpassword)



@admin.register(Amon,Map,Sulf,Calc,Nitr,Uree,Kimia)
class ViewAdmin(ImportExportModelAdmin):
          pass



