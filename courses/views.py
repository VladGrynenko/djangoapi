from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course

# Create your views here.

def home(request):
    ctx = {}
    return render(request, 'home.html', ctx)


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
