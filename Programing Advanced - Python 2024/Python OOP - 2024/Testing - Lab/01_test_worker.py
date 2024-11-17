class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Test", 1000, 100)

    def test_successful_initialisation(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_money_on_worker_when_working(self):
        self.worker.work()

        self.assertEqual(self.worker.salary, self.worker.money)

    def test_is_decrease_energy(self):
        self.worker.work()

        self.assertEqual(99, self.worker.energy)

    def test_check_error_leave_work_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_check_is_energy_increased_after_rest(self):
        self.worker.rest()

        self.assertEqual(101, self.worker.energy)

    def test_check_proper_stings_and_values(self):
        self.assertEqual(f'Test has saved 0 money.', str(self.worker.get_info()))


if __name__ == "__main__":
    main()




