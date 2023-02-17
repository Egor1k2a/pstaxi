from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode

from pstaxi import settings
from utils.models import generate_unique_slug


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название бренда')
    slug = models.SlugField(max_length=210, default='', blank=True)
    logo = models.ImageField(upload_to='motorpool/brands/', blank=True, null=True)

    @property
    def logo_url(self):
        return self.logo.url if self.logo else f'{settings.STATIC_URL}images/brand-car.png'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('motorpool:brand_detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Brand, self.title)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Option(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Опции'


# Это собственный загрузчик статических файлов, который учитывает кроме пути к модели auto также название бренда
# автомобиля.
def get_upload_to_auto(instance, filename):
    full_file_name = 'motorpool/auto'
    if instance.brand:
        if instance.brand.slug:
            full_file_name += f'/{instance.brand.slug}'
        else:
            full_file_name += f'/{slugify(unidecode(instance.brand.title), allow_unicode=True)}'
        full_file_name += f'/{filename}'
    return full_file_name


class Auto(models.Model):
    AUTO_CLASS_ECONOMY = 'e'
    AUTO_CLASS_COMFORT = 'c'
    AUTO_CLASS_BUSINESS = 'b'

    AUTO_CLASS_CHOICES = [
        (AUTO_CLASS_ECONOMY, 'economy'),
        (AUTO_CLASS_COMFORT, 'comfort'),
        (AUTO_CLASS_BUSINESS, 'business'),
    ]

    number = models.CharField(max_length=15)
    description = models.TextField(max_length=500, default='', blank=True)
    year = models.PositiveSmallIntegerField(null=True)
    auto_class = models.CharField(max_length=1, null=True, choices=AUTO_CLASS_CHOICES, default=AUTO_CLASS_ECONOMY)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE, related_name='cars')
    options = models.ManyToManyField(Option, related_name='cars')
    logo = models.ImageField(upload_to=get_upload_to_auto, blank=True, null=True)

    def display_engine_power(self):
        return self.pts.engine_power
    display_engine_power.short_description = 'Engine power'

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'


class VehiclePassport(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE, related_name='pts')
    vin = models.CharField(max_length=30, verbose_name='Идентификаторный номер (VIN)')
    engine_volume = models.SmallIntegerField(verbose_name='Объём двигателя, куб.см')
    engine_power = models.SmallIntegerField(verbose_name='Мощность двигателя, л.с.')

    def __str__(self):
        return f'{self.auto}::{self.vin}'

    class Meta:
        verbose_name_plural = 'Паспорта машин'
        verbose_name = 'Паспорт машины'
