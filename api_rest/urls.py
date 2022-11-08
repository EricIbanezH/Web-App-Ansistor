from rest_framework import routers
from .api import ProductosViewSets,AnswerViewSets,NotificacionesViewSets,QuestionViewSets,UserViewSets,UserProductViewSets,UserSessionViewSets

router= routers.DefaultRouter()

router.register('api/productos',ProductosViewSets, 'Productos')
router.register('api/answer',AnswerViewSets, 'Answer')
router.register('api/notificaciones',NotificacionesViewSets, 'Notificaciones')
router.register('api/question',QuestionViewSets, 'Question')
router.register('api/user',UserViewSets, 'User')
router.register('api/user-producto',UserProductViewSets, 'UserProducto')
router.register('api/user-session',UserSessionViewSets, 'Answer')

urlpatterns = router.urls
