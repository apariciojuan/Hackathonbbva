from django.db import models
from random import choice, randint
from django.urls import reverse
# Create your models here.


def custom_upload(instance, filename):
    filename = filename.encode('ascii', errors='ignore').decode('ascii')
    return 'images/{0}/{1}'.format(instance.apellido, filename)


class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=custom_upload)
    numero_usuario = models.CharField(max_length=50, unique=True, blank=True)


    def get_absolute_url(self):
        return reverse("perfil", kwargs={'pk': self.pk})


    def save(self, *args, **kwargs):
        if not self.numero_usuario:
            sec = ["HTC", "HAS", "CTH", "FTB", "GRA", "XEM", "PSE", "BAA"]
            number = "%s%s"%(choice(sec), randint(100,222000))
            while PerfilUsuario.objects.filter(numero_usuario=number).count():
                number = "%s%s"%(choice(sec), randint(100,222000))
            self.numero_usuario = number
        super().save(*args, **kwargs)


    def __str__(self):
        """Return record owner."""
        return str(self.apellido)
