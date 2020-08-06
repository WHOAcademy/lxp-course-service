from django.urls import path

from course_app import views


urlpatterns = [
    path('', views.CourseListView.as_view(), name='list-courses'),
]
