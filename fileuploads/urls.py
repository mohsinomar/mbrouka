from django.urls import path
from . import views

urlpatterns = [

    path('upload_and_display', views.upload_and_display_files, name='upload_and_display'),

    path('supprimé_document/<int:pk>/', views.delete_matrix,),
   
]