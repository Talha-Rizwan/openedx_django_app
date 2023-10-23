from django.urls import path
from .views import hello_template
from list_and_filter.views import CourseListAPIView

urlpatterns = [
    path('hello_template/', hello_template, name='hello_template'),
    path('v1/list/', CourseListAPIView.as_view(), name='course_list')
]
