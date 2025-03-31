from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):

    def setUp(self):
        self.SoccerPlayer = SoccerPlayer("radomir", 20, 5, "Barcelona")
        self.SoccerPlayer2 = SoccerPlayer("Ismail", 22, 10, "PSG")

    def test_success_initialisation(self):
        self.assertEqual("radomir", self.SoccerPlayer.name)
        self.assertEqual(20, self.SoccerPlayer.age)
        self.assertEqual(5, self.SoccerPlayer.goals)
        self.assertEqual("Barcelona", self.SoccerPlayer.team)
        self.assertEqual({}, self.SoccerPlayer.achievements)

    def test_setter_name_if_name_len_is_below_or_equal_5_symbol_raises(self):
        expected = "Name should be more than 5 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.SoccerPlayer.name = "rado"

        self.assertEqual(expected, str(ve.exception))

    def test_setter_age_if_age_is_below_16_raises(self):
        expected = "Players must be at least 16 years of age!"

        with self.assertRaises(ValueError) as ve:
            self.SoccerPlayer.age = 12

        self.assertEqual(expected, str(ve.exception))

    def test_setter_goals_if_goals_are_below_0_set_it_to_0(self):
        self.SoccerPlayer.goals = -2

        self.assertEqual(0, self.SoccerPlayer.goals)

    def test__setter_team_if_team_not_in_valid_teams_raises(self):
        expected = f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!"

        with self.assertRaises(ValueError) as ve:
            self.SoccerPlayer.team = "Beroe"

        self.assertEqual(expected, str(ve.exception))

    def test_change_team_method_if_new_team_not_in_valid_teams_return(self):
        expected = "Invalid team name!"
        actual = self.SoccerPlayer.change_team("CSKA")

        self.assertEqual(expected, actual)

    def test_change_team_method_if_new_team_is_in_valid_teams_return(self):
        expected1 = "Team successfully changed!"
        expected2 = "Real Madrid"
        actual = self.SoccerPlayer.change_team("Real Madrid")

        self.assertEqual(expected2, self.SoccerPlayer.team)
        self.assertEqual(expected1, actual)

    def test_add_new_achievement_method_if_achievement_not_in_achievements_and_return(self):
        expected1 = "i_dont_know has been successfully added to the achievements collection!"
        expected2 = {"i_dont_know": 1}
        actual = self.SoccerPlayer.add_new_achievement('i_dont_know')

        self.assertEqual(1, len(self.SoccerPlayer.achievements))
        self.assertEqual(expected1, actual)
        self.assertEqual(expected2, self.SoccerPlayer.achievements)

    def test_add_new_achievement__two_different(self):
        result = self.SoccerPlayer.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.SoccerPlayer.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.SoccerPlayer.achievements), 1)

        result = self.SoccerPlayer.add_new_achievement("Champions League")
        self.assertEqual(result, "Champions League has been successfully added to the achievements collection!")
        self.assertEqual(self.SoccerPlayer.achievements["Champions League"], 1)
        self.assertEqual(len(self.SoccerPlayer.achievements), 2)

    def test_add_new_achievement__twice(self):
        result = self.SoccerPlayer.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.SoccerPlayer.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.SoccerPlayer.achievements), 1)

        result = self.SoccerPlayer.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.SoccerPlayer.achievements["Ballon d'Or"], 2)
        self.assertEqual(len(self.SoccerPlayer.achievements), 1)

    def test_lt_method_if_our_goals_are_lower_than_other_return(self):
        self.assertEqual(self.SoccerPlayer < self.SoccerPlayer2, "Ismail is a top goal scorer! S/he scored more than radomir.")

        self.assertEqual(self.SoccerPlayer2 < self.SoccerPlayer, "Ismail is a better goal scorer than radomir.")


if __name__ == "__main__":
    main()
