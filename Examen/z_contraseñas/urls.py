from django.urls import path
from . import views

'''
urlpatterns = [
    path('nueva/', views.nueva),
    path('mostrar/', views.mostrar),
    path('eliminar/', views.eliminar),
    path('editar/', views.editar),
]
'''
#----------------EXAMEN--------------
urlpatterns = [
    path('introducir/', views.introducir),
    path('get/', views.get),
    path('editar/', views.editar),
]