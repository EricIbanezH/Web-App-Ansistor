from datetime import datetime
from django.shortcuts import render
import requests
import json
from api_rest import models
from session.views import user_id

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

def consultaUser():
    url = 'http://127.0.0.1:8000/api/api/user/'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json

def consultaUser_id(id):
    url = 'http://127.0.0.1:8000/api/api/user/'+str(id)
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json

def consultaQuestion_id(id):
    url = 'http://127.0.0.1:8000/api/api/question/'+str(id)
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json

def consultaProductos():
    url = 'http://127.0.0.1:8000/api/api/productos/'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json

def consultaQuestions():
    url = 'http://127.0.0.1:8000/api/api/question/'
    users = consultaUser()
    productos = consultaProductos()
    count=0
    nombre = ''
    producto = ''
    response = requests.get(url)
    response_json = json.loads(response.text)
    for i in response_json:
     for j in users:
         if i['id_user'] == j['id_user']:
             nombre = j['username']
             break
     for h in productos:
         if i['id_producto'] == h['id_producto']:
             producto = h['nombre']
             break
     response_json[count].update({'username':nombre,'producto':producto})
     count +=1
    return response_json

def consultaAnswer():
    url = 'http://127.0.0.1:8000/api/api/answer/'
    users = consultaUser()
    count=0
    nombre = ''
    response = requests.get(url)
    response_json = json.loads(response.text)
    for i in response_json:
     for j in users:
         if i['id_user'] == j['id_user']:
             nombre = j['username']
             break
     response_json[count].update({'username':nombre})
     count +=1
    return response_json

def listaproductos():
    productos = models.Productos.objects.all()
    lista=[]
    for i in productos:
        lista.append((i.id_producto,i.nombre))
    return lista

def publicarNotificacion(response):
    url = 'http://127.0.0.1:8000/api/api/notificaciones/'
    url2= 'http://127.0.0.1:8000/api/api/user-session/'
    payload = {'id_notificaciones':max_id(url,'id_notificaciones')+1,
            'id_user':consultaQuestion_id(response.POST['id_quest'])['id_user'],
            'mensaje':'el usuario '+ consultaUser_id(max_id(url2,'id_user'))['username'] + ' a respondido a tu pregunta',
            'title':'Han respondido a tu pregunta',
            'state':'nonread',
            'remitente': consultaUser_id(max_id(url2,'id_user'))['username']}
    print(payload)
    requests.post(url,json=payload)

def publicarPregunta(response):
    fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    url = 'http://127.0.0.1:8000/api/api/question/'
    url2= 'http://127.0.0.1:8000/api/api/user-session/'
    payload = {'id_quest':max_id(url,'id_quest')+1,
            'id_user':max_id(url2,'id_user'),
            'question':response.POST['title'],
            'type':response.POST['tipo'],
            'id_producto':response.POST['producto'],
            'cuerpo':response.POST['cuerpo'],
            'fecha': fecha}
    print(payload)
    requests.post(url,json=payload)

def publicarRespuesta(response):
    fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    url = 'http://127.0.0.1:8000/api/api/answer/'
    url2= 'http://127.0.0.1:8000/api/api/user-session/'
    payload = {'id_answer':max_id(url,'id_answer')+1,
            'id_quest':response.POST['id_quest'],
            'id_user':max_id(url2,'id_user'),
            'answer':response.POST['title'],
            'cuerpo':response.POST['cuerpo'],
            'fecha': fecha}
    publicarNotificacion(response)
    requests.post(url,json=payload)