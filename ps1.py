from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

# def radixSort(univsize, base, arr):
#     k = math.ceil(math.log(univsize) / math.log(base))
#     n = len(arr)
#     new_arr = [(0, (0, [] * k))] * n #presize array for slight efficiency
#     for i in range(n):
#         (k_i, v_i) = arr[i]
#         new_arr[i] = (k_i, (v_i, BC(k_i, base, k)))
#     for j in range(k):
#         for i in range(n):
#             (k_i, (v_i, vPrime_i)) = new_arr[i]
#             k_i = int(vPrime_i[j])
#             new_arr[i] = (k_i, (v_i, vPrime_i))   
#         new_arr = countSort(base, new_arr)
#     for i in range(n):
#         (k_i, (v_i, vPrime_i)) = new_arr[i]
#         k_i = 0
#         for j in range(k):
#             k_i += vPrime_i[j] * math.pow(base, j)
#         arr[i] = (k_i, v_i)
#     return arr


def radixSort(univsize, base, arr):
    k = math.ceil(math.log(univsize) / math.log(base))
    n = len(arr)
    for i in range(n):
        if arr[i][0] == 0:
            newbase = [0] * k
        else:
            newbase = BC(arr[i][0], base, k)
        pair = list(arr[i])
        pair.append(newbase)

        arr[i] = pair
    for j in range(k):
        for i in range(n):
            k_i = arr[i][2][j]

            arr[i][0] = k_i
        arr = countSort(base, arr)
    for i in range(n):
        k_i = 0
        for j in range(k):
            digit = arr[i][2][j]
            k_i += int(digit * math.pow(base, j))
        arr[i][0] = k_i
        arr[i].pop()
        arr[i] = tuple(arr[i])
    return arr
            
   