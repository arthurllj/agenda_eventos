from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    ativo = models.BooleanField(default=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    participantes = models.ManyToManyField(Participante, blank=True)

    def __str__(self):
        return self.titulo
