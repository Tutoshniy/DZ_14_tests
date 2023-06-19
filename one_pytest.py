import pytest
from task_one import triangle


def test_triangle():
    assert triangle(5, 5, 5) == 'Треугольник равносторонний', 'Что-то не так...'
    assert triangle(2, 2, 3) == 'Треугольник равнобедренный', 'Что-то не так...'
    assert triangle(1, 2, 3) == 'Такого треугольника не существует', 'Что-то не так...'


if __name__ == "__main__":
    pytest.main()
