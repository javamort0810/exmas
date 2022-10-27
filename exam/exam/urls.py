from app1.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("maqola/",new),
    path("add_News/",add_news),
    path("login/",login),
    path('logout/',logout_s)

]
