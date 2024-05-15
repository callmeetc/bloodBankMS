from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class BloodGroup(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Donor(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500, default="")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    image = models.ImageField(default='user_icon_400x472.png',upload_to="user_profile_pics")
    ready_to_donate = models.BooleanField(default=True)

    def __str__(self):
        return str(self.blood_group)
##this code is supposed to reduce the size of the apploaded pp to a standar 300*300 but it isnt working well yet... 
    # def save(self):
    #     super().save(self)
        
    #     img=Image.open(self.image.path)
    #     if img.height>300 or img.width>300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
