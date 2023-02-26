# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
if a + b > c or b + c > a or c + a > b:
    if a == b == c:
        print('Равнобедренный')
    elif a == b or b == c or c == a:
        print('Равнобедренный')
    else:
        print('Разносторонний')

else:
    print('Это не треугольник')