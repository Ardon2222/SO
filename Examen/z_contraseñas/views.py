#Todos los imports y funciones necesarias 
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Gestor 

#En donde podremos ver desde el propio navegador los usuarios y contraseñas
'''
@csrf_exempt
def mostrar(request):
    response = serializers.serialize('json', Gestor.objects.all())
    return JsonResponse(response, safe=False)

#Con la url que enviaremos un post con los parametros usuario y contraseña para crear-
#- un nuevo usuario (La DI tambien llamada "pk" se pone automaticamente)

@csrf_exempt
def nueva(request):
    my_json = json.loads(request.body.decode("UTF8").replace("*", "*"))
    usuario = my_json['usuario']
    contra = my_json['contra']
    entrada = Gestor.objects.create(usuario=usuario, contra=contra)
    entrada.save()
    response = {
        "respuesta": "Nuevo usuario creado"
    }
    return JsonResponse(response)

#Con la url que enviaremos un post con los parametros usuario_id que es el pk, usuario-
#- y contraseña para editar el nombre y contraseña del usuario con el id proporcionado

@csrf_exempt
def editar(request):
    my_json = json.loads(request.body.decode("UTF8"))
    usuario_id = my_json.get('usuario_id')
    gestor = Gestor.objects.filter(pk=usuario_id).first()

    if gestor is not None:
        gestor.usuario = my_json['usuario']
        gestor.contra = my_json['contra']
        gestor.save()
        response = {
            "respuesta": f"Informacion editada del {usuario_id}"
        }
        return JsonResponse(response)
    else:
        error_response = {
            "error": "ID de usuario no encontrada"
        }
        return JsonResponse(error_response, status=400)

#Con la url que enviaremos un post con el parametro usuario_id que es el pk-
#- se eliminara ese usuario (En caso de poner "all" se eliminaran todos)

@csrf_exempt
def eliminar(request):
    my_json = json.loads(request.body.decode("UTF8"))
    usuario_id = my_json.get('usuario_id')

    if usuario_id is not None or gestor is not None:
        usuario_id=str(usuario_id)
        if usuario_id.lower() == 'all':
            Gestor.objects.all().delete()
            response = {
                "respuesta": "Todos los usuarios eliminados exitosamente"
            }
            return JsonResponse(response)
        else:
            usuario_id=int(usuario_id)
            gestor = Gestor.objects.filter(pk=usuario_id).first()
            gestor.delete()
            response = {
                "respuesta": f"Usuario con ID {usuario_id} eliminado exitosamente"
            }
            return JsonResponse(response)
    else:
        error_response = {
            "error": "ID de usuario encontrada"
        }
        return JsonResponse(error_response, status=400)
'''
    #----------------EXAMEN--------------
@csrf_exempt
def get(request):
    response = serializers.serialize('json', Gestor.objects.all())
    return JsonResponse(response, safe=False)

#Con la url que enviaremos un post con los parametros usuario y contraseña para crear-
#- un nuevo usuario (La DI tambien llamada "pk" se pone automaticamente)

@csrf_exempt
def introducir(request):
    my_json = json.loads(request.body.decode("UTF8").replace("*", "*"))
    dni = my_json['dni']
    contra = my_json['contra']
    entrada = Gestor.objects.create(dni=dni, contra=contra)
    entrada.save()
    response = {
        "respuesta": "Nuevo usuario creado"
    }
    return JsonResponse(response)

@csrf_exempt
def editar(request):
    my_json = json.loads(request.body.decode("UTF8"))
    usuario_id = my_json.get('usuario_id')
    gestor = Gestor.objects.filter(pk=usuario_id).first()

    if gestor is not None:
        gestor.contra = my_json['contra']
        gestor.save()
        response = {
            "respuesta": f"Informacion editada del {usuario_id}"
        }
        return JsonResponse(response)
    else:
        error_response = {
            "error": "ID de usuario no encontrada"
        }
        return JsonResponse(error_response, status=400)

#Con la url que enviaremos un post con los parametros usuario_id que es el pk, usuario-
#- y contraseña para editar el nombre y contraseña del usuario con el id proporcionado
