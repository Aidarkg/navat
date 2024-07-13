from django.db import models


class Base(models.Model):
    title = models.CharField('Название', max_length=200)
    quantity = models.PositiveIntegerField('Количество')
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        abstract = True


class Syrup(Base):
    UNIT_CHOICES = [
        ('pcs', 'Штук'),
        ('blk', 'Блок'),
    ]

    unit = models.CharField('Единица измерения', max_length=3, choices=UNIT_CHOICES, default='pcs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сироп'
        verbose_name_plural = 'Сиропы'
