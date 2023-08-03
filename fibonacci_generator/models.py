from django.db import models


class FibNum(models.Model):
    """
    Creation of FibNum model in the database DB SQLite3 with fields n, value to store and retrieve data
    """
    # nth term in the sequence
    n = models.IntegerField(default=0)
    # value of nth term in the sequence
    value = models.IntegerField(default=0)

    def __int__(self):
        return self.n, self.value
