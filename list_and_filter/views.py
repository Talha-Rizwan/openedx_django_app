from django.shortcuts import render

from rest_framework import filters
from rest_framework.generics import ListAPIView
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.course_api.serializers import CourseSerializer

def hello_template(request):
    return render(request, 'list_and_filter/hello.html')

class CourseListAPIView(ListAPIView):
    queryset = CourseOverview.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['display_name', 'language']
