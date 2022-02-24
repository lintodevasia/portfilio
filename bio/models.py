from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()
    link = models.CharField(max_length=250)
    year = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Experience(models.Model):
    jobrole = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.jobrole
class skill(models.Model):
    skills = models.CharField(max_length=250)
    def __str__(self):
        return self.skills
class who (models.Model):
    whos = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='pics')
    resume = models.FileField(upload_to='files')
    def __str__(self):
        return self.whos

class profile (models.Model):
    dp = models.CharField(max_length=250)
    photos = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.dp