from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=90, default='', verbose_name='Категория')

    def display_event_count(self):
        return self.events.count()
    display_event_count.short_description = 'Количество событий'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Feature(models.Model):
    title = models.CharField(max_length=90, default='', verbose_name='Свойство')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Свойство события'
        verbose_name_plural = 'Свойства события'


class Event(models.Model):
    FULLNESS_FREE = '1'
    FULLNESS_MIDDLE = '2'
    FULLNESS_FULL = '3'
    FULLNESS_LEGEND_FREE = '<= 50%'
    FULLNESS_LEGEND_MIDDLE = '> 50%'
    FULLNESS_LEGEND_FULL = 'sold-out'
    FULLNESS_VARIANTS = [
        (FULLNESS_FREE, FULLNESS_LEGEND_FREE),
        (FULLNESS_MIDDLE, FULLNESS_LEGEND_MIDDLE),
        (FULLNESS_FULL, FULLNESS_LEGEND_FULL),
    ]

    title = models.CharField(max_length=200, default='', verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')
    date_start = models.DateTimeField(verbose_name='Дата начала')
    participants_number = models.PositiveSmallIntegerField(default=0, verbose_name='Количество участников')
    is_private = models.BooleanField(default=False, verbose_name='Частное')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name='events')
    features = models.ManyToManyField(Feature, blank=True)

    def display_enroll_count(self):
        return self.enrolls.count()
    display_enroll_count.short_description = 'Количество записей'

    def get_places_left(self):
        return int(self.participants_number or 0) - self.display_enroll_count()

    def get_fullness_legend(self, **kwargs):
        legend = ''
        if int(self.participants_number or 0) > 0:
            legend = Event.FULLNESS_LEGEND_FREE
            places_left = kwargs.get('places_left', None)
            if places_left is None:
                places_left = self.get_places_left()
            if places_left == 0:
                legend = Event.FULLNESS_LEGEND_FULL
            elif places_left < int(self.participants_number or 0) / 2:
                legend = Event.FULLNESS_LEGEND_MIDDLE
        return legend

    def display_places_left(self):
        places_left = self.get_places_left()
        return f'{places_left} ({self.get_fullness_legend(places_left=places_left)})'
    display_places_left.short_description = 'Осталось мест'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class Enroll(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='enrolls')
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE, related_name='enrolls')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.event.title} - {self.user}'

    class Meta:
        verbose_name = 'Запись на событие'
        verbose_name_plural = 'Записи на событие'


class Review(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE, related_name='reviews')
    rate = models.PositiveSmallIntegerField(default=0)
    text = models.TextField(max_length=1000, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.rate} - {self.event.title}'

    class Meta:
        verbose_name = 'Отзыв на событие'
        verbose_name_plural = 'Отзывы на события'
