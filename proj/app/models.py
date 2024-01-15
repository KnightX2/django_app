from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.auth.models import Group
gender_choices = [
    ("F", "Female"),
    ("M", "Male")
]
class person(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender=models.CharField(max_length=20,choices=gender_choices)
    middle_name = models.CharField(max_length=100)
    class Meta:
        abstract = True

class stranger(person):
    is_banned = models.BooleanField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length= 100)
    cars = models.ManyToManyField("vehicle")

    def __str__(self):  # a standard function for displaying info in txt when calling on display function in django shell
        return f'(Stranger:{self.stranger_id.first_name}, {self.stranger_id.middle_name}, {self.stranger_id.last_name},Entry Record ID: {self.entry_record_id}, Reason for Entry: {self.reason_for_entry},Entry Date: {self.entry_date}, Out Date: {self.out_date}, Stranger ID:  {self.stranger_id.person_id})'

class User(person, AbstractUser):
    role=models.CharField(max_length=300)
    last_login=models.DateTimeField(auto_now=True)
    is_logged_in = models.BooleanField()
    groups = models.ManyToManyField(Group, related_name="User")
    

    def __str__(self) -> str:
        return f'({self.first_name},{self.last_name},{self.email},{self.role})'

class session(models.Model):
    session_id = models.BigIntegerField(primary_key = True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    login_time=models.DateTimeField(auto_now_add=True)
    logout_time= models.DateTimeField(auto_now=True)
    IP_address=models.GenericIPAddressField()
    device_info =models.CharField(max_length=400)
    def __str__(self):
        return f'(Session ID:{self.session_id}, User ID: {self.user_id.person_id}, Login Time: {self.login_time}, Logout Time: {self.logout_time}, IP Address: {self.IP_address}, Device Info: {self.device_info})'
    

class entry_record (models.Model):
    entry_record_id = models.BigIntegerField(primary_key = True)
    reason_for_entry = models.CharField(max_length = 300)
    entry_date = models.DateTimeField(auto_now_add=True)
    out_date = models.DateTimeField (auto_now=True)
    stranger_id = models.ForeignKey(stranger,on_delete=models.CASCADE)
    def __str__(self):
        return f'(Entry Record ID: {self.entry_record_id}, Reason for Entry: {self.reason_for_entry}, Entry Date: {self.entry_date}, Out Date: {self.out_date},  Stranger ID: {self.stranger_id.person_id})'

class security_note (models.Model):
    entry_record_id = models.ForeignKey(entry_record,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.now)
    stranger_id = models.ForeignKey(stranger,on_delete=models.CASCADE)
    reason = models.CharField(max_length = 1000)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['entry_record_id','stranger_id'], name = "entry_record_stranger_id")
        ]
class vehicle (models.Model):
    vehicle_id=models.BigIntegerField(primary_key= True)
    state=models.CharField(max_length=100)
    model=models.CharField(max_length=300)
    colour=models.CharField(max_length=50)

class vehicle (models.Model):
    vehicle_id = models.BigIntegerField(primary_key = True)
    vehicle_color = models.CharField(max_length = 100)
    vehicle_model = models.CharField(max_length = 200)
    vehicle_state = models.CharField(max_length= 200)
