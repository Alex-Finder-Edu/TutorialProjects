from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_wold, name='hello-world'),
    path('view-models/', views.view_models, name='view-models'),
]
