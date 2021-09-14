from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название бренда')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title
