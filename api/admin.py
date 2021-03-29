from django.contrib import admin

# Register your models here.
from api.models import CustomUser, Plotter, Pattern

admin.site.register(CustomUser)
admin.site.register(Plotter)
admin.site.register(Pattern)