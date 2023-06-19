import unittest
from task_one import triangle


class TestTriangle(unittest.TestCase):

    def test1(self):
        self.assertEquals(triangle(5, 5, 5), 'Треугольник равносторонний', 'Что-то не так...')

    def test2(self):
        self.assertEquals(triangle(2, 2, 3), 'Треугольник равнобедренный', 'Что-то не так...')

    def test3(self):
        self.assertEquals(triangle(1, 2, 3), 'Такого треугольника не существует', 'Что-то не так...')


if __name__ == "__main__":
    unittest.main()
