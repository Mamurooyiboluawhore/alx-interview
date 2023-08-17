#!/usr/bin/python3
''' Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''
    function that rotate it 90 degrees clockwise
    '''
    mat = len(matrix)

    for i in range(mat):
        for j in range(i, mat):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
