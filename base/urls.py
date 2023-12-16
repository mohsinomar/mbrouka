from django.urls import path
from .views import*
from django.contrib.auth.views import LogoutView
from base.views import*
from app_auth.views import*

urlpatterns = [
    path('login/',login_blog,name='login'),
    path('register/',register,name='register'),  
    path('logout/', LogoutView.as_view(next_page ='login'), name='logout'),
    path('', home, name='home'),
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-supprime/<int:pk>/', TaskDelete.as_view(), name='task-supprime'),
    ###########################################################################
    path('fertigations', FertiList.as_view(), name='fertigations'),
    path('fertigation-create/', FertiCreate.as_view(), name='fertigation-create'),
    path('fertigation-update/<int:pk>/', FertiUpdate.as_view(), name='fertigation-update'),
    path('fertigation-supprime/<int:pk>/', FertiDelete.as_view(), name='fertigation-supprime'),
    ###########################################################################
    path('fertiAmmstocks', FertiAmmStockList.as_view(), name='fertiAmmstocks'),  
    path('fertiAmmstock-create/', FertiAmmStockCreate.as_view(), name='fertiAmmstock-create'),
    path('fertiAmmstock-update/<int:pk>/', FertiAmmStockUpdate.as_view(), name='fertiAmmstock-update'),
    path('fertiAmmstock-supprime/<int:pk>/', FertiAmmStockDelete.as_view(), name='fertiAmmstock-supprime'),
    ########################################################################################################
    path('fertiMapstocks', FertiMapStockList.as_view(), name='fertiMapstocks'),
    path('fertiMapstock-create/', FertiMapStockCreate.as_view(), name='fertiMapstock-create'),
    path('fertiMapstock-update/<int:pk>/', FertiMapStockUpdate.as_view(), name='fertiMapstock-update'),
    path('fertiMapstock-supprime/<int:pk>/', FertiMapStockDelete.as_view(), name='fertiMapstock-supprime'),
     ########################################################################################################
    path('fertiCalcstocks', FertiCalcStockList.as_view(), name='fertiCalcstocks'),
    path('fertiCalcstock-create/', FertiCalcStockCreate.as_view(), name='fertiCalcstock-create'),
    path('fertiCalcstock-update/<int:pk>/', FertiCalcStockUpdate.as_view(), name='fertiCalcstock-update'),
    path('fertiCalcstock-supprime/<int:pk>/', FertiCalcStockDelete.as_view(), name='fertiCalcstock-supprime'),
    ###########################################################################################################
    path('fertiSulfatestocks', FertiSulfateStockList.as_view(), name='fertiSulfatestocks'),
    path('fertiSulfatestock-create/', FertiSulfateStockCreate.as_view(), name='fertiSulfatestock-create'),
    path('fertiSulfatestock-update/<int:pk>/', FertiSulfateStockUpdate.as_view(), name='fertiSulfatestock-update'),
    path('fertiSulfatestock-supprime/<int:pk>/', FertiSulfateStockDelete.as_view(), name='fertiSulfatestock-supprime'),   
    ###########################################################################################################
    path('fertiUreestocks', FertiUreeStockList.as_view(), name='fertiUreestocks'),
    path('fertiUreestock-create/', FertiUreeStockCreate.as_view(), name='fertiUreestock-create'),
    path('fertiUreestock-update/<int:pk>/', FertiUreeStockUpdate.as_view(), name='fertiUreestock-update'),
    path('fertiUreestock-supprime/<int:pk>/', FertiUreeStockDelete.as_view(), name='fertiUreestock-supprime'),  
    ###########################################################################################################
    path('fertiNitrstocks', FertiNitrStockList.as_view(), name='fertiNitrstocks'),
    path('fertiNitrstock-create/', FertiNitrStockCreate.as_view(), name='fertiNitrstock-create'),
    path('fertiNitrstock-update/<int:pk>/', FertiNitrStockUpdate.as_view(), name='fertiNitrstock-update'),
    path('fertiNitrstock-supprime/<int:pk>/', FertiNitrStockDelete.as_view(), name='fertiNitrstock-supprime'), 
    ##############################################################################################################
    path('phytos', PhytoList.as_view(), name='phytos'),
    path('phyto-create/', PhytoCreate.as_view(), name='phyto-create'),
    path('phyto-update/<int:pk>/', PhytoUpdate.as_view(), name='phyto-update'),
    path('phyto-supprime/<int:pk>/', PhytoDelete.as_view(), name='phyto-supprime'),   
    ################################################################################################################
    path('orderengs', OrderList.as_view(), name='orderengs'),
    path('ordereng-create/', OrderCreate.as_view(), name='ordereng-create'),
    path('ordereng-update/<int:pk>/',OrderUpdate.as_view(), name='ordereng-update'),
    path('ordereng-supprime/<int:pk>/', OrderDelete.as_view(), name='ordereng-supprime'),
    ####################################################################################
    path('export_ammon',export_ammon,name='export_ammon'),
    

   
]