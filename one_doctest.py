from task_one import triangle


def triangle_test(a: int, b: int, c: int) -> bool:
    """

    >>> triangle(5, 5, 5)
    'Треугольник равносторонний'
    >>> triangle(2, 2, 3)
    'Треугольник равнобедренный'
    >>> triangle(1, 2, 3)
    'Такого треугольника не существует'
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
