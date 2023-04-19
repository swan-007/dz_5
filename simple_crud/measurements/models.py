from django.db import models


class Project(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)



class Measurement(models.Model):
    value = models.FloatField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


