from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):

    def setUp(self):
        self.hero = Hero("test1", 1, 100, 100)
        self.enemy = Hero("test2", 1, 50, 50)

    def test_success_initialisation(self):
        self.assertEqual("test1", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_is_hero_name_is_equal_to_enemy_name_raises(self):
        expected = "You cannot fight yourself"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(expected, str(ex.exception))

    def test_battle_is_hero_health_lower_or_equal_to_0_raises(self):
        expected = "Your health is lower than or equal to 0. You need to rest"
        self.hero.health = -20
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected, str(ex.exception))

    def test_battle_is_enemy_health_is_lower_or_equal_to_0_raises(self):
        expected = f"You cannot fight {self.enemy.username}. He needs to rest"
        self.enemy.health = -3
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected, str(ex.exception))

    def test_is_hero_health_and_enemy_health_are_lower_or_equal_to_1_and_return_message(self):
        self.hero.damage = 9999
        self.enemy.damage = 9999
        expected = "Draw"
        actual = self.hero.battle(self.enemy)

        self.assertEqual(expected, actual)

    def test_is_hero_kills_enemy_hero(self):
        self.hero.damage = 2000
        self.hero.health = 9999
        expected = "You win"
        actual = self.hero.battle(self.enemy)

        self.assertEqual(expected, actual)

    def test_is_hero_gains_stats_after_win(self):
        self.hero.health = 1000
        self.hero.damage = 1000

        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        expected = "You win"
        result = self.hero.battle(self.enemy)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual(expected, result)

    def test_if_hero_looses_battle_and_enemy_gains_stats(self):
        self.enemy.health = 500
        self.enemy.damage = 800
        self.enemy.level = 20
        expected_lvl = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_dmg = self.enemy.damage + 5
        result = self.hero.battle(self.enemy)
        self.assertEqual(expected_lvl, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_dmg, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_method(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected, self.hero.__str__())


if __name__ == "__main__":
    main()