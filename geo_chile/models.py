
from django.db import models


class Region(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["code"]


class Province(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["region", "name"]


class Commune(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["region", "name"]
