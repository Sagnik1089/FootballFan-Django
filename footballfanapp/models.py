from django.db import models
import uuid


class footballclub(models.Model):
    name=models.CharField(max_length=30)
    abb=models.CharField(max_length=30, null=True)
    slogan=models.CharField(max_length=200, null=True)
    description=models.TextField(max_length=5000, null=True)
    logo=models.ImageField(null=True, blank=True, default='default_logo.png', upload_to='club_logo/')
    venue_pic=models.ImageField(null=True, blank=True, default='home_default.png', upload_to='club_home_venue/')
    estd=models.IntegerField(help_text='Year')
    country=models.CharField(max_length=30)
    league=models.CharField(max_length=30,null=True)
    official_site=models.CharField(max_length=200, null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    home_venue=models.CharField(max_length=100, null=True)
    current_manager=models.CharField(max_length=50,null=True)
    manager_pic=models.ImageField(null=True, blank=True, default='default_manager_pic.png', upload_to='club_managers/')
    ucl_won=models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.name
    
class internationalteam(models.Model):
    name=models.CharField(max_length=30)
    abb=models.CharField(max_length=30, null=True)
    description=models.TextField(max_length=5000, null=True)
    logo=models.ImageField(null=True, blank=True, default='default_logo.png', upload_to='int_logo/')
    flag=models.ImageField(null=True, blank=True, default='flag_default.png', upload_to='int_flag/')
    official_site=models.CharField(max_length=200, null=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    current_manager=models.CharField(max_length=50,null=True)
    manager_pic=models.ImageField(null=True, blank=True, default='default_manager_pic.png', upload_to='int_managers/')
    wc_won=models.IntegerField(null=True, default=0)
    euro_won=models.IntegerField(null=True, default=0)
    copa_won=models.IntegerField(null=True,default=0)
    continent=models.CharField(max_length=30,null=True)


    def __str__(self):
        return self.name
