from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('output',views.action,name="action"),
    path('sample',views.sample,name="sample")
]
