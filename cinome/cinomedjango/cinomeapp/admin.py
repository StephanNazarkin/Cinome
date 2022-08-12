from django.contrib import admin
from .models import Test

class TestAdmin(admin.ModelAdmin):
  list = ('title')

  admin.site.register(Test)