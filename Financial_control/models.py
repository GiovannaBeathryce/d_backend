from django.db import models


class Financial_control(models.Model):
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.IntegerField()
    cartão = models.CharField(max_length=12)
    hora = models.CharField(max_length=12)
    dono_da_loja = models.CharField(max_length=15)
    nome_loja = models.CharField(max_length=20)
