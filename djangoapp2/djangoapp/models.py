from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=10)

    def __str__(self):
        self.full_name = self.first_name + ' ' + self.last_name
        return f'{self.full_name} - {self.email}'
