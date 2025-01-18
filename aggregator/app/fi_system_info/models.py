from django.db import models


# Create your models here.


class Agent(models.Model):
    """
    Instance of fuzzing machine
    """
    created = models.DateTimeField("date created", auto_now=True)
    host = models.CharField(max_length=200, default="localhost")
    port = models.CharField(max_length=8, default="80")
    title = models.CharField(max_length=100, blank=True, default='No title')
    description = models.TextField(default="No description")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.url_address


class FuzzingTarget(models.Model):
    """
    Fuzzing process on some work machine
    """
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    target_name = models.CharField(max_length=200, default="No target name")
    priority = models.IntegerField(default=0)
    last_status = models.CharField(max_length=200, default="Unknown")
