from django.urls import path, include
from Apps.Docente.views import index

urlpatterns = [
    path('', index),

]