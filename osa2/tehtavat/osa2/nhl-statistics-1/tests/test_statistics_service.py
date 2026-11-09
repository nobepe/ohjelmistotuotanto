
import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_player_that_does_not_exist(self):
        player = self.stats.search("Nobody")
        self.assertIsNone(player)

    def test_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top(self):
        players = self.stats.top(2)
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")


if __name__ == "__main__":
    unittest.main()
