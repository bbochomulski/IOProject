import required
from rest_framework import serializers

from .models import User, Employee, Expert, Transaction, Product, Reservation, Appointment, Pawn, ProductCategory


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.surname = validated_data.get('surname')
        instance.address = validated_data.get('address')
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['url', 'name', 'surname', 'address', 'email']


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(User)
    pesel = serializers.IntegerField(required=True)
    is_boss = serializers.BooleanField(required=True)

    def create(self, validated_data):
        user_data = validated_data.get('user')
        validated_data['user'] = User.objects.create(
            name=user_data.get('name'),
            surname=user_data.get('surname'),
            address=user_data.get('address'),
            email=user_data.get('email')
        )
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        instance.user = User.objects.create(
            name=user_data.get('name'),
            surname=user_data.get('surname'),
            address=user_data.get('address'),
            email=user_data.get('email')
        )
        instance.pesel = validated_data.get('pesel')
        instance.is_boss = validated_data.get('is_boss')
        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = ['user', 'pesel', 'is_boss']


class ExpertSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    number = serializers.IntegerField(required=True)
    speciality = serializers.CharField(required=True)

    def create(self, validated_data):
        return Expert.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.surname = validated_data.get('surname')
        instance.number = validated_data.get('number')
        instance.speciality = validated_data.get('speciality')
        instance.save()
        return instance

    class Meta:
        model = Expert
        fields = ['name', 'surname', 'number', 'speciality']


class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(required=True)
    type = serializers.ChoiceField(choices=Transaction.TransactionType.choices)
    user = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=User.objects.all())
    employee = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=Employee.objects.all())
    expert = serializers.PrimaryKeyRelatedField(many=False, required=False, queryset=Expert.objects.all())

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount')
        instance.type = validated_data.get('type')
        instance.user = User.objects.get(pk=validated_data.get('user'))
        instance.employee = Employee.objects.get(pk=validated_data.get('employee'))
        instance.expert = Expert.objects.get(pk=validated_data.get('expert'))
        instance.save()
        return instance

    class Meta:
        model = Transaction
        fields = ['amount', 'type', 'user', 'employee', 'expert']


class ProductCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        return ProductCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

    class Meta:
        model = ProductCategory
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    amount = serializers.FloatField(required=True)
    category = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=ProductCategory.objects.all())
    description = serializers.CharField(required=True)
    transaction = serializers.PrimaryKeyRelatedField(many=False, required=False, queryset=Transaction.objects.all())

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.amount = validated_data.get('amount')
        instance.category = validated_data.get('category')
        instance.description = validated_data.get('description')
        instance.transaction = validated_data.get('transaction')
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = ['url', 'name', 'amount', 'category', 'description', 'transaction']


class ReservationSerializer(serializers.ModelSerializer):
    date_from = serializers.DateTimeField(required=True)
    date_to = serializers.DateTimeField(required=True)
    product = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=User.objects.all())

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date_from = validated_data.get('date_from')
        instance.date_to = validated_data.get('date_to')
        instance.product = validated_data.get('product')
        instance.user = validated_data.get('user')
        instance.save()
        return instance

    class Meta:
        model = Reservation
        fields = ['url', 'date_from', 'date_to', 'product', 'user']


class AppointmentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=True)
    employee = serializers.PrimaryKeyRelatedField(many=False, required=False, queryset=Employee.objects.all())
    user = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=User.objects.all())
    expert = serializers.PrimaryKeyRelatedField(many=False, required=False, queryset=Expert.objects.all())

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date')
        instance.employee = validated_data.get('employee')
        instance.user = validated_data.get('user')
        instance.expert = validated_data.get('expert')
        instance.save()
        return instance

    class Meta:
        model = Appointment
        fields = ['date', 'employee', 'user', 'expert']


class PawnSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=True)
    loan_to_pay = serializers.IntegerField(required=True)
    loan_paid = serializers.IntegerField(required=True)
    amount = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    next_payment = serializers.DateTimeField(required=True)
    employee = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=Employee.objects.all())
    user = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=User.objects.all())
    product = serializers.PrimaryKeyRelatedField(many=False, required=True, queryset=Product.objects.all())

    def create(self, validated_data):
        return Pawn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date')
        instance.loan_to_pay = validated_data.get('loan_to_pay')
        instance.loan_paid = validated_data.get('loan_paid')
        instance.amount = validated_data.get('amount')
        instance.next_payment = validated_data.get('next_payment')
        instance.employee = validated_data.get('employee')
        instance.user = validated_data.get('user')
        instance.product = validated_data.get('product')
        instance.save()
        return instance

    class Meta:
        model = Pawn
        fields = ['date', 'loan_to_pay', 'loan_paid', 'amount', 'next_payment', 'employee', 'user', 'product']

