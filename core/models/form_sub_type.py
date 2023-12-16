from django.db import models
from core.models.form_type import FormType

class FormSubType(models.Model):
    class Meta:
        app_label = "core"

    name = models.CharField(max_length=255, unique=True)
    form_type = models.ForeignKey(FormType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
