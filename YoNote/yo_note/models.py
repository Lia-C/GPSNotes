from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Notes(models.Model):
    user = models.ForeignKey(User)
    text_body = models.CharField(max_length=200)
    start_date = models.DateTimeField('Start Date')
    exp_date = models.DateTimeField('Expiration Date')