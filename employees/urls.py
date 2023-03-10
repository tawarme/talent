from django.urls import path
from rest_framework.routers import DefaultRouter
#from employees.views import EmployeeView, EmployeeCreateView
from employees.views import EmployeeViewSet


router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')

urlpatterns = router.urls
