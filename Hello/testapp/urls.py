from django.urls import path
from testapp import views
urlpatterns = [
    path('home',views.home, name='home'),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contacts',views.contacts,name="contacts"),
]
