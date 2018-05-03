"""
Tests area_of_triangle module
"""

import unittest
from mock import patch
from mock import MagicMock
from io import StringIO

from src.area_of_triangle import *


class Test_calculate_area_triangle(unittest.TestCase):
    """
    Class that tests function calculate_area_triangle

    """

    def test_area_positive(self):
        """
        Positive test.
        Correct area value

        """
        self.assertEqual(1.0, calculate_area_triangle([[0, 0], [1, 0], [0, 2]]))

    def test_incorrect_args_not_float_nonpositive(self):
        """
        Negative test.
        Checks exception if user entered not a number

        """
        with self.assertRaises(ValueError) as raised_exception:
            calculate_area_triangle([[0, 'a'], [1, 0], [0, 2]])
        self.assertEqual(raised_exception.exception.args[0], "[0, 'a']: coordinats must be number")

    def test_incoorect_agrs_wrong_len_vertex_nonpositive(self):
        """
        Negative test.
        Checks exception if user entered not tree vertex

        """
        with self.assertRaises(ValueError) as raised_exception:
            calculate_area_triangle([[0, 0], [1, 0], [0, 2], [0, 3]])
        self.assertEqual(raised_exception.exception.args[0],
                         "Incorrect format vertex. Inputed 4 points. Needs 3 points")

    def test_incorrect_args_wrong_len_coordinats_nonpositive(self):
        """
        Negative test.
        Checks exception if user entered not two coordinates of vertex

        """

        with self.assertRaises(ValueError) as raised_exception:
            calculate_area_triangle([[0, 0, 1], [1, 0], [0, 2]])
        self.assertEqual(raised_exception.exception.args[0],
                         "Incorrect format [0, 0, 1]. Inputed 3 coordinats. Needs 2 coordinats")

    def test_incorrect_collinear_vertex_nonpositive(self):
        """
        Negative test.
        Checks exception if user entered vertex is a collinear

        """
        with self.assertRaises(ValueError) as raised_exception:
            calculate_area_triangle([[0, 0], [0, 0], [0, 0]])
        self.assertEqual(raised_exception.exception.args[0], "Vertex can't to be vertex triangle. Vertex is collinear")


class Test_is_vertex_triangle(unittest.TestCase):
    """
        Class that tests function is_vertex_triangle

    """

    def test_area_positive(self):
        """
        Positive test

        """
        self.assertIsNone(is_vertex_triangle([[0, 0], [1, 0], [0, 2]]))

    def test_incorrect_args_not_float_nonpositive(self):
        """
           Negative test.
            Checks exception if user entered not a number

        """
        with self.assertRaises(ValueError) as raised_exception:
            is_vertex_triangle([[0, 'a'], [1, 0], [0, 2]])
        self.assertEqual(raised_exception.exception.args[0], "[0, 'a']: coordinats must be number")

    def test_incorrect_agrs_wrong_len_vertex_nonpositive(self):
        """
            Negative test.
            Checks exception if user entered not two coordinates of vertex

        """
        with self.assertRaises(ValueError) as raised_exception:
            is_vertex_triangle([[0, 0], [1, 0], [0, 2], [0, 3]])
        self.assertEqual(raised_exception.exception.args[0],
                         "Incorrect format vertex. Inputed 4 points. Needs 3 points")

    def test_incorrect_args_wrong_len_coordinats_nonpositive(self):
        """
            Negative test.
            Checks exception if user entered not two coordinates of vertex

        """
        with self.assertRaises(ValueError) as raised_exception:
            is_vertex_triangle([[0, 0, 1], [1, 0], [0, 2]])
        self.assertEqual(raised_exception.exception.args[0],
                         "Incorrect format [0, 0, 1]. Inputed 3 coordinats. Needs 2 coordinats")

    def test_incorrect_collinear_vertex_nonpositive(self):
        """
            Negative test.
            Checks exception if user entered vertex is a collinear

        """
        with self.assertRaises(ValueError) as raised_exception:
            is_vertex_triangle([[0, 0], [0, 0], [0, 0]])
        self.assertEqual(raised_exception.exception.args[0], "Vertex can't to be vertex triangle. Vertex is collinear")


