#!/usr/bin/python3
"""Define func to print pascal triangle"""


def pascal_triangle(n):
    """return list of list int that repr pascal triangle
    Args:
    n int = no or row"""
    pascalList = []

    for i in range(n):
        list = []
        for j in range(i+1):
            if j == 0:
                list.append(1)
                continue
            if j == i:
                list.append(1)
                continue
            list.append(pascalList[i-1][j-1] + pascalList[i-1][j])

        pascalList.append(list)
    return pascalList
