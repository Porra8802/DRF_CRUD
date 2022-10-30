from rest_framework import routers
from orgmatrixnumbers.api import OrgMatrixNumbersViewSet
# from orgmatrixnumbers.views import orgnum

router=routers.DefaultRouter()

router.register(
    'api/matrixnumbers', 
    OrgMatrixNumbersViewSet, 
    'matrixnumbers'
    )

urlpatterns = router.urls