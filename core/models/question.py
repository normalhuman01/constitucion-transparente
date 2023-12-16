from django.db import models
from core.models.form_type import FormType


class Question(models.Model):
    class Meta:
        app_label = "core"

    form_type = models.ForeignKey(FormType, on_delete=models.CASCADE)
    question = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
