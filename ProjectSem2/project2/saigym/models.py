from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=100)

    # image = models.ImageField(upload_to='saigym/images', default="")

    def __str__(self):
        return self.name


class RegisteredMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    securityQue = models.CharField(
        max_length=50, default=" ", null=True, blank=True)
    answer = models.CharField(
        max_length=50, default=" ", null=True, blank=True)

    def __str__(self):
        return self.user.username


class Card(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=True, related_name='card')
    name = models.CharField(max_length=50, default=" ", null=True, blank=True)
    phone = models.IntegerField(default=1)
    address = models.CharField(max_length=20, null=True, blank=True)
    admission = models.DateTimeField(auto_now_add=True, null=True)
    regno = models.IntegerField(default=1)
    select = models.CharField(max_length=20, null=True, blank=True)
    jan = models.CharField(max_length=10, null=True, blank=True)
    feb = models.CharField(max_length=10, null=True, blank=True)
    mar = models.CharField(max_length=10, null=True, blank=True)
    apr = models.CharField(max_length=10, null=True, blank=True)
    may = models.CharField(max_length=10, null=True, blank=True)
    jun = models.CharField(max_length=10, null=True, blank=True)
    july = models.CharField(max_length=10, null=True, blank=True)
    aug = models.CharField(max_length=10, null=True, blank=True)
    sept = models.CharField(max_length=10, null=True, blank=True)
    octt = models.CharField(max_length=10, null=True, blank=True)
    nov = models.CharField(max_length=10, null=True, blank=True)
    dec = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class diet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=True, related_name='display')
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    upload_diet = models.CharField(max_length=500, null=True, blank=True)
    upload_workout = models.CharField(max_length=500, null=True, blank=True)
    select = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class authTrainer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname


class authMember(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

class BookFirstClass(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    select = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Upload_photo(models.Model):
    image = models.ImageField(upload_to='saigym/static/images', default="")
