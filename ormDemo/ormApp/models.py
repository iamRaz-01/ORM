from django.db import models
from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.name} - {self.branch}"

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):
    LOAN_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    loan_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='loans')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_in_years = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=LOAN_STATUS_CHOICES, default='Pending')
    date_applied = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.loan_id} - {self.customer.first_name} ({self.status})"
