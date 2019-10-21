from django.contrib.auth import get_user_model
from django.db import models


class Offer(models.Model):
    currChoices = [
        ('czk', 'Czk'),
        ('eur', '€'),
        ('usd', '$'),
        ('lib', 'Pounds')
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.FloatField()
    currency = models.CharField(
        max_length=3,
        choices=currChoices,
        )
    active = models.BooleanField(default=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    #objects = OfferManager()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Image(models.Model):
    url = models.CharField(max_length=255)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

'''
class Category(models):
    pass'''