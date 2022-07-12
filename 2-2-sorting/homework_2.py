"""ID: 69370361"""


def partition(arr, left, right):
    pivot = arr[left]
    start = left + 1
    end = right - 1
    while True:
        if (start <= end and arr[end] > pivot):
            end -= 1
        elif (start <= end and arr[start] < pivot):
            start += 1
        elif (arr[end] > pivot) or (arr[start] < pivot):
            continue
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
        else:
            arr[left], arr[end] = arr[end], arr[left]
            return end


def quick_sort(arr, left, right):
    if left < right - 1:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot)
        quick_sort(arr, pivot+1, right)


def main():
    n = int(input())
    student_list = []
    for _ in range(n):
        student = input().split()

        # расставляем показатели в том порядке 
        # в котором они будут сортироваться
        tasks = -int(student[1])
        fine = int(student[2])
        login = student[0]

        student_list.append([tasks, fine, login])

    quick_sort(student_list, 0, n)
    for student in student_list:
        print(student[2])


if __name__ == "__main__":
    main()
