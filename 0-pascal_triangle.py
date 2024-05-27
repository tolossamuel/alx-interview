#!/usr/bin/python3

"""
0-main
"""
def pascal_triangle(n):
    arr = [[1]]
    for i in range(n-1):
        temp = [1]
        for x in range(1,len(arr[-1])):
            temp.append(arr[-1][x-1]+arr[-1][x])
        temp.append(1)
        arr.append(temp.copy())
    return arr

            
        