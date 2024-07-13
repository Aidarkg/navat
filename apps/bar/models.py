from django.db import models


class Base(models.Model):
    title = models.CharField('Название', max_length=200)
    quantity = models.PositiveIntegerField('Количество')
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    UNIT_CHOICES = [
        ('pcs', 'Штук'),
        ('blk', 'Блок'),
    ]

    unit = models.CharField('Единица измерения', max_length=3, choices=UNIT_CHOICES, default='pcs')

    class Meta:
        abstract = True


class Syrup(Base):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сироп'
        verbose_name_plural = 'Сиропы'


class Drinks(Base):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class Tea(Base):
    UNIT_CHOICES = [
        ('pcs', 'Пачка'),
        ('blk', 'Коробка'),
    ]

    unit = models.CharField('Единица измерения', max_length=3, choices=UNIT_CHOICES, default='pcs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чай'
        verbose_name_plural = 'Чай'


class Coffee(Base):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'


class Alcohol(Base):
    CATEGORY_CHOICES = [
        ('vodka', 'Водка'),
        ('vodka_flavored', 'Настроение водка'),
        ('whiskey', 'Виски'),
        ('liqueur', 'Ликер'),
        ('rum', 'Ром'),
        ('cognac', 'Коньяк'),
        ('tequila', 'Текила'),
        ('wine', 'Вино'),
    ]

    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Алкоголь'
        verbose_name_plural = 'Алькоголь'


class Beer(Base):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пиво'
        verbose_name_plural = 'Пива'
