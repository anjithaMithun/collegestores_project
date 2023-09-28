from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    wikipedia_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    course_name = models.CharField(max_length=50, unique=True)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('collegeapp:department', args=[self.course_name])

    def __str__(self):
        return self.course_name


class Purpose(models.Model):
    p_name = models.CharField(max_length=250)

    def __str__(self):
        return self.p_name
