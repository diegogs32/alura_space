from django.urls import path
from usuarios.views import login, cadastro, logout


urlpatterns = [
    path('login',login, name='login'),
    path('casdatro',cadastro, name='cadastro' ), 
    path('logout', logout, name='logout'),
    

]