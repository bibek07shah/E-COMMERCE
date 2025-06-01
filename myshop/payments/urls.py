from django.urls import path
from .views import *

urlpatterns = [
    path('initkhalti/<int:id>/', initkhalti, name='initkhalti'), 
    path('verifyKhalti/', verifyKhalti, name='verifyKhalti'),
    

]
