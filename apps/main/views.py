from django.shortcuts import render

from apps.usuario.models import PerfilUsuario
from .forms import ImageForm

import face_recognition


def index(request):
    form = ImageForm()
    mensaje = None
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = PerfilUsuario.objects.get(numero_usuario=request.POST['numero_identificatorio'])
            known_image = face_recognition.load_image_file(usuario.photo)
            unknown_image = face_recognition.load_image_file(form.cleaned_data['img'])

            biden_encoding = face_recognition.face_encodings(known_image)[0]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            #print(results)
            if results[0]:
                mensaje = "Comparacion biometrica exitosa"
            else:
                mensaje = "No fue exitosa la comparacion biometrica"

    ctx = {'form': form, 'mensaje': mensaje}
    return render(request, 'main/index.html', ctx)



def solicitud(request):
    if request.POST:
        user_id = request.POST.get('user', '')
        if PerfilUsuario.objects.filter(numero_usuario=user_id).exists():
            user = PerfilUsuario.objects.get(numero_usuario=user_id)
            #aca enviamos el pedido al movil via push notification
            ctx = {'mensaje': 'Solicitud de autorizacion enviada'}
        else:
            ctx = {'mensaje': 'El numero de usuario no existe'}
        return render(request, 'main/solicitud.html', ctx)
    else:    
        return render(request, 'main/solicitud.html')