from django.contrib import admin

# Importing Models
from .models import Slide, Prediction

# Register your models here.

admin.site.register(Slide)
admin.site.register(Prediction)
