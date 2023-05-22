from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
def emailValidator(value):
    if str(value).endswith('@esprit.tn') == False:
        raise ValidationError(
            "Your email must be @esprit.tn"
        )

       

class Person(AbstractUser):
    cin = models.CharField(
        "CIN",
        primary_key=True,
        max_length=8,
        validators = [
            MaxLengthValidator(8,message="CIN must be 8 characters long"),
            MinLengthValidator(8,message="CIN must be 8 characters long"),
            RegexValidator(
                regex=r'^[0-9]{8}$',
                message="digits only",
            )
        ]
    )
    username = models.CharField("Username", max_length=255, unique=True)
    email = models.EmailField(
        unique=True,validators=[emailValidator]
    )


    USERNAME_FIELD = 'username'
 


    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "users"
