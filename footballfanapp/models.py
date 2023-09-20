from django.db import models
import uuid


class footballclub(models.Model):
    name=models.CharField(max_length=30)
    abb=models.CharField(max_length=30, null=True)
    slogan=models.CharField(max_length=200, null=True)
    description=models.TextField(max_length=5000, null=True)
    logo=models.ImageField(null=True, blank=True, default='default_logo.png', upload_to='logo/')
    estd=models.IntegerField(help_text='Year')
    country=models.CharField(max_length=30)
    league=models.CharField(max_length=30,null=True)
    official_site=models.CharField(max_length=200, null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    home_venue=models.CharField(max_length=100, null=True)
    current_manager=models.CharField(max_length=50,null=True)
    manager_pic=models.ImageField(null=True, blank=True, default='default_manager_pic.png', upload_to='managers/')

    def __str__(self):
        return self.name
