"""Сортировка подсчётом (Counting Sort)

Временная сложность: O(N+k)

- Создаём массив из нулей длиной в максимально возможное число сортируемого массива.
- Проходим по сортируемому массиву и считаем, сколько раз встретился 
  каждый из его элементов. Для этого в массиве созданном массиве по индексу 
  каждого встретившегося элемента увеличивать значение на единицу.
- Проходим по элементам созданного массива и добавим их в новый массив 
  с учётом количества повторов.

функция counting_sort(array, k)
  counted_values = [0] * k
  for value in array:
    counted_values[value] += 1

  index = 0
  for value = 0 .. (k - 1):
    for amount = 1 .. counted_values[value]:
      array[index] = value
      index += 1

"""


def counting_sort(arr, n):
    repeat_arr = [0] * n
    for item in arr:
        repeat_arr[item] += 1

    sort_arr = []

    for num in range(n):
        sort_arr += [num] * repeat_arr[num]

    return sort_arr


def main():
    arr = [5, 7, 1, 0, 1, 5, 11, 1]
    n = 12
    sort_arr = counting_sort(arr, n)
    print(sort_arr)


if __name__ == "__main__":
    main()
