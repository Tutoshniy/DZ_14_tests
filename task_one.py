def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Треугольник равносторонний"
        elif a == b or b == c or a == c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Такого треугольника не существует"
