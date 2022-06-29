"""Пузырьковая сортировка (Bubble Sort)

Временная сложность: О(n2)

- Сравнить текущий элемент со следующим.
- Если следующий элемент меньше/больше текущего, поменять их местами.
- Если массив отсортирован, закончить алгоритм, иначе перейти на шаг 1.

"""

def bubble_sort(data):
    """Реализация алгоритма пузырьковой сортировки."""

    len_data = len(data)

    for _ in range(len_data):
        for j in range(len_data - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        print(" ".join(list(map(str, data))))

    return data

if __name__ == '__main__':

    array = list(map(int, input().split()))
    bubble_sort(array)
