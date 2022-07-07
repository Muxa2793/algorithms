"""Быстрая сортировка (Quick Sort)

Временная сложность: O(log2(N)) - в лучшем случае, O(N^2) - в худшем.
Вероятность худшего случая мала.

- Выбираем опорный элемент.
- Делим массив на два подмассива: слева элементы меньше опорного,
  справа — больше, посередине — равные опорному.
  Этот этап часто выделяют в отдельную функцию, которую называют partition.
- Применяем быструю сортировку к двум подмассивам, левому и правому.
- Объединяем результат.

функция partition(array, pivot):
    left = элементы array, меньшие pivot
    center = элементы array, равные pivot
    right = элементы array, большие pivot
    return left, center, right

функция quicksort(array):
    if length(array) < 2:  # базовый случай,
        return array       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = случайный элемент из array
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)

"""

import random


def partition(arr, pivot):

    left = []
    center = []
    right = []

    for item in arr:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            center.append(item)
        else:
            right.append(item)

    return left, center, right


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = random.choice(arr)
    left, center, right = partition(arr, pivot)
    return quick_sort(left) + center + quick_sort(right)


def main():
    arr = [1, 1, 2, 4, 10, 2]
    sort_arr = quick_sort(arr)
    print(sort_arr)


if __name__ == "__main__":
    main()
