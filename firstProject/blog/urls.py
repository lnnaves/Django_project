from django.urls import path 
from blog import views 

#criando arquivo de urls do blog   
# http://127.0.0.1:8000/blog/variacoesBlog 

#ja comeca no blog/
urlpatterns = [
    path("", views.blog),
]
