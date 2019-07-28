from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length = 10)

    genders = (
        ('M','Male'),
        ('F','Female')
    )

    gender = models.CharField(max_length = 1, choices = genders)

    def __str__(self):
        return self.user.username



class Item(models.Model):
    name = models.CharField(max_length=60)
    category_list = [
        ('ELC', 'Electronics'),
        ('CA', 'Cars'),
        ('LA', 'Lands'),
    ]

    category = models.CharField(max_length=3, choices=category_list)
    description = models.CharField(max_length=1600)
    picture = models.ImageField(upload_to='items_pics')
    price = models.IntegerField(max_length=12)
    cities = [
        ('RUH', 'Riyadh'),
        ('MAK', 'Makkah'),
        ('JED', 'Jeddah'),
    ]
    location = models.CharField(max_length=3, choices=cities)
    mobile = models.IntegerField(max_length=10)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absloute_url(self):
    #     return reverse('details', args=[str(self.id)])
