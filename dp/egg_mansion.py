


def get_min_times(N, k):
    """
    :param N: the height of mansion
    :param k: the number of eggs
    :return:
    """
    import numpy as np
    res = np.zeros((N + 1, k + 1), dtype=np.int)
    res[0, :] = 1
    res[1, :] = 1
    for i in range(2,res.shape[0]):
        res[i, 0] = i
        res[i, 1] = i

    # todo the loop of i
    for j in range(2, res.shape[1]):
        # todo the loop of k
        for i in range(2, res.shape[0]):
            local_min = np.max(res)
            for q in range(1,i):
                if local_min > max(res[q, j - 1], res[i - q-1, j]):
                    local_min = max(res[q, j - 1], res[i - q-1, j])
            res[i, j] = local_min + 1
    return res[N, k]


if __name__ == '__main__':
    N = 2000
    k = 4
    res = get_min_times(N, k)
    print(res)
