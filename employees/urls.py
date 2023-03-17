from django.urls import path
from rest_framework.routers import DefaultRouter
#from employees.views import EmployeeView, EmployeeCreateView
from employees.views import ParamViewSet, ParamItemViewSet, EmployeeViewSet, EmployeeIncidentsViewSet, AssignationViewSet, ProjectViewSet, CustomerViewSet


router = DefaultRouter()
router.register('param', ParamViewSet, basename='param')
router.register('param_item', ParamItemViewSet, basename='param_item')
router.register('employees', EmployeeViewSet, basename='employee')
router.register('incidents', EmployeeIncidentsViewSet, basename='incidents')
router.register('assignation', AssignationViewSet, basename='assignation')
router.register('project', ProjectViewSet, basename='project')
router.register('customer', CustomerViewSet, basename='customer')

#print(router.urls)
urlpatterns = router.urls
