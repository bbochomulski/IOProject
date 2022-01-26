from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from rest_framework import generics
from django.views.generic import View
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


# for key, value in data.items():
#     print(f"{key} = {value}")


class Home(View):
    def get(self, request):
        return render(request, 'main_page.html')


class UserAdd(View):

    def get(self, request):
        return render(request, 'user_add.html')

    def post(self, request):
        user = User.objects.create(name=request.POST['name'], surname=request.POST['surname'],
                                   address=request.POST['address'], email=request.POST['email'])
        user.save()
        return HttpResponseRedirect(reverse('user_table'))


class UserTable(View):

    def get(self, request):
        users = list()
        for user in User.objects.all():
            users.append(model_to_dict(user))
        context = {
            'users': users
        }
        return render(request, 'user_table.html', context)

    def post(self, request):
        return render(request, 'employee_table.html')



class UserEdit(View):

    def get(self, request):
        return HttpResponseRedirect(reverse('user_table'))

    def post(self, request):
        data = request.POST
        if "save" in request.POST:
            user = User.objects.get(id=data['save'])
            user.name = data['name']
            user.surname = data['surname']
            user.address = data['address']
            user.email = data['email']
            user.save()
            return HttpResponseRedirect(reverse('user_table'))

        if "delete" in request.POST:
            User.objects.get(id=data['delete']).delete()
            return HttpResponseRedirect(reverse('user_table'))

        id = data['edit']
        user = model_to_dict(User.objects.get(id=id))
        context = {
            'user': user
        }
        return render(request, 'user_edit.html', context)


class EmployeeAdd(View):

    def get(self, request):
        return render(request, 'employee_add.html')

    def post(self, request):
        if request.method == 'POST':
            user = User.objects.create(name=request.POST['name'], surname=request.POST['surname'],
                                       address=request.POST['address'], email=request.POST['email'])
            user.save()
            if request.POST.get('is_boss') == 'on':
                is_boss = True
            else:
                is_boss = False
            employee = Employee.objects.create(user=user, pesel=request.POST['pesel'], is_boss=is_boss)
            employee.save()
        return HttpResponseRedirect(reverse('employee_table'))


class EmployeeEdit(View):

    def get(self, request):
        return HttpResponseRedirect(reverse('employee_table'))

    def post(self, request):
        data = request.POST
        if "save" in request.POST:
            employee = Employee.objects.get(id=data['save'])
            user = User.objects.get(id=employee.user_id)
            user.name = data['name']
            user.surname = data['surname']
            user.address = data['address']
            user.email = data['email']
            user.save()
            employee.user = user
            employee.pesel = data['pesel']
            if 'is_boss' in data:
                employee.is_boss = True
            else:
                employee.is_boss = False
            employee.save()
            return HttpResponseRedirect(reverse('employee_table'))

        if "delete" in request.POST:
            employee = Employee.objects.get(id=data['delete'])
            employee.user.delete()
            employee.delete()
            return HttpResponseRedirect(reverse('employee_table'))

        id = data['edit']
        employee = model_to_dict(Employee.objects.get(id=id))
        user = model_to_dict(User.objects.get(id=employee['user']))
        employee['user'] = user
        context = {
            'employee': employee
        }
        return render(request, 'employee_edit.html', context)


class EmployeeTable(View):

    def get(self, request):
        employees = list()
        for employee in Employee.objects.all():
            employee_dict = model_to_dict(employee)
            employee_dict['user'] = model_to_dict(User.objects.get(id=employee_dict['user']))
            employees.append(employee_dict)
        context = {
            'employees': employees
        }
        return render(request, 'employee_table.html', context)

    def post(self, request):
        if "delete" in request.POST:
            print(f"ID do usuniecia: {request.POST['delete']}")
        if "edit" in request.POST:
            print(f"ID do edycji: {request.POST['edit']}")
        return render(request, 'employee_table.html')

class AppointmentAdd(View):

    def get(self, request):
        employees = list()
        users = list()
        experts = list()
        for employee in Employee.objects.all():
            employee = model_to_dict(employee)
            user = model_to_dict(User.objects.get(id=employee['user']))
            employee['user'] = user
            employees.append(employee)
        for user in User.objects.all():
            users.append(model_to_dict(user))
        for expert in Expert.objects.all():
            experts.append(model_to_dict(expert))
        context = {
            'employees': employees,
            'users': users,
            'experts': experts
        }
        return render(request, 'appointment_add.html', context)

    def post(self, request):
        if request.method == 'POST':

            print(f":pracownik{request.POST['employee']}")
            employee = Employee.objects.get(id=request.POST['employee'])
            user = User.objects.get(id=request.POST['user'])
            expert = Expert.objects.get(id=request.POST['expert'])
            appointment = Appointment.objects.create(date=request.POST['date'], employee=employee, user=user, expert=expert)
            appointment.save()

        return HttpResponseRedirect(reverse('appointment_table'))

class AppointmentTable(View):

    def get(self, request):

        appointments = list()

        for appointment in Appointment.objects.all():
            appointments.append(appointment)
        context = {
            'appointments': appointments
        }
        return render(request, 'appointment_table.html', context)

    def post(self, request):
        if "delete" in request.POST:
            Appointment.objects.get(id=request.POST['delete']).delete()
        return HttpResponseRedirect(reverse('appointment_table'))

class AppointmentEdit(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('appointment_table'))
    def post(self, request):
        data = request.POST
        if "save" in request.POST:
            appointment = Appointment.objects.get(id=data['save'])
            appointment.date = data['date']
            appointment.employee = data['employee']
            appointment.user = data['user']
            appointment.expert = data['expert']
            appointment.save()
            return HttpResponseRedirect(reverse('appointment_table'))

        id = data['edit']
        appointment = model_to_dict(Appointment.objects.get(id=id))
        context = {
            'appointment': appointment
        }
        return render(request, 'appointment_edit.html', context)

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
