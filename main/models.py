from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, blank=True)
    telegram = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    youtube = models.URLField()

    def __str__(self):
        return self.name


class Company_text(models.Model):
    head_uz = models.CharField(max_length=50, blank=True)
    head_ru = models.CharField(max_length=50, blank=True)
    body_uz = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/head/')


class Buyurtma(models.Model):
    form_text_uz = models.TextField(blank=True)
    form_text_ru = models.TextField(blank=True)
    # name_uz = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.IntegerField()


class Sales_price(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    old_price = models.IntegerField()
    new_price = models.IntegerField()


class Production(models.Model):
    name_uz = models.CharField(max_length=255, blank=True)
    name_ru = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/price_tea/')

    def __str__(self):
        return self.name_uz or self.name_ru


class About_production(models.Model):
    text_uz = models.TextField(blank=True)
    text_ru = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/tea/')


class Tea(models.Model):
    text_uz = models.TextField(blank=True)
    text_ru = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/about_tea/')


class About_company(models.Model):
    head_uz = models.CharField(max_length=255, blank=True)
    head_ru = models.CharField(max_length=255, blank=True)
    text_uz = models.TextField(blank=True)
    text_ru = models.TextField(blank=True)


class About_tea(models.Model):
    head_uz = models.CharField(max_length=255, blank=True)
    head_ru = models.CharField(max_length=255, blank=True)
    body_uz = models.CharField(max_length=255, blank=True)
    body_ru = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    image_background = models.ImageField(upload_to='img/faqts_tea/')


class Faqts_tea(models.Model):
    head_uz = models.CharField(max_length=255, blank=True)
    head_ru = models.CharField(max_length=255, blank=True)
    number = models.IntegerField()
    text_uz = models.TextField(blank=True)
    text_ru = models.TextField(blank=True)

    def __str__(self):
        return self.head_uz or self.head_ru

