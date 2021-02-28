
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('login', views.login),
    path('loginshalgah',views.shalgah),
    path('zasah',views.zasah),
    path('zasahshalgah',views.zshalgah),
    path('ustgah',views.ustgah),
    path('insert',views.insert)
]
