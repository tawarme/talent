from django.urls import path
from rest_framework.routers import DefaultRouter
#from employees.views import EmployeeView, EmployeeCreateView
from employees.views import EmployeeViewSet, EmployeeIncidentsViewSet, AssignationViewSet


router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')
router.register('incidents', EmployeeIncidentsViewSet, basename='incidents')
router.register('assignation', AssignationViewSet, basename='assignation')

#print(router.urls)
urlpatterns = router.urls
