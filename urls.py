from django.urls import path
from . import views
#----------------EXAMEN--------------
urlpatterns = [
    path('introducir/', views.introducir),
    path('get/', views.get),
    path('editar/', views.editar),
#Nuevo para eliminar
    path('eliminar/', views.eliminar),
]
