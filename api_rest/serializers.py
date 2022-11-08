from rest_framework import serializers
from .models import Productos, Answer, Notificaciones, Question, User,UserProduct,UserSession

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('id_producto','nombre','precio','descripcion','img_src')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id_answer','id_quest','id_user','answer','cuerpo','fecha')
        
class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = ('id_notificaciones','id_user','mensaje','title','state','remitente')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id_quest','id_user','question','type','id_producto','cuerpo','fecha')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id_user','nombre','apellidos','telefono','username','password')
        
class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('id_user_product','id_producto','id_user','license_type','license_cad')
        
class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ('id_user_session','id_user','state','last_login','device')