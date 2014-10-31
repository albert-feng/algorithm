__author__ = 'fwg'
#!/usr/bin/env python
# -*-coding: utf-8 -*-

from random import randrange


def binary_search(low, high, target, data):
    while low <= high:
        mid = (low + high) // 2
        mid_val = data[mid]
        if target < mid_val:
            high = mid - 1
        elif target > mid_val:
            low = mid + 1
        else:
            return mid
        binary_search(low, high, target, data)


if __name__ == '__main__':
    li = [randrange(1, 100) for i in xrange(0, 10)]
    li.append(20)
    li.sort()
    print li
    print binary_search(0, len(li)-1, 20, li)
