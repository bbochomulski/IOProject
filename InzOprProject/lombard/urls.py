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
from .views import (
    RootApi,
    UserListView,
    EmployeeListView,
    ExpertListView,
    TransactionListView,
    ProductListView,
    ProductCategoryListView,
    ReservationListView,
    AppointmentListView,
    PawnListView,
    UserDetailView,
    ProductDetailView,
    ReservationDetailView,
    AppointmentDetailView,
    PawnDetailView,
    ProductDetailView)

urlpatterns = [
    path('', RootApi.as_view(), name=RootApi.name),
    path('users', UserListView.as_view(), name=UserListView.name),
    path('users/<int:pk>', UserDetailView.as_view(), name=UserDetailView.name),
    path('employees', EmployeeListView.as_view(), name=EmployeeListView.name),
    path('experts', ExpertListView.as_view(), name=ExpertListView.name),
    path('transactions', TransactionListView.as_view(), name=TransactionListView.name),
    path('products', ProductListView.as_view(), name=ProductListView.name),
    path('products/<int:pk>', ProductDetailView.as_view(), name=ProductDetailView.name),
    path('reservations', ReservationListView.as_view(), name=ReservationListView.name),
    path('reservations/<int:pk>', ReservationDetailView.as_view(), name=ReservationDetailView.name),
    path('appointments', AppointmentListView.as_view(), name=AppointmentListView.name),
    path('appointments/<int:pk>', AppointmentDetailView.as_view(), name=AppointmentDetailView.name),
    path('pawns', PawnListView.as_view(), name=PawnListView.name),
    path('pawns/<int:pk>', PawnDetailView.as_view(), name=PawnDetailView.name),
    path('products-category', ProductCategoryListView.as_view(), name=ProductCategoryListView.name),
]
