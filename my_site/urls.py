"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from my_site import settings
# from animal_shelter import views
from django.conf.urls.static import static
from animal_shelter.views import HomePageView, CatsList, DogsList, ParrotsList, ContactsPageView, CatDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('cats/', CatsList.as_view(), name="cats"),
    path('dogs/', DogsList.as_view(), name="dogs"),
    path('parrots/', ParrotsList.as_view(), name="parrots"),
    path('contacts/', ContactsPageView.as_view(), name="contacts"),
    path('pet_info/<int:pk>/', CatDetailView.as_view(), name="pet_info"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
