from django.test import SimpleTestCase
from course_app.models import CourseModel


class TestCourse(SimpleTestCase):
    def setUp(self):
        self.course = CourseModel(author_id=1, title="Title", text="text")

    def test_title(self):
        self.assertEqual(self.course.title, "Title")
