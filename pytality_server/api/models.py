from django.db import models
from django.db.models import TextField, CharField


class Snippet(models.Model):
    wrong_code = TextField()
    correct_code = TextField()
    task_title = CharField(max_length=256)
    #4
