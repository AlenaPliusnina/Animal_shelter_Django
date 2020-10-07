from django.contrib import admin
from animal_shelter.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind_of_animal',)