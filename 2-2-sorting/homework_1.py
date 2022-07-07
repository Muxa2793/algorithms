"""ID: 69327969"""


def broken_search(nums, target):
    """Реализация бинарного поиска для сломанного массива."""

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def main():
    assert(broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5)) == 6
    assert(broken_search([5, 1], 1)) == 1


if __name__ == "__main__":
    main()
