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
