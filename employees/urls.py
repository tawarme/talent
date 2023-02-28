from django.urls import path
from employees.views import EmployeeView, EmployeeCreateView

urlpatterns = [
    path('employees/', EmployeeCreateView.as_view()),
    path('employees/<int:pk>/', EmployeeView.as_view()),
]