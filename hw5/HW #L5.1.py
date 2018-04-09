import random as rn


class Matrix:
    """ Class of a matrix that implements the simplest operations

    """

    def __init__(self, *args):
        """

        :param args: list of lists or size matrix
        """
        self.matrix=[]
        self.string = 0
        self.column = 0
        if len(args) == 1 and type(args[0]) == (list):
            if (not self.create_matrix(args[0])):
                raise ValueError("Invalid list sintax")
            pass

        elif len(args) == 2 and type(args[0]) == (int) and type(args[1]) == (int):
            self.create_random_matrix(args[0], args[1])
            pass
        else:
            raise TypeError("Invalid args")
            return

    def create_random_matrix(self, str, col):
        """
            Create random matrix
        :param str: count string
        :param col: count column
        :return: none
        """
        self.string = str
        self.column = col

        for s in range(str):
            string = [rn.random() for x in range(col)]

            self.matrix.append(string)
        pass

    def create_matrix(self, matr):
        """

        :param matr: list of lists - matrix
        :return: bool: true- matrix created, false - don't created
        """
        if len(matr) != 0 and type(matr[0]) == (list) and len(matr[0]) != 0:
            str_check_length = len(matr[0])
            if all(map(lambda str: len(str) == str_check_length, matr)):
                self.string = len(matr)
                self.column = str_check_length
                self.matrix = [x.copy() for x in matr]
                return True

        return False

    def is_squared(self):
        """
        :return:bool: true -  matrix is squared, false matrix isn't squared
        """
        return self.string == self.column

    def is_symmetrical(self, anti_diag=False):
        """
            Check matrix fo simmetrical(antisimmetrical)
        :param anti_diag: bool: True - simmetrical, false-antisimmetrical
        :return:bool
        """
        if self.is_squared():
            if not anti_diag:
                for i in range(self.string):
                    for j in range(i):
                        if self.matrix[i][j] != self.matrix[j][i]:
                            break
                    else:
                        continue
                    return False
                    break
                else:
                    return True
            else:
                for i in range(self.string):
                    for j in range(self.string - i):
                        if self.matrix[i][j] != self.matrix[-j - 1][-i - 1]:
                            break
                    else:
                        continue
                    return False
                    break
                else:
                    return True
        else:
            raise ValueError("matrix is not squared")

    def is_equal_shape(self, matr):
        """

        :param matr: class  Matrix
        :return: bool: True - matrixs have equal shape, false - matrixs don't have equal shape
        """
        if isinstance(matr, self.__class__):
            return matr.string == self.string and matr.column == self.column
        else:
            raise TypeError('matr must be instance class Matrix')

    def is_equal(self, matr):
        """

        :param matr: class  Matrix
        :return:bool: True - matrixs are equal, false - matrixs aren't equal
        """
        if self.is_equal_shape(matr):
            for str1, str2 in zip(self.matrix, matr.matrix):
                if any(map(lambda x, y: x != y, str1, str2)):
                    break
            else:
                return True
        return False

    def transpose(self):
        """
        Transpose matrix
        :return: class matrix
        """
        if self.is_squared():
            matr_T = [x.copy() for x in self.matrix]

            for i in range(self.string):
                for j in range(i):
                    matr_T[j][i] = self.matrix[i][j]
                    matr_T[i][j] = self.matrix[j][i]
            return Matrix(matr_T)
        else:
            raise ValueError("matrix is not squared")

    def prod_const(self, num):
        """
            Matrix multiplication by a number
        :param num: number
        :return: class Matrix
        """
        res_matr = []
        for str in self.matrix:
            res_matr.append([x * num for x in str])
        return Matrix(res_matr)

    def summ(self, matr):
        """
            Sum of two matrices
        :param matr: class Matrix
        :return:  class Matrix
        """
        if (self.is_equal_shape(matr)):
            res_matr = []
            for str1, str2 in zip(self.matrix, matr.matrix):
                res_matr.append([x + y for x, y in zip(str1, str2)])
            return Matrix(res_matr)
        else:
            raise ValueError("Error: matrixs have different shapes")

    def difference(self, matr):
        """
            Difference of two matrices
        :param matr: class Matrix
        :return: matr: class mMtrix
        """
        if (self.is_equal_shape(matr)):
            res_matr = []
            for str1, str2 in zip(self.matrix, matr.matrix):
                res_matr.append([x - y for x, y in zip(str1, str2)])
            return Matrix(res_matr)
        else:
            raise ValueError("Error: matrixs have different shapes")

    def prod(self, matr):
        """
            Multiplication of two matrices
        :param matr: class Matrix
        :return: class matrix
        """
        if isinstance(matr, self.__class__):
            res_matr = Matrix(self.string, matr.column)
            if self.column == matr.string:
                for i in range(res_matr.string):
                    for j in range(res_matr.column):
                        sum = 0;
                        for k in range(self.column):
                            sum += self.matrix[i][k] * matr.matrix[k][j]
                        res_matr.matrix[i][j] = sum
                return res_matr
            else:
                raise ValueError("Error: matrixs have different shapes")

        else:
            raise TypeError('matr must be instance class Matrix')

    def __add__(self, other):
        return self.summ(other)

    def __sub__(self, other):
        return self.difference(other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.prod(other)
        else:
            return self.prod_const(other)

    def __eq__(self, other):
        return self.is_equal(other)

    def __str__(self):
        return self.matrix.__str__()


if __name__ == '__main__':
    a = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])
    b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    c = Matrix([[1, 0], [0, 1]])
    d=Matrix(5,5)
    print("Matrix")
    print("a: ",a)
    print("b: ",b)
    print("c: ",c)
    print("d: ",d)

    print("a==a ",a==a)
    print("b==a ",b==a)

    print("simmetrical main diag for c ",c.is_symmetrical())
    print("simmetrical anti diag for c ", c.is_symmetrical(anti_diag=True))

    print("b.T ",b.transpose())

    print("mult  number c*5",c*5)

    print("sum b+b",b+b)
    print("sub b-b",b-b)

    print("mul a*b",a*b)


