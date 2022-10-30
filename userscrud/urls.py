from rest_framework import routers
from userscrud.api import UserCrudViewSet

router=routers.DefaultRouter()

router.register(
    'api/cruduni2', 
    UserCrudViewSet, 
    'cruduni2'
    )

urlpatterns = router.urls
