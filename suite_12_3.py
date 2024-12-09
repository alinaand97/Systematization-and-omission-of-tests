# suite_12_3.py
import unittest
from Model11 import RunnerTest, TournamentTest

# Создаем тестовый набор (TestSuite)
test_suite = unittest.TestSuite()

# Добавляем тесты
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# В создание объекта TextTestRunner передаем аргумент verbosity=2
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)