from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    is_active = models.BooleanField(default=True)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name