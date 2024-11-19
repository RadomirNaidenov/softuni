class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main

class CarTest(TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Supra", 10, 50)

    def test_successful_initialisation(self):
        self.assertEqual("Toyota", self.car.make)
        self.assertEqual("Supra", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make_(self):
        expected = "Make cannot be null or empty!"
        with self.assertRaises(Exception) as ex:
            Car("", "Supra", 10, 50)

        self.assertEqual(expected, str(ex.exception))

    def test_empty_model(self):
        expected = "Model cannot be null or empty!"
        with self.assertRaises(Exception) as ex:
            Car("Toyota", "", 10, 50)

        self.assertEqual(expected, str(ex.exception))

    def test_fuel_consumption_value_cannot_negative_or_equal_to_0(self):
        expected = "Fuel consumption cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            Car("Toyota", "Supra", 0, 50)

        self.assertEqual(expected, str(ex.exception))

    def test_fuel_capacity_value_cannot_be_negative_or_equal_to_0(self):
        expected = "Fuel capacity cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            Car("Toyota", "Supra", 10, 0)

        self.assertEqual(expected, str(ex.exception))

    def test_fuel_amount_cannot_be_lower_than_zero(self):
        expected = "Fuel amount cannot be negative!"
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual(expected, str(ex.exception))

    def test_refuel_fuel_cannot_be_lower_or_equal_to_0(self):
        expected = "Fuel amount cannot be zero or negative!"
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual(expected, str(ex.exception))

    def test_refuel_is_adding_fuel_to_fuel_amount(self):
        expected = 20
        self.car.refuel(20)

        self.assertEqual(expected, self.car.fuel_amount)

    def test_refuel_is_fuel_amount_is_bigger_than_fuel_capacity(self):
        expected = 50
        self.car.refuel(51)

        self.assertEqual(expected, self.car.fuel_amount)

    def test_drive_method_if_fuel_is_enough_to_drive(self):
        expected = "You don't have enough fuel to drive!"

        with self.assertRaises(Exception) as ex:
            self.car.drive(3000)

        self.assertEqual(expected, str(ex.exception))

    def test_drive_method_is_lowered_after_drive(self):
        expected = 20
        self.car.fuel_amount = 40
        self.car.drive(200)
        self.assertEqual(expected, self.car.fuel_amount)

if __name__ == "__main__":
    main()








