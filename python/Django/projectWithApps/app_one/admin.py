from django.contrib import admin
from .models import Student, Faculty

# Register your models here.
admin.site.register([Student, Faculty])