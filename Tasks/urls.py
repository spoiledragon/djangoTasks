from rest_framework import routers
from .api import TasksViewSet
router=routers.DefaultRouter()

router.register('api/tasks',TasksViewSet ,'tasks')
urlpatterns = router.urls