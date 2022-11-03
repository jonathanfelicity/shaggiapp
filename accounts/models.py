from django.db import models


class Accounts(models.Model):
    balance = models.IntegerField()