from django.shortcuts import render
from rest_framework import viewsets
from . models import Course
from . serializers import CourseSerializer
from . import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (
                # IsAuthenticated,
                permissions.UpdateCoursePermission,)





##
