from django.db import models
from django.urls import reverse


class Category (models.Model):
    name = models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse("categories:cat-update", kwargs={"id":self.id})

class SubCategory (models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    depreciation_length = models.IntegerField()

    def get_absolute_url(self):
        return reverse("categories:subcat-update", kwargs={"id":self.id})