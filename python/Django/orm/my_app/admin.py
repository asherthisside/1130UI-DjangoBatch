from django.contrib import admin
from my_app.models import *

# Register your models here.
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register([Language, Framework])