from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва', max_length=100)
    anons = models.CharField('Анонс Події', max_length=300)
    full_text = models.TextField('Текс')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'
