from django.urls import path

from course_app import views


urlpatterns = [
    path('courses', views.CourseListView.as_view(), name='list-courses'),
    path('course/<int:id>', views.CourseDetailsView.as_view(), name='retrieve-course')
]
