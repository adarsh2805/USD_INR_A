from django.urls import path
from GSDAPP import views
urlpatterns = [
    path('',views.index,name = 'index'),
]