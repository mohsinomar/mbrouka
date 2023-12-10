from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import*
from django.contrib import messages
from app_auth.views import register

def home(request):
    title = 'Station mabrouka'
    users= User.objects.values()   
    useres= User.objects.count()
    utilisateurs=Userpassword.objects.all()
    context={'title': title,
             'users':users,
             'useres':useres,
             'utilisateurs':utilisateurs,
         }
    return render(request,'home.html',context )


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['domaine', 'Parcelle', 'Varieté','Secteur']   
    success_url = reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['domaine', 'Parcelle', 'Varieté','Secteur']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

###"""""""""""""#""""""""""##"########
class FertiList(LoginRequiredMixin, ListView):
    model =Fertigation
    context_object_name = 'fertigations'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertigations'] = context['fertigations'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertigations'] = context['fertigations'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class FertiCreate(LoginRequiredMixin, CreateView):
    model =Fertigation


    fields = ['domaine', 'date', 'ammonitrate','map','sulfate','calcium','case2', 'organique','qté_eau','dure_irr']
    
    success_url = reverse_lazy('fertigations')

    def form_valid(self, form1):
        form1.instance.user = self.request.user
        return super(FertiCreate, self).form_valid(form1)

class FertiUpdate(LoginRequiredMixin, UpdateView):
    model =Fertigation


    fields = [ 'domaine','date', 'ammonitrate','sulfate','calcium', 'case1','case2', 'organique','qté_eau','dure_irr']
    success_url = reverse_lazy('fertigations')


class FertiDelete(LoginRequiredMixin, DeleteView):
    model =Fertigation


    context_object_name = 'fertigation'
    success_url = reverse_lazy('fertigations')

###"""""""""""""#""""""""""##"########

class FertiAmmStockList(LoginRequiredMixin, ListView):    
    model =Amon
    ordering = 'id'
    context_object_name = 'fertiAmmstocks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertiAmmstocks'] = context['fertiAmmstocks'].filter(user=self.request.user)       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertiAmmstocks'] = context['fertiAmmstocks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context

class FertiAmmStockCreate(LoginRequiredMixin, CreateView):
    
    model =Amon
    
    fields = [ 'domaine','date', 's_initial','entree','sortie', 'destination','s_restant']    
    success_url = reverse_lazy('fertiAmmstocks')
    def form_valid(self, Ammform):
        Ammform.instance.user = self.request.user
        return super(FertiAmmStockCreate, self).form_valid(Ammform)
class FertiAmmStockUpdate(LoginRequiredMixin, UpdateView):
    model =Amon
    fields = [ 'domaine','date', 's_initial','entree','sortie', 'destination','s_restant']
    success_url = reverse_lazy('fertiAmmstocks')

class FertiAmmStockDelete(LoginRequiredMixin, DeleteView):
    model =Amon
    context_object_name = 'fertiAmmstock'
    success_url = reverse_lazy('fertiAmmstocks')
################################################################################################

