# File hw3_2.py
# Author(s): xingqil, xxxx
from math import inf


# 2.a
def price(i):
    if 4 >= i >= 1:
        return [0, 1, 5, 8, 9][i]
    else:
        return 0


def Rev(N):
    M = {}
    M_cut = {}

    def _rev(N):
        if N in M:
            return M[N]

        k_mx = 0
        mxrev = 0

        if N <= 1:
            mxrev = price(N)
        else:
            for k in range(1, N + 1):
                if price(k) + _rev(N - k) > mxrev:
                    mxrev = price(k) + _rev(N - k)
                    k_mx = k

        M[N] = mxrev
        M_cut[N] = k_mx
        return mxrev

    res = _rev(N)
    cut_list = []

    if N > 1:
        while N != 0:
            cut_list.append(M_cut[N])
            N -= M_cut[N]
    else:
        return N, [N]

    return res, cut_list


# 2.b
def find_shrt_path(A):
    n_ = len(A)

    def _find_shrt_path(A, k):
        new_A = [[x for x in y] for y in A]

        for i in range(n_):
            if i == k:
                continue
            for j in range(n_):
                if j == k:
                    continue

                new_A[i][j] = min(A[i][j], A[i][k] + A[k][j])

        return new_A

    for dim in range(n_):
        A = _find_shrt_path(A, dim)

    return A


# 2.d
def max_sublist_sum(l):
    n_ = len(l)
    if n_ == 1:
        return l
    else:
        mx_l = [0, ] * n_
        mx_l[0] = l[0]

        for i in range(1, n_):
            mx_l[i] = max(l[i], mx_l[i - 1] + l[i])

        return max(mx_l)


if __name__ == "__main__":
    # 2.a
    for i_ in range(21):
        res_, cut_list_ = Rev(i_)
        print("N = {} max revenue: {} cuts: {}".format(i_, res_, cut_list_))

    # 2.b
    A_0 = [[0, inf, inf, 1],
           [2, 0, 4, 5],
           [inf, inf, 0, 3],
           [inf, 7, 1, 0]]
    print("A_4 is: {}".format(find_shrt_path(A_0)))

    # 2.c
    A_0 = [[0, 6, inf, 1, inf, inf, 3],
           [inf, 0, 2, inf, inf, 4, inf],
           [inf, inf, 0, 4, inf, inf, inf],
           [inf, inf, inf, 0, 10, inf, 2],
           [inf, inf, 1, inf, 0, 1, inf],
           [inf, inf, 4, inf, 1, 0, inf],
           [2, 1, inf, inf, inf, inf, 0]]
    print("A_7 is: {}".format(find_shrt_path(A_0)))

    # 2.d
    import numpy as np

    np.random.seed(1)  # so results match

    list1 = [2, -4, 7, 2, 0, 5, -3, 4, -2]
    print("max_sublist_sum(", list1,
          "): ", max_sublist_sum(list1))

    for n in range(10, 20):
        listn = list(np.random.randint(-5, 9, size=n))
        print("max_sublist_sum(", listn,
              "): ", max_sublist_sum(listn))





