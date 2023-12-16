from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadFileForm
from django.contrib import messages
from django.urls import path
import os





def upload_and_display_files(request):
    files = UploadedFile.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('hi')
            for file in request.FILES.getlist('files'):
                exists= UploadedFile.objects.filter(file=file).exists() 
               
                if exists:
                     data=1
                else:
                     data=0        
                     UploadedFile.objects.create(file=file).save()
            if data==1:
                          messages.error(request,'Le fichier existe déja!.')
            else:
                          messages.success(request,'Le fichier a été télécharger avec succes.')
            return redirect('upload_and_display')
    else:
                  form = UploadFileForm()

    return render(request, 'upload_and_display.html', {'form': form,'files':files})

def delete_matrix(request, pk):
               
       files = UploadedFile.objects.get(pk=pk)
       files.delete()
       os.remove(files.file.path)
       messages.success(request,'fichier supprrimé avec succes')
       return redirect('/upload_and_display')
    
