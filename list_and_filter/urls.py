from django.urls import path
from .views import hello_template  # make sure to import the new view

urlpatterns = [
    path('hello_template/', hello_template, name='hello_template'),
    # ... your other url patterns ...
]