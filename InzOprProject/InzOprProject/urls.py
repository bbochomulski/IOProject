"""InzOprProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lombard import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('employee_table', views.EmployeeTable.as_view(), name='employee_table'),
    path('employee_add', views.EmployeeAdd.as_view(), name='employee_add'),
    path('employee_edit', views.EmployeeEdit.as_view(), name='employee_edit'),
    path('appointment_table', views.AppointmentTable.as_view(), name='appointment_table'),
    path('appointment_add', views.AppointmentAdd.as_view(), name='appointment_add'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('lombard.urls'))
]
