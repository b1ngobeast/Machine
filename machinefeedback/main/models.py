from django.db import models


class Countries(models.Model):
    name = models.TextField(max_length=60, db_index=True)

    class Meta:
        verbose_name = 'Страна',
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Creator(models.Model):
    name = models.TextField(max_length=60, help_text='Производитель')
    country = models.TextField(max_length=60, help_text='Страна')

    class Meta:
        verbose_name = 'Производитель',
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Car(models.Model):
    car = models.TextField(max_length=60, help_text='Модель авто')
    creator = models.TextField(max_length=100, help_text='Производитель')
    first_year = models.CharField(max_length=4, help_text='Начало выпуска')
    last_year = models.CharField(max_length=4, help_text='Окончание выпуска(если производится до сих пор - нв)')

    class Meta:
        verbose_name = 'Машина',
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.car


class Comment(models.Model):
    autor_email = models.EmailField()
    car = models.TextField(max_length=60, help_text='Модель авто')
    create_date = models.DateField()
    comment = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Коммент',
        verbose_name_plural = 'Комменты'

    def __str__(self):
        return self.car
