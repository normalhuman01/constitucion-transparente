from django.db import models
from core.models.form_sub_type import FormSubType
from core.models.form import Form


class Response(models.Model):
    class Meta:
        app_label = "core"

    form_sub_type = models.ForeignKey(FormSubType, on_delete=models.CASCADE)
    level_agreement = models.IntegerField(null=True, blank=True)
    argument = models.TextField(blank=True, null=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
