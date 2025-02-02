import unittest
from runner import Runner, Tournament  # Предполагается, что классы Runner и Tournament находятся в runner.py


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):

        cls.all_results = {}

    def setUp(self):

        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_usain_nick_race(self):

        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()


        self.assertEqual(results[2], "Ник")


        self.__class__.all_results[1] = results

    def test_andrey_nick_race(self):

        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()


        self.assertEqual(results[2], "Ник")


        self.__class__.all_results[2] = results

    def test_three_runners_race(self):

        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()


        self.assertEqual(results[3], "Ник")
        self.assertEqual(results[1], "Усэйн")

        # Сохраняем результаты для вывода в tearDownClass
        self.__class__.all_results[3] = results

    @classmethod
    def tearDownClass(cls):
        
        print("\nРезультаты всех тестов:")
        for key, value in cls.all_results.items():
            print(f"Тест {key}: {value}")


if __name__ == '__main__':
    unittest.main()