class Test_get_vertex_triangle(unittest.TestCase):
    """
        Class that tests function get_vertex_triangle

    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_input_positive(self, mock_stdout):
        """
        Positive test.
        Checks correct entered value

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 0', '0 1', '2 0'])):
            args = get_vertex_triangle()
            self.assertTrue(args[0])
            self.assertEqual(args[1], [[0, 0], [0, 1], [2, 0]])
            self.assertEqual(mock_stdout.getvalue(), "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_inncorrect_input_not_to_float_nonpositive(self, mock_stdout):
        """
            Negative test.
            Checks exception if user entered not a number

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 a', '0 1', '2 0'])):
            args = get_vertex_triangle()
            self.assertFalse(args[0])
            self.assertEqual(args[1], [])
            self.assertEqual(mock_stdout.getvalue(), "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n"
                             + "Value error: ['0', 'a']: coordinats must be number\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_input_wrong_len_coordinats_nonpositive(self, mock_stdout):
        """
            Negative test.
            Checks exception if user entered not two coordinates of vertex

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 0 1', '0 1', '2 0'])):
            args = get_vertex_triangle()
            self.assertFalse(args[0])
            self.assertEqual(args[1], [])
            self.assertEqual(mock_stdout.getvalue(), "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n"
                             + "Incorrect format ['0', '0', '1']. Inputed 3 coordinats. Needs 2 coordinats\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_input_collinear_vertex_nonpositive(self, mock_stdout):
        """
            Negative test.
            Checks exception if user entered vertex is a collinear

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 0 ', '0 0', '0 0'])):
            args = get_vertex_triangle()
            self.assertFalse(args[0])
            self.assertEqual(args[1], [])
            self.assertEqual(mock_stdout.getvalue(),
                             "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n"
                             + "Value error: vertex can't to be vertex triangle. Vertex is collinear\n")


class Test_get_area_triangle_from_point(unittest.TestCase):
    """
        Class that tests function get_area_triangle_from_point

    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_input_positive(self, mock_stdout):
        """
            Positive test.
            Checks correct entered value

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 0', '0 1', '2 0'])):
            self.assertEqual(get_area_triangle_from_point(), 1.0)
            self.assertEqual(mock_stdout.getvalue(), "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_inncorrect_input_not_to_float_nonpositive(self, mock_stdout):
        """
            Negative test.
            Checks exception if user entered not a number

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 a', '0 1', '2 0'])):
            self.assertIsNone(get_area_triangle_from_point())
            self.assertEqual(mock_stdout.getvalue(), "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n"
                             + "Value error: ['0', 'a']: coordinats must be number\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_input_wrong_len_coordinats_nonpositive(self, mock_stdout):
        """
            Negative test.
            Checks exception if user entered not two coordinates of vertex

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 0 1', '0 1', '2 0'])):
            self.assertIsNone(get_area_triangle_from_point())
            self.assertEqual(mock_stdout.getvalue(), "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n"
                             + "Incorrect format ['0', '0', '1']. Inputed 3 coordinats. Needs 2 coordinats\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_input_wrong_collinear_vertex__nonpositive(self, mock_stdout):
        """
            Negative test.
            Checks exception if user entered vertex is a collinear

        """
        with patch('src.area_of_triangle.get_input', MagicMock(side_effect=['0 0 ', '0 0', '0 0'])):
            self.assertIsNone(get_area_triangle_from_point())
            self.assertEqual(mock_stdout.getvalue(),
                             "Enter coordinats vertex\n Format:\n'x1 y1 \n x2 y2 \n x3 y3'\n"
                             + "Value error: vertex can't to be vertex triangle. Vertex is collinear\n")

