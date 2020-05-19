from django.contrib import admin

from .models import Category, UnitOfMeasure, Measurable, Entry, Expected

admin.site.register(Category)
admin.site.register(UnitOfMeasure)
admin.site.register(Measurable)
admin.site.register(Entry)
admin.site.register(Expected)
