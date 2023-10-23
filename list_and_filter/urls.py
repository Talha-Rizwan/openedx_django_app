from django.urls import path
from .views import hello_template  # make sure to import the new view
from list_and_filter.views import get_courses

urlpatterns = [
    path('hello_template/', hello_template, name='hello_template'),
    path(
        'list/', get_courses, name='get_courses_list'
    )
]