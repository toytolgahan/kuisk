from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('why/',views.why, name='why'),
    path('discipline/<slug:discipline_slug>/',views.discipline_detail,name='discipline_detail'),
    path('person_detail/<int:pk>/',views.person_detail, name='person_detail'),
    path('search/',views.search,name='search'),
]