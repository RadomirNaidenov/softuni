class IntegerList:

    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def setUp(self):
        self.integer = IntegerList(1, '1', False, [], 2, {}, 1.2)

    def test_check_successful_initialization(self):
        expected = [1, 2]
        actual_result = self.integer.get_data()
        self.assertEqual(expected, actual_result)

    def test_get_data_return_list_with_integers(self):
        expected = [1, 2]
        actual = self.integer.get_data()
        self.assertEqual(expected, actual)

    def test_add_method_not_int_raises(self):
        test_data_values = [7.5, "asd", {}, [], False]
        for value in test_data_values:
            with self.assertRaises(ValueError) as ex:
                self.integer.add(value)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_add_int_adds_element(self):
        result = self.integer.add(5)
        expected = [1, 2, 5]
        self.assertIn(5, self.integer.get_data())
        self.assertEqual(expected, result)

    def test_remove_index_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_remove_number_from_list(self):
        result = self.integer.remove_index(0)
        expected = 1
        self.assertEqual(expected, result)

    def test_get_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.get(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_return_int_from_specific_index(self):
        result = self.integer.get(0)
        expected = 1
        self.assertEqual(expected, result)

    def test_insert_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.insert(3, 2)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_valid_index_but_not_int_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.integer.insert(0, 2.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_return_insert_int_on_specific_index_in_list(self):
        expected = [0, 1, 2]
        self.integer.insert(0, 0)
        actual = self.integer.get_data()
        self.assertEqual(expected, actual)

    def test_get_method_return_biggest_int(self):
        expected = 2
        actual = self.integer.get_biggest()
        self.assertEqual(expected, actual)

    def test_get_index_method_is_return_the_index_on_specific_element(self):
        expected = 1
        actual = self.integer.get_index(2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()












