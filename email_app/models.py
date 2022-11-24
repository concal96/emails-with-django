from django.db import models
from datetime import datetime

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=264, unique=False, )
    ()
    que = datetime.now()
    def __str__(self):
        return self.email

