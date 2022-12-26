from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Steps(models.Model):
    """
        Model to store step records using
        Foreign Key linked to user
    """

    class Meta:
        verbose_name = "Steps"
        ordering = ["-date"]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="steps")
    date = models.DateTimeField()
    steps = models.IntegerField()

    def __str__(self):
        return self.user