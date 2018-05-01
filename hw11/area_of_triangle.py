"""
File calculate area of triangles use point from user

"""

import itertools
from numpy import sqrt


def get_area_triangle_from_point():
    """
    Return area of triangles. User write points vertex as cootdinats.

    :return: float or None -- area of triangles if input is correct
    """
    res_input = get_points_triangle()
    if (not res_input[0]):
        return None
    else:
        return calculate_area_triangle(res_input[1])


def get_points_triangle():
    """
    Get point of vertex from user.

    :return: tuple(bool,list) -- first arg true - correct input, false -  other, list - correct point of vertex
    """
    print("Enter coordinats vertex\n", "Format:\n'x1 y1 \n x2 y2 \n x3 y3'")
    tmp = []
    vertex = []
    for i in range(1, 4):
        tmp.append(input(f"Vertex {i}: ").split())

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


def calculate_area_triangle(vertex):
    """
    Calculate area of triangles

    :param vertex: list of point of vertex.
    :type value: list of list
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
    Check list of vertex correcting. Raise error if vertex is't correct
    :param vertex: point of vertex
    :type vertex: list of list
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
    #print(calculate_area_triangle([[0,'a'],[1,0],[0,2]]))
