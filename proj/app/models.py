from django.db import models
gender_choices = [
    ("F", "Female"),
    ("M", "Male")
]
class person(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length= 100)
    middle_name = models.CharField(max_length=100)
    gender=models.CharField(max_length=20,choices=gender_choices)
    class Meta:
        abstract = True
class stranger(person):
    is_banned = models.BooleanField()

class employee(person):
    email= models.EmailField()
    password_encryption = models.CharField(max_length=300)
    role=models.CharField(max_length=300)
    last_login=models.DateTimeField(auto_now=True)
    is_logged_in = models.BooleanField()

class session(models.Model):
    session_id = models.BigIntegerField(primary_key = True)
    user_id = models.ForeignKey(employee,on_delete=models.CASCADE)
    login_time=models.DateTimeField(auto_now_add=True)
    logout_time= models.DateTimeField(auto_now=True)
    IP_address=models.GenericIPAddressField()
    device_info =models.CharField(max_length=400)
class amer(models.Model):
    hello_name = models.CharField(max_length=300)
    hi = models.CharField(max_length=100,default="A")
