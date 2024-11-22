from django.urls import path
from home import views 

#criando arquivo de urls da home 
# http://127.0.0.1:8000/variacoesHome 

urlpatterns = [
    path("", views.home),
]
