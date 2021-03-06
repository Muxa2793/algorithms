"""Сортировка выбором (Selection Sort)

Временная сложность: О(n2)

- находим номер минимального значения в текущем списке
- производим обмен этого значения со значением первой неотсортированной позиции 
  (обмен не нужен, если минимальный элемент уже находится на данной позиции)
- теперь сортируем хвост списка, исключив из рассмотрения уже отсортированные элементы

"""

def selection_sort(data):
    """Реализация алгоритма сортировки выбором."""

    for idx, _ in enumerate(data):
        m = idx
        j = idx + 1
        while j < len(data):
            if data[j] < data[m]:
                m = j
            j += 1
        data[idx], data[m] = data[m], data[idx]

    return data

if __name__ == '__main__':

    array = [11, 2, 9, 7, 1]
    print(selection_sort(array))
