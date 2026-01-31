from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_wold, name='hello-world'),
]
