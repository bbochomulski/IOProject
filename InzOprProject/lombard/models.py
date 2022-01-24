from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        related_name='corresponding_user',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    pesel = models.BigIntegerField(null=False)
    is_boss = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name} {self.user.surname}'


class Expert(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    number = models.IntegerField()
    speciality = models.CharField(max_length=255)


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        IN = 'IN', _('Kupno')
        OUT = 'OUT', _('Sprzedaz')

    amount = models.DecimalField(decimal_places=2, max_digits=10)
    type = models.CharField(max_length=3, choices=TransactionType.choices, default=TransactionType.IN)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=False, blank=False)
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, null=True, blank=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, null=False, blank=False)
    description = models.TextField(max_length=1000)
    transaction = models.ForeignKey(Transaction, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}"


class Reservation(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)


class Appointment(models.Model):
    date = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True, blank=True)


class Pawn(models.Model):
    date = models.DateTimeField()
    loan_to_pay = models.IntegerField()
    loan_paid = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    next_payment = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False, blank=False)



