from django.db import models
import uuid

class footballclub(models.Model):
    name=models.CharField(max_length=30)
    abb=models.CharField(max_length=30, null=True)
    slogan=models.CharField(max_length=200, null=True)
    description=models.TextField(max_length=5000, null=True)
    logo=models.ImageField(null=True, blank=True, default='default.png')
    estd=models.IntegerField(help_text='Year')
    country=models.CharField(max_length=30)
    league=models.CharField(max_length=30,null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
