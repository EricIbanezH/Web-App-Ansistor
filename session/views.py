import this
from django.shortcuts import render
import requests
import json
from datetime import datetime
import socket

user_id = "null"
def max_id(url,id):
 response = requests.get(url)
 response_json = json.loads(response.text)
 values = response_json
 idCont=0
 idMAX=0
 for i in values:
     if i[id]=='':
         idCont +=1
         idMAX=idCont
     elif int(i[id])>idMAX:
         idMAX=int(i[id])
 return idMAX

def user_id_return():
    global user_id
    return str(user_id)

def consultaj_id(id):
 url= "http://127.0.0.1:8000/api/api/user-session/"+id
 response = requests.get(url)
 response_json = json.loads(response.text)
 return response_json

def consulta_user_id(id):
 url= "http://127.0.0.1:8000/api/api/user/"+str(id)
 response = requests.get(url)
 response_json = json.loads(response.text)
 return response_json

def consulta_user_active():
 global user_id
 if user_id=='':
    url= "http://127.0.0.1:8000/api/api/user/"+'0'
 else:
     url= "http://127.0.0.1:8000/api/api/user/"+str(user_id)
 response = requests.get(url)
 response_json = json.loads(response.text)
 return response_json

def consultaj():
 url= "http://127.0.0.1:8000/api/api/user-session/"
 response = requests.get(url)
 response_json = json.loads(response.text)
 return response_json

def consulta_users():
 url= "http://127.0.0.1:8000/api/api/user/"
 response = requests.get(url)
 response_json = json.loads(response.text)
 return response_json

def consultajj():
 nombre = consultaj()
 return nombre

def estadoSession():
    users = consultajj()
    for i in users:
        if i['state'] == 'login' :
            global user_id
            user_id = i['id_user']
            return True
    return False

def delete(id):    
 url= "http://127.0.0.1:8000/api/api/user-session/"
 url += str(max_id(url,'id_user_session'))
 response = requests.delete(url)
 return response

def registro_userSession(id_user):
 last_login = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
 device=socket.gethostname()
 url= "http://127.0.0.1:8000/api/api/user-session/"         
 payload = {'id_user_session':max_id(url,'id_user_session')+1,
            'id_user':id_user,
            'state':'login',
            'last_login':last_login,
            'device':device}
 requests.post(url,json=payload)

def form_loggin(request):
    #print('usuario es:' + request.POST['usuario'])
    #print('pass es:' + request.POST['password'])
    users = consulta_users()
    for i in users:
        if i['username'] == request.POST['usuario'] and i['password']==request.POST['password']:
            global user_id
            user_id = i['id_user']
            print('inicio de sesion exitoso')
            registro_userSession(user_id)

def registro_user(request):
 url= "http://127.0.0.1:8000/api/api/user/"        
 payload = {'id_user':max_id(url,'id_user')+1,
            'nombre':request.POST['nombre'],
            'apellidos':request.POST['apellido'],
            'telefono':request.POST['telefono'],
            'username':request.POST['email'],
            'password':request.POST['password']}
 requests.post(url,json=payload)

def put_user(request):
 url2= "http://127.0.0.1:8000/api/api/user-session/"
 url= "http://127.0.0.1:8000/api/api/user/" + str(max_id(url2,'id_user'))+'/'    
 payload = {
            'nombre':request.POST['nombre'],
            'apellidos':request.POST['apellido'],
            'telefono':request.POST['telefono'],
            'username':request.POST['email']}
 print(payload)
 requests.patch(url,json=payload)

def form_registro(request):
    users = consulta_users()
    for i in users:
        if i['username']==request.POST['email']:
         print('Ya existe una cuenta regritrada con este correo')
         return False
    registro_user(request)
    return True

def form_update(request):
    users = consulta_users()
    for i in users:
        if i['username']==request.POST['email']:
         print('Ya existe una cuenta registrada con este correo')
         return False
    put_user(request)
    return True