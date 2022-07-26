def multiplicate(A):

    assert len(A), 'Размер list равняется нулю!'

    all_mul = 1
    for a_i in A:
        all_mul *= a_i

    return [all_mul / x for x in A]


if __name__ == '__main__':
    # A = []
    # print(multiplicate(A))
    A = [1, 2, 3, 4]
    print(multiplicate(A))