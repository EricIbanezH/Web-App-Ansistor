from rest_framework import viewsets,permissions
from .serializers import ProductoSerializer,AnswerSerializer,NotificacionesSerializer,QuestionSerializer,UserSerializer,UserProductSerializer,UserSessionSerializer
from .models import Productos, Answer, Notificaciones, Question, User,UserProduct,UserSession

class ProductosViewSets(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class AnswerViewSets(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AnswerSerializer
    
class NotificacionesViewSets(viewsets.ModelViewSet):
    queryset = Notificaciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NotificacionesSerializer

class QuestionViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionSerializer
    
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    
class UserProductViewSets(viewsets.ModelViewSet):
    queryset = UserProduct.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserProductSerializer
    
class UserSessionViewSets(viewsets.ModelViewSet):
    queryset = UserSession.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSessionSerializer