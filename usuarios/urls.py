from django.urls import path
from usuarios.views import login, cadastro


urlpatterns = [
    path('login',login, name='login'),
    path('casdatro',cadastro, name='cadastro' ), 
    

]