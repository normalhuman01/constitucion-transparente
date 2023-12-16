from django.db import models


class Form(models.Model):
    class Meta:
        app_label = "core"

    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, unique=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
