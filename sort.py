__author__ = 'fwg'
#!/usr/bin/env python
# -*-coding: utf-8 -*-

import random
from random import randrange


def bubble_sort(data):
    for i in xrange(len(data)):
        for j in xrange(len(data[1:])):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    print data


def quick_sort(data):
    if len(data) < 2:
        return data
    pivot_element = random.choice(data)
    small = [i for i in data if i < pivot_element]
    medium = [i for i in data if i == pivot_element]
    large = [i for i in data if i > pivot_element]
    return quick_sort(small) + medium + quick_sort(large)


if __name__ == '__main__':
    li = [randrange(1, 100) for i in xrange(0, 10)]
    # bubble_sort(li)
    print quick_sort(li)