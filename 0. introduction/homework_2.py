"""ID посылки: 68574022."""

def main(qty: int, trainer: list) -> int:
    """Считает очки на тренажёре."""

    result = 0
    nums_set = set()

    attempts = qty * 2

    for i in range(1, 10):
        attempt = attempts
        for j in trainer:
            if j not in nums_set:
                nums_set.add(j)
            if str(i) == j:
                attempt -= 1
        if str(i) in nums_set and attempt >= 0:
            result += 1

    return result


if __name__ == "__main__":

    assert(main(3, ['1', '2', '3', '1', '2', '.', '.', '2',
                    '2', '.', '.', '2', '2', '.', '.', '2'])) == 2

    assert(main(4, ['1', '1', '1', '1', '9', '9', '9', '9',
                    '1', '1', '1', '1', '9', '9', '1', '1'])) == 1

    assert(main(4, ['1', '1', '1', '1', '1', '1', '1', '1',
                    '1', '1', '1', '1', '1', '1', '1', '1'])) == 0

    qty = int(input())
    array = []
    for _ in range(0, 4):
        array = array + list(input())
    print(main(qty, array))
