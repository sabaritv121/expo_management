from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Login_view(AbstractUser):
    is_users = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)




class users(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='users')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name




class Company(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE, related_name='company')
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    status = models.BooleanField(default= False)

    def __str__(self):
        return self.company_name


# create expo
class CreateExpo(models.Model):
    venue = models.TextField(max_length=100)
    layout = models.FileField()
    start_date = models.DateField()
    end_date = models.DateField()
    expo_code = models.CharField(max_length=6)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.expo_code



#online form submition



class OnlineForm(models.Model):
    data = [

        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    ]
    user = models.ForeignKey(Company, on_delete=models.CASCADE)
    expo_code = models.ForeignKey(CreateExpo, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    number_of_booths = models.CharField(choices=data,max_length=20,default="1")

    def __str__(self):
        return self.user.company_name



#book tickets
class BookTickets(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    expo_code = models.ForeignKey(CreateExpo, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    mobile = models.CharField(max_length=10,default=0000000000)
    status = models.IntegerField(default=0)



#booth allocation table
class BoothAllocation(models.Model):
    expocode = models.ForeignKey(OnlineForm, on_delete=models.CASCADE)
    number = models.IntegerField()
    Booth_id = models.CharField(max_length=6)


#feedbacks and reply
class Feedback(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)