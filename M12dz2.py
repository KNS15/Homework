import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'{key}: {value.name}')

    def test_1(self):
        tour_1 = Tournament(90, self.runner_1, self.runner_3)
        result = tour_1.start()
        self.all_results['test_1'] = result
        self.assertTrue(result[max(result)] == "Ник")

    def test_2(self):
        tour_2 = Tournament(90, self.runner_2, self.runner_3)
        result = tour_2.start()
        self.all_results['test_2'] = result
        self.assertTrue(result[max(result)] == "Ник")

    def test_3(self):
        tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour_3.start()
        self.all_results['test_3'] = result
        self.assertTrue(result[max(result)] == "Ник")

