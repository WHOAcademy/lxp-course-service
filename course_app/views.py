from rest_framework import generics

from course_app import serializers, models


class CourseListView(generics.ListAPIView):
    """
    Use this endpoint to GET all courses.
    """
    serializer_class = serializers.CourseSerializer
    queryset = models.CourseModel.objects.all()
