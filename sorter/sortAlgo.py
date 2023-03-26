import numpy as np
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                yield data
def __partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quickSort(arr,low,high):
    if low<high:
        pi=__partition(arr,low,high)
        yield arr
        yield from quickSort(arr,low,pi-1)
        yield from quickSort(arr,pi+1,high)
def __checkArraySorted(arr):
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            return False
    return True
def BogoSort(arr):
    while not __checkArraySorted(arr):
        arr=np.random.permutation(arr)
        yield arr