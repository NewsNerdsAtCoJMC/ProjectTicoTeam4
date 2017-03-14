from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import SignificantMajors, College, Blog

admin.site.register(SignificantMajors)

admin.site.register(College)

admin.site.register(Blog)
