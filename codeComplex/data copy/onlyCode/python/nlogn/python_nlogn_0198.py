# problem: https://codeforces.com/contest/903/problem/D
# idea: https://www.programmersought.com/article/86646430026/
# import numpy as np


# def almost_difference():
#     n = int(input())
#     if n == 1:
#         return 0
#     # n = 5
#     # array = [1,2,3,1,3]
#     # n = 4
#     # array = [6,6,4,4]
#     x = np.zeros(1000000)
#     # int from 1... -> 10^9
#     # normal array declaration took over 3s. so used array from numpy
#     count_equal = np.zeros(10**9+1)
#     array = [int(el) for el in input().split()]
#     ad_sum = 0
#     prev_sum = 0
#     for i in range(n):
#         # formula from the: https://www.programmersought.com/article/86646430026/
#         ad_sum = ad_sum + i * array[i] - prev_sum +count_equal[array[i]+1] - count_equal[array[i]-1]
#         count_equal[array[i]] += 1
#         prev_sum += array[i]
 
#     return ad_sum
 
 
# print(almost_difference())



def almost_difference():
    n = int(input())
    if n == 1:
        return 0
    # n = 5
    # array = [1,2,3,1,3]
    # n = 4
    # array = [6,6,4,4]
    # x = np.zeros(1000000)
    # int from 1... -> 10^9
    # normal array declaration took over 3s. so used array from numpy
    dict_equal = dict()
    array = [int(el) for el in input().split()]
    ad_sum = 0
    prev_sum = 0
    for i in range(n):
        if not array[i] in dict_equal.keys():
            dict_equal[array[i]] = 0
        if not array[i]-1 in dict_equal.keys():
            dict_equal[array[i]-1] = 0
        if not array[i]+1 in dict_equal.keys():
            dict_equal[array[i]+1] = 0

        # formula from the: https://www.programmersought.com/article/86646430026/
        ad_sum = ad_sum + i * array[i] - prev_sum +dict_equal[array[i]+1] - dict_equal[array[i]-1]
        dict_equal[array[i]] += 1
        prev_sum += array[i]
 
    return ad_sum

print(almost_difference())
