from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=10, null=True)
    branch = models.CharField(max_length=30)
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username



class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.DateField(auto_now_add=True)
    branch = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    notes_file = models.FileField(upload_to='notes/')
    file_type = models.CharField(max_length=50, default='PDF')  # Set a default value
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.subject