class FertiMapStockList(LoginRequiredMixin, ListView):
              
    model =Map
    ordering = 'id'
    context_object_name = 'fertiMapstocks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertiMapstocks'] = context['fertiMapstocks'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertiMapstocks'] = context['fertiMapstocks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class FertiMapStockCreate(LoginRequiredMixin, CreateView):
    model =Map


    fields = [ 'domaine','date', 's_initial','entree','sortie', 'destination','s_restant']
    
    success_url = reverse_lazy('fertiMapstocks')

    def form_valid(self, Mapform):
        Mapform.instance.user = self.request.user
        return super(FertiMapStockCreate, self).form_valid(Mapform)

class FertiMapStockUpdate(LoginRequiredMixin, UpdateView):
    model =Map


    fields = [ 'domaine','date', 's_initial','entree','sortie', 'destination','s_restant']
    success_url = reverse_lazy('fertiMapstocks')


class FertiMapStockDelete(LoginRequiredMixin, DeleteView):
    model =Map


    context_object_name = 'fertiMapstock'
    success_url = reverse_lazy('fertiMapstocks')
####################################################################################
class FertiSulfateStockList(LoginRequiredMixin, ListView):
              
    model =Sulf
    ordering = 'id'
    context_object_name = 'fertiSulfatestocks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertiSulfatestocks'] = context['fertiSulfatestocks'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertiSulfatestocks'] = context['fertiSulfatestocks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class FertiSulfateStockCreate(LoginRequiredMixin, CreateView):
    model =Sulf


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    
    success_url = reverse_lazy('fertiSulfatestocks')

    def form_valid(self, Sulfateform):
        Sulfateform.instance.user = self.request.user
        return super(FertiSulfateStockCreate, self).form_valid(Sulfateform)

class FertiSulfateStockUpdate(LoginRequiredMixin, UpdateView):
    model =Sulf


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    success_url = reverse_lazy('fertiSulfatestocks')


class FertiSulfateStockDelete(LoginRequiredMixin, DeleteView):
    model =Sulf


    context_object_name = 'fertiSulfatestock'
    success_url = reverse_lazy('fertiSulfatestocks')
####################################################################################
class FertiCalcStockList(LoginRequiredMixin, ListView):
              
    model =Calc
    ordering = 'id'
    context_object_name = 'fertiCalcstocks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertiCalcstocks'] = context['fertiCalcstocks'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertiCalcstocks'] = context['fertiCalcstocks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class FertiCalcStockCreate(LoginRequiredMixin, CreateView):
    model =Calc


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    
    success_url = reverse_lazy('fertiCalcstocks')

    def form_valid(self, Calcform):
        Calcform.instance.user = self.request.user
        return super(FertiCalcStockCreate, self).form_valid(Calcform)

class FertiCalcStockUpdate(LoginRequiredMixin, UpdateView):
    model =Calc


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    success_url = reverse_lazy('fertiCalcstocks')


class FertiCalcStockDelete(LoginRequiredMixin, DeleteView):
    model =Calc


    context_object_name = 'fertiCalcstock'
    success_url = reverse_lazy('fertiCalcstocks')
####################################################################################
class FertiUreeStockList(LoginRequiredMixin, ListView):
              
    model =Uree
    ordering = 'id'
    context_object_name = 'fertiUreestocks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertiUreestocks'] = context['fertiUreestocks'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertiUreestocks'] = context['fertiUreestocks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class FertiUreeStockCreate(LoginRequiredMixin, CreateView):
    model =Uree


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    
    success_url = reverse_lazy('fertiUreestocks')

    def form_valid(self, Ureeform):
        Ureeform.instance.user = self.request.user
        return super(FertiUreeStockCreate, self).form_valid(Ureeform)

class FertiUreeStockUpdate(LoginRequiredMixin, UpdateView):
    model =Uree


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    success_url = reverse_lazy('fertiUreestocks')


class FertiUreeStockDelete(LoginRequiredMixin, DeleteView):
    model =Uree


    context_object_name = 'fertiUreestock'
    success_url = reverse_lazy('fertiUreestocks')
####################################################################################
class FertiNitrStockList(LoginRequiredMixin, ListView):
              
    model =Nitr
    ordering = 'id'
    context_object_name = 'fertiNitrstocks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fertiNitrstocks'] = context['fertiNitrstocks'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['fertiNitrstocks'] = context['fertiNitrstocks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class FertiNitrStockCreate(LoginRequiredMixin, CreateView):
    model =Nitr


    fields = ['domaine', 'date', 's_initial','entree','sortie', 'destination','s_restant']
    
    success_url = reverse_lazy('fertiNitrstocks')

    def form_valid(self, Nitrform):
        Nitrform.instance.user = self.request.user
        return super(FertiNitrStockCreate, self).form_valid(Nitrform)

class FertiNitrStockUpdate(LoginRequiredMixin, UpdateView):
    model =Nitr


    fields = [ 'domaine','date', 's_initial','entree','sortie', 'destination','s_restant']
    success_url = reverse_lazy('fertiNitrstocks')


class FertiNitrStockDelete(LoginRequiredMixin, DeleteView):
    model =Nitr


    context_object_name = 'fertiNitrstock'
    success_url = reverse_lazy('fertiNitrstocks')



class PhytoList(LoginRequiredMixin, ListView):
    model =Phytos
    ordering = 'id'
    context_object_name = 'phytos'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['phytos'] = context['phytos'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['phytos'] = context['phytos'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context




class PhytoCreate(LoginRequiredMixin, CreateView):
    model =Phytos


    fields = ['domaine','date','varieté','parcelle','horaire','produit','matiére_avtive','ennemi_ciblé','qté_produits','outiel','ouvries','temperature','météo']

    
    success_url = reverse_lazy('phytos')

    def form_valid(self, form2):
        form2.instance.user = self.request.user
        return super(PhytoCreate, self).form_valid(form2)

class PhytoUpdate(LoginRequiredMixin, UpdateView):
    model =Phytos


    fields = ['domaine','date','varieté','parcelle','horaire','produit','matiére_avtive','ennemi_ciblé','qté_produits','outiel','ouvries','temperature','météo']
    success_url = reverse_lazy('phytos')


class PhytoDelete(LoginRequiredMixin, DeleteView):
    model =Phytos


    context_object_name = 'phyto'
    success_url = reverse_lazy('phytos')


class OrderList(LoginRequiredMixin, ListView):
    model =OrderEng
    ordering = 'id'
    context_object_name = 'orderengs'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['orderengs'] = context['orderengs'].filter(user=self.request.user)
       
        search_input = self.request.GET.get('Chercher-sujet') or ''
        if search_input:
            context['orderengs'] = context['orderengs'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context



class OrderCreate(LoginRequiredMixin, CreateView):
    model =OrderEng
    fields = ['producteur', 'date1','date2', 'amm','map','sulf','nitr','calc']    
    success_url = reverse_lazy('orderengs')
    def form_valid(self, formorder):
        formorder.instance.user = self.request.user
        return super(OrderCreate, self).form_valid(formorder)

class OrderUpdate(LoginRequiredMixin, UpdateView):
    model =OrderEng
    fields = ['producteur', 'date1','date2', 'amm','map','sulf','nitr','calc']
    success_url = reverse_lazy('orderengs')

class OrderDelete(LoginRequiredMixin, DeleteView):
    model =OrderEng
    context_object_name = 'ordereng'
    success_url = reverse_lazy('orderengs')