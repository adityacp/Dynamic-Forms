from djongo import models
from bson.objectid import ObjectId


class Field(models.Model):
    _id = models.ObjectIdField()
    field_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    options = models.TextField()
    mandatory = models.CharField(max_length=10)

    def __str__(self):
        return "Field {0}".format(self.field_name)


class Form(models.Model):
    _id = models.ObjectIdField()
    name = models.TextField()
    fields = models.ArrayField(model_container=Field)

    def __str__(self):
        return "Form {0}".format(self.name)


class Response(models.Model):
    _id = models.ObjectIdField()
    form = models.EmbeddedField(model_container=Form)
    answers = models.JSONField()

    def __str__(self):
        return "Response for form {0}".format(self.form)
