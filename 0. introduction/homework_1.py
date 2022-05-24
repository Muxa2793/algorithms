"""ID посылки: 68573968."""


def calculate_distance(street_length: int, numbers: list) -> list:
    """Расчитывает дистанцию от пустого участка."""

    dist = street_length
    result = [0] * street_length

    for i in range(0, street_length):
        if numbers[i] == 0:
            dist = 0
        else:
            dist += 1
        result[i] = dist

    return result


def main(street_length: int, numbers: list) -> str:
    """Рассчитывает минимальное расстояние до пустых участков."""

    # считаем дистанцию с левой стороны
    dist_left = calculate_distance(street_length, numbers)
    # считаем дистанцию с правой стороны
    dist_right = calculate_distance(street_length, numbers[::-1])[::-1]

    result = []

    # отбираем минимальные значения
    for i in range(0, street_length):
        if dist_left[i] < dist_right[i]:
            result.append(str(dist_left[i]))
        else:
            result.append(str(dist_right[i]))

    return result


if __name__ == "__main__":

    assert(main(6, [0, 7, 9, 4, 8, 20])) == ['0', '1', '2', '3', '4', '5']
    assert(main(5, [0, 1, 4, 9, 0])) == ['0', '1', '2', '1', '0']

    print('Введите длину улицы: ')
    street_length = int(input())
    print('Укажите номера участков: ')
    numbers = list(map(int, input().split()))
    print(' '.join(main(street_length, numbers)))
