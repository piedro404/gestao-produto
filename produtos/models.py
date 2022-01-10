from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=35)
    preco = models.DecimalField(max_digits=8,decimal_places=2)
    unidade = models.IntegerField()
    publicador = models.CharField(max_length=50)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='produtos_photos', null=True, blank=True)

    def __str__(self):
        return self.nome_produto