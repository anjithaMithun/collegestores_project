from django.contrib import admin

from collegeapp.models import Department, Courses, Purpose

# Register your models here.
admin.site.register(Department)
admin.site.register(Courses)
admin.site.register(Purpose)