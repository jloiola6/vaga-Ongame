from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Nome', max_length= 80)
    nickname = models.CharField('Sobrenome', max_length= 80)
    login = models.CharField('Login', max_length= 15, unique=True)
    password = models.CharField('Senha', max_length= 100)
    email = models.CharField('email', max_length= 40, unique=True)
    sex = models.CharField('Sexo', max_length= 1, choices=(('M','Masculino'),('F','Feminino')), default='Masculino')

    create_at = models.DateTimeField('Criado em', auto_now_add= True)
    updated_at = models.DateTimeField('Atualizado em', auto_now= True)


    def __str__(self):
        return self.name


    