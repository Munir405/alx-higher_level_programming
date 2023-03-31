#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    loi = list_of_integers
    beg = 0
    end = len(loi)-1

    if loi[beg] > loi[beg+1]:
        return loi[beg]
    if loi[end] > loi[end-1]:
        return loi[end]

    mid = (beg+end)//2
    if loi[mid-1] < loi[mid] and loi[mid+1] < loi[mid]:
        return loi[mid]
    if loi[mid] < loi[mid-1]:
        return find_peak(loi[beg:mid+1])
    elif loi[mid] < loi[mid+1]:
        return find_peak(loi[mid:end+1])
    else:
        return loi[beg]
