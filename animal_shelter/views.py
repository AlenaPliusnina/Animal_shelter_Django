from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from animal_shelter.models import Animal


class HomePageView(TemplateView):

    template_name = "home.html"

    # def get_animal(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["latest_articles"] = Animal.objects.all()
    #     return context


class CatsList(ListView):
    queryset = Animal.objects.filter(kind_of_animal='C')
    template_name = "pets.html"
    context_object_name = "pets"


class DogsList(ListView):
    queryset = Animal.objects.filter(kind_of_animal='D')
    template_name = "pets.html"
    context_object_name = "pets"


class ParrotsList(ListView):
    queryset = Animal.objects.filter(kind_of_animal='P')
    template_name = "pets.html"
    context_object_name = "pets"


class ContactsPageView(TemplateView):
    template_name = "contacts.html"


class CatDetailView(DetailView):
    # queryset = Animal.objects.filter(kind_of_animal='C')
    model = Animal
    template_name = "pet_info.html"
    context_object_name = "pet"


