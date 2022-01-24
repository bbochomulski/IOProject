from django.forms import model_to_dict
from rest_framework import generics
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import (
    User,
    Employee,
    Expert,
    Transaction,
    Product,
    Reservation,
    ProductCategory,
    Appointment,
    Pawn
)

from .serializers import (
    UserSerializer,
    EmployeeSerializer,
    ExpertSerializer,
    TransactionSerializer,
    ProductCategorySerializer,
    ProductSerializer,
    ReservationSerializer,
    AppointmentSerializer,
    PawnSerializer
)


def home(request):
    return render(request, 'main_page.html')


class RootApi(generics.GenericAPIView):
    name = 'root-api'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserListView.name, request=request),
            'employees': reverse(EmployeeListView.name, request=request),
            'experts': reverse(ExpertListView.name, request=request),
            'transactions': reverse(TransactionListView.name, request=request),
            'products': reverse(ProductListView.name, request=request),
            'product categories': reverse(ProductCategoryListView.name, request=request),
            'reservations': reverse(ReservationListView.name, request=request),
            'appointments': reverse(AppointmentListView.name, request=request),
            'pawns': reverse(PawnListView.name, request=request),
        })


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-list'


class ExpertListView(generics.ListCreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    name = 'expert-list'


class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    name = 'transaction-list'


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-list'


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    name = 'product-detail'


class ProductCategoryListView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    name = 'productcategory-list'


class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-list'


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-detail'


class AppointmentListView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    name = 'appointment-list'


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    name = 'appointment-detail'

class PawnListView(generics.ListCreateAPIView):
    queryset = Pawn.objects.all()
    serializer_class = PawnSerializer
    name = 'pawn-list'


class PawnDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pawn.objects.all()
    serializer_class = PawnSerializer
    name = 'pawn-detail'
