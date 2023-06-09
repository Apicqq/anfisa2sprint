from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')

    class Meta:
        abstract = True


class IsOnMainModel(models.Model):
    is_on_main = models.BooleanField(default=False,
                                     verbose_name='На главную')

    class Meta:
        abstract = True
