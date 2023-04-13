from django.urls import path
from . import views
urlpatterns = [
    path('send_comment/', views.send_comment, name='send_comment'),
]