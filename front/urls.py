from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('terminos/',views.term),
    path('acuerdo/',views.privacy),
    path('productos/',views.productosViewHtml),
    path('loggin/',views.login),
    path('perfil/',views.perfil),
    path('registro/',views.registro),
    path('notificaciones/',views.notificaciones),
    path('comunidad/',views.QyA),
    path('logout/',views.cerrarSession),
    path('payment/<str:id_producto>/<str:periodo>',views.payment),
    path('hello/<str:username>',views.param)
]
