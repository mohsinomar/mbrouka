from django import forms
class DateInput(forms.DateInput):
        input_type = 'date'
        input_formats = ('%d-%m-%Y')
class Ammoform(forms.Form):

          domaine = forms.CharField(label="  Domaine  " ,widget=forms.TextInput(attrs={'class':'form-control'}))
          date = forms.DateField(widget=DateInput)
          s_initial = forms.CharField(label="  Domaine  " ,widget=forms.TextInput(attrs={'class':'form-control'}))
          entree = forms.CharField(label="  Domaine  " ,widget=forms.TextInput(attrs={'class':'form-control'}))
          sortie = forms.CharField(label="  Domaine  " ,widget=forms.TextInput(attrs={'class':'form-control'}))
          destination = forms.CharField(label="  Domaine  " ,widget=forms.TextInput(attrs={'class':'form-control'}))
          s_restant = forms.CharField(label="  Domaine  " ,widget=forms.TextInput(attrs={'class':'form-control'}))

   
       