"""
File containt functions tha calculate area of triangles useing points from user

"""

import itertools
from math import sqrt

def get_input():
    """
    Return input function
    :return:
    """
    return input();



def get_area_triangle_from_point():
    """
    Returns area of triangle. User inputs points as cootdinates.

    :return: float or None -- returns area of triangle if input is correct
    """
    res_input = get_vertex_triangle()
    if (not res_input[0]):
        return None
    else:
        return calculate_area_triangle(res_input[1])


def get_vertex_triangle():
    """
    Get points of vertex from user.

    :return: tuple(bool,list) -- if first arg is true - then correct input, else.
    """
    print("Enter coordinats vertex\n", "Format:\n'x1 y1 \n x2 y2 \n x3 y3'")
    tmp = []
    vertex = []
    for i in range(1, 4):
        tmp.append(get_input(f"Vertex {i}: ").split())

    for point in tmp:
        if len(point) != 2:
            print(f"Incorrect format {point}. Inputed {len(point)} coordinats. Needs 2 coordinats")
            return False, []
        try:
            x = float(point[0])
            y = float(point[1])
        except ValueError:
            print(f"Value error: {point}: coordinats must be number")
            return False, []
        else:
            vertex.append([x, y])

    sides = [sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) for v1, v2 in itertools.combinations(vertex, 2)]
    if all((s1 >= s2 + s3 for s1, s2, s3 in itertools.permutations(sides, 3))):
        print("Value error: vertex can't to be vertex triangle. Vertex is collinear")
        return False, []
    else:
        return True, vertex


def calculate_area_triangle(vertex: list) -> float:
    """
    Calculates area of triangles

    :param vertex: list of points of vertex.
    :type value: list of lists
    :return: float -- area of triangles

    >>> calculate_area_triangle([[0,0],[1,0],[0,2]])
    1.0

    >>> calculate_area_triangle([[0,'a'],[1,0],[0,2]])
    Traceback (most recent call last):
    ...
    ValueError: [0, 'a']: coordinats must be number

    >>> calculate_area_triangle([[0,0],[1,0],[0,2],[0,3]])
    Traceback (most recent call last):
    ...
    ValueError: Incorrect format vertex. Inputed 4 points. Needs 3 points

    >>> calculate_area_triangle([[0,0,1],[1,0],[0,2]])
    Traceback (most recent call last):
    ...
    ValueError: Incorrect format [0, 0, 1]. Inputed 3 coordinats. Needs 2 coordinats

    """
    is_vertex_triangle(vertex)
    sides = [sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) for v1, v2 in itertools.combinations(vertex, 2)]
    p = sum(sides) / 2
    return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


def is_vertex_triangle(vertex):
    """
    Checks if list of vertex is correct. Raise error if vertex is not correct
    :param vertex: points of vertex
    :type vertex: list of lists
    :return:None


    >>> is_vertex_triangle([[0,0],[1,0],[0,2]])

    >>> is_vertex_triangle([[0,'a'],[1,0],[0,2]])
    Traceback (most recent call last):
    ...
    ValueError: [0, 'a']: coordinats must be number

    >>> is_vertex_triangle([[0,0],[1,0],[0,2],[0,3]])
    Traceback (most recent call last):
    ...
    ValueError: Incorrect format vertex. Inputed 4 points. Needs 3 points

    >>> is_vertex_triangle([[0,0,1],[1,0],[0,2]])
    Traceback (most recent call last):
    ...
    ValueError: Incorrect format [0, 0, 1]. Inputed 3 coordinats. Needs 2 coordinats


    """
    if len(vertex) != 3:
        raise ValueError(f"Incorrect format vertex. Inputed {len(vertex)} points. Needs 3 points")

    for point in vertex:
        if len(point) != 2:
            raise ValueError(f"Incorrect format {point}. Inputed {len(point)} coordinats. Needs 2 coordinats")
        try:
            float(point[0])
            float(point[1])
        except ValueError:
            raise ValueError(f"{point}: coordinats must be number")

    sides = [sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) for v1, v2 in itertools.combinations(vertex, 2)]
    if any((s1 >= s2 + s3 for s1, s2, s3 in itertools.permutations(sides, 3))):
        raise ValueError("Vertex can't to be vertex triangle. Vertex is collinear")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #print(get_area_triangle_from_point())
    #print(calculate_area_triangle([[0,0],[1,0],[0,2]]))
