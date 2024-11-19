from project.mammal import Mammal
from unittest import TestCase, main


class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal("name", "type", "sound")

    def test_success_initialization(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)

    def test_make_sound_is_return_correct_message(self):
        expected = "name makes sound"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom_is_return_kingdom(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info_is_return_correct_message(self):
        expected = "name is of type type"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)





if __name__ == "__main__":
    main()

