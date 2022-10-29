from django.db import models

from apps.user.models import User

# Create your models here.
class Notice(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null= True)
    title = models.CharField('Titulo', max_length=60)   
    category = models.CharField('Categoria', max_length=60, choices=(('Jogos','Jogos'),('Serviços','Serviços'),('Suporte', 'Suporte'),('Compras', 'Compras')), default='Masculino')
    text = models.TextField('Texto')
    image = models.FileField(null= True, blank= True)

    create_at = models.DateTimeField('Criado em', auto_now_add= True)

    def author_name(self):
        return self.user.name

    def path_image(self):
        return str(self.image).replace('static/','')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    notice = models.ForeignKey(Notice, on_delete=models.DO_NOTHING)
    text = models.TextField('Texto')

    create_at = models.DateTimeField('Criado em', auto_now_add= True)