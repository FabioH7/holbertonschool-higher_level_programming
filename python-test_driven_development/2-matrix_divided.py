#!/usr/bin/python3
""" Substracts all cells of a matrix"""
def matrix_divided(matrix, div):
    """ Takes a matrix and divides every int or float inside it by div
    
    """
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return list(map(lambda row: list(map(lambda elem: round(elem / div, 2), row)), matrix))
