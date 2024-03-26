from django.contrib import admin

# Register your models here.
from Expo_app import models

admin.site.register(models.users)
admin.site.register(models.Company)
admin.site.register(models.Login_view)