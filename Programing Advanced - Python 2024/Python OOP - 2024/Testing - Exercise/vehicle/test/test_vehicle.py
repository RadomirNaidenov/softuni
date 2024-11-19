from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10.0, 150.0)

    def test_success_initialisation(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.assertEqual(10.0, self.vehicle.capacity)
        self.assertEqual(150.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_is_lower_than_need_fuel(self):
        expected = "Not enough fuel"
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(expected, str(ex.exception))

    def test_drive_is_fuel_decreased_after_drive(self):
        expected = 6.25
        self.vehicle.drive(3)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_refuel_the_given_refuel_value_is_bigger_than_our_capacity_raises(self):
        expected = "Too much fuel"
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(200)

        self.assertEqual(expected, str(ex.exception))

    def test_refuel_is_refuel_the_fuel_with_the_given_(self):
        self.vehicle.fuel -= 5

        self.vehicle.refuel(5)
        expected = 10.0

        self.assertEqual(expected, self.vehicle.fuel)

    def test_is__str__method_is_return_correct_result(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == "__main__":
    main()