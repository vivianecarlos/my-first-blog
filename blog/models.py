from django.conf import settings
from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.CharField(max_length=8)
    sexo = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=50)
    naturalidade = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome