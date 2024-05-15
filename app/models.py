from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=20)
    data_ingresso = models.DateField()

    def __str__(self):
        return f"{self.matricula} - {self.email}"
