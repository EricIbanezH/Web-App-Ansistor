from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpRequest
from productos import views as viewProducto
from django.contrib import messages
from session import views as viewSession
from session import formsP
from qya import views as viewQya
from qya import forms_qya

def cerrarSession(response):
    viewSession.delete(str(viewSession.user_id))
    return redirect('/')

def index(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        return render(response,'index.html',userSession_state)
    else:
        return redirect('/')

def term(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        return render(response,'terminos.html',userSession_state)
    else:
        return redirect('/')

def privacy(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        return render(response,'acuerdo.html',userSession_state)
    else:
        return redirect('/')

def about(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        return render(response,'acerca de.html',userSession_state)
    else:
        return redirect('/')

def payment(response,id_producto,periodo):
    if response.method=='GET':
        producto = viewProducto.consulta_producto_id(id_producto)
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        userSession_state.update({'user': viewSession.consulta_user_id(viewSession.user_id),'producto':producto,'periodo':periodo,'precioAnual':(int(producto['precio'])*12)-100})
        return render(response,'payment.html',userSession_state)
    else:
        return redirect('/')

def notificaciones(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        userSession_state.update({'listaNoti': viewProducto.consultaNotificacionesJson()})
        userSession_state.update({'user': viewSession.user_id})
        return render(response,'notificaciones.html',userSession_state)
    else:
        viewProducto.delete(response.POST['id_notificaciones'])
        messages.add_message(request=response,level=messages.SUCCESS, message='Notificacion eliminada')
        return redirect('/notificaciones')

def QyA(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        userSession_state.update( {'questions':viewQya.consultaQuestions(),'answers':viewQya.consultaAnswer()})
        userSession_state.update({'form':forms_qya})
        return render(response,'QyA.html',userSession_state)
    else:
        #viewSession.delete(str(viewSession.user_id))
        if response.POST['tipoPost']=='respuesta':
            if viewSession.estadoSession():
             viewQya.publicarRespuesta(response)
            else:
             return redirect('/loggin')
        else:
            if viewSession.estadoSession():
             viewQya.publicarPregunta(response)
            else:
             return redirect('/loggin')
        return redirect('/comunidad')

def perfil(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        userSession_state.update({'perfil': viewSession.consulta_user_id(viewSession.user_id)})
        return render(response,'perfil.html',userSession_state)
    else:
        if viewSession.form_update(response):
         messages.add_message(request=response,level=messages.SUCCESS, message='Actualizado con exito')
        else:
         messages.add_message(request=response,level=messages.WARNING, message='El email ya existe o datos incorrectos')
        return redirect('/perfil')

def login(request):
    if request.method=='GET':
        return render(request,'loggin.html',{'user':formsP.formLoggin_user,
                                             'pass':formsP.formLoggin_pass})
    else:
        user = request.POST.get('usuario')
        response = render(request,'loggin.html',{})
        response.set_cookie('usuario','1')
        viewSession.form_loggin(request)
        print(request.COOKIES['csrftoken'])
        if viewSession.estadoSession():
            response.set_cookie('sessionState',True)
            return redirect('/')
        else:
            return redirect('/loggin/')

def param(response, username):
    return HttpResponse("<h1>Hola %s</h1>" % username)

def productosViewHtml(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        userSession_state.update({'listaPro': viewProducto.consultajj()})
        return render(response,'productos.html',userSession_state)
    else:
        return redirect('/')

def registro(response):
    if response.method=='GET':
        userSession_state = {'statusSession':viewSession.estadoSession(),'cerraSession':formsP.formLogout}
        userSession_state.update({'form': formsP.formRegistro})
        return render(response,'registro.html',userSession_state)
    else:
        if viewSession.form_registro(response):
         return redirect('/loggin')
        else:
         return redirect('/registro')