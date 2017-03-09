from django.db import models

class SignificantMajors(models.Model):
    major = models.CharField(max_length=255)
    def __str__(self):
        return self.major

class College(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    city = models.CharField(max_length=255)
    enrollment = models.IntegerField()
    instate_cost = models.IntegerField()
    outstate_cost = models.IntegerField()
    website = models.URLField()
    majors = models.URLField()
    financial_aid = models.URLField()
    significant_majors = models.ManyToManyField(SignificantMajors)
    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    post = models.CharField(max_length=3200)
