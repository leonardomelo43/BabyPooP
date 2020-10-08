from django.db import models


class Customer(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        password = models.CharField(max_length=100)
        telephone = models.CharField(max_length=100)
        address_line1 = models.CharField(max_length=100)
        address_line2 = models.CharField(max_length=100)
        zip_code = models.CharField(max_length=20)
        state = models.CharField(max_length=100)
        profile_pic = models.ImageField('Foto de Perfil', upload_to='media', blank=True)

        def __str__(self):
            return self.name
