from django.db import models


# Create your models here.


class FibNum(models.Model):
    n = models.IntegerField(default=0)
    value = models.IntegerField(default=0)

    def __int__(self):
        return (self.n, self.value)
