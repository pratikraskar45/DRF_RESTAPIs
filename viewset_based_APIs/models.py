from django.db import models


class BankAccount(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_holder_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    ACCOUNT_TYPES = [
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('Salary', 'Salary'),
    ]

    account_type = models.CharField(
        max_length=20,
        choices=ACCOUNT_TYPES,
        default='Savings'
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )

    branch_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=20)
    account_opening_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.account_number