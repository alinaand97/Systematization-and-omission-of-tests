# Систематизация и пропуск тестов



import unittest

def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_run(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_walk(self):
        # Ваш тест
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        # Ваш тест
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        # Ваш тест
        pass