from django.db import models


class Task(models.Model):
    title = models.CharField('Social network', max_length=100)
    description = models.TextField('Link', max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
