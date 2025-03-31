from unittest import TestCase, main
from project.student import Student


class StudentTest(TestCase):

    def setUp(self):
        self.student = Student("Bro1")
        self.student_with_courses = Student("Bro2", {"math": ["1"]})
    
    def test_success_initialisation(self):
        self.assertEqual("Bro1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["1"]}, self.student_with_courses.courses)
    
    def test_enroll_if_course_in_courses_(self):
        expected = "Course already added. Notes have been updated."
        result = self.student_with_courses.enroll("math", "1")

        self.assertEqual(expected, result)

    def test_enroll_if_course_and_noted_if_been_added(self):
        expected = "Course and course notes have been added."
        result = self.student_with_courses.enroll("english", 1, "Y")

        self.assertEqual(expected, result)

    def test_if_course_and_course_notes_have_been_added_with_no_course_notes(self):
        expected = "Course and course notes have been added."
        actual = self.student_with_courses.enroll("bulgarian", "1")
        self.assertEqual(expected, actual)

    def test_enroll_if_course_and_notes_have_been_added_with_no_notes(self):
        expected = "Course has been added."
        result = self.student_with_courses.enroll("french", "2", "No")

        self.assertEqual(expected, result)
        self.assertEqual([], self.student_with_courses.courses["french"])

    def test_add_notes_if_course_not_in_courses(self):
        expected = "Cannot add notes. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("russian", "5")

        self.assertEqual(expected, str(ex.exception))

    def test_add_notes_if_course_in_courses_add_notes_return_message(self):
        expected = "Notes have been updated"
        result = self.student_with_courses.add_notes("math", "5")

        self.assertEqual(["1", "5"], self.student_with_courses.courses["math"])
        self.assertEqual(expected, result)

    def test_leave_course_if_course_in_courses(self):
        expected = "Course has been removed"
        result = self.student_with_courses.leave_course("math")

        self.assertEqual(len(self.student_with_courses.courses), len(self.student_with_courses.courses))
        self.assertEqual(expected, result)

    def test_leave_courses_cannot_leave_courses_if_course_not_in_courses_raises(self):
        expected = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("TMSP")

        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    main()

    
    
        