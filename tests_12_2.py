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
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.obj1 = Runner('Усэйн', 10)
        self.obj2 = Runner('Андрей', 9)
        self.obj3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    def test_run1(self):
        dist1 = Tournament(90, self.obj1, self.obj3)
        results = dist1.start()
        self.all_results[max(results.keys())] = results
        self.assertEqual(results[2], self.obj3)

    def test_run2(self):
        dist2 = Tournament(90, self.obj2, self.obj3)
        results = dist2.start()
        self.all_results[max(results.keys())] = results
        self.assertEqual(results[2], self.obj3)

    def test_run3(self):
        dist3 = Tournament(90, self.obj1, self.obj2, self.obj3)
        results = dist3.start()
        self.all_results[max(results.keys())] = results
        self.assertEqual(results[3], self.obj3)


if __name__ == "__main__":
    unittest.main()