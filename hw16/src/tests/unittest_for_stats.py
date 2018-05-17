import unittest
from stat import stat_func


class Tests_mean_stats(unittest.TestCase):
    def test__mean__correct_args__positive(self):
        data=[1,2,3,4,5]

        self.assertEqual(stat_func.mean(data),3)

    def test__mean__args_not_iterable__nonpositive(self):
        data=5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.mean(data)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")

    def test__mean__args_unsupported_plus__nonpositive(self):
        data = ['a',2]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.mean(data)
        self.assertEqual(raised_exception.exception.args[0], "unsupported operand ' + '")

    def test__mean__args_length_0__nonpositive(self):
        data=[]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.mean(data)
        self.assertEqual(raised_exception.exception.args[0], "division by zero")
#

    def test__median__correct_args__length_6__positive(self):
        data=[1,2,2,4,5,6]
        self.assertEqual(stat_func.median(data), 3)

    def test__median__correct_args__length_7__positive(self):
        data=[1,2,2,4,5,6,7]
        self.assertEqual(stat_func.median(data), 4)

    def test__median__args_not_iterable__nonpositive(self):
        data=5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.median(data)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")

    def test__median__args_unsupported_compare__nonpositive(self):
        data = ['a',2]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.median(data)
        self.assertEqual(raised_exception.exception.args[0], "'<' not supported operation")

#
    def test__mode__correct_args__positive(self):
        data=[1,2,2,4,5,6,4,7]

        self.assertEqual(stat_func.mode(data), 4)

    def test__mode__args_not_iterable__nonpositive(self):
        data=5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.mode(data)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")
#
    def test__quartile__correct_args__positive(self):
        data = [1, 2, 2, 4, 5, 6, 4, 7]
        q=0.25

        self.assertListEqual(stat_func.mode(data), [6,7])

    def test__quartile__args_not_iterable__nonpositive(self):
        data = 5
        p=0.5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.quartile(data,p)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")

    def test__quartile__args_p_not_in_intervel__nonpositive(self):
        data = [1,2,3,4,5]
        p=10

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.quartile(data,p)
        self.assertEqual(raised_exception.exception.args[0], "p must be [0,1]")

    def test__quartile__args_unsupported_compare__nonpositive(self):
        data = ['a', 2]
        p=0.5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.quartile(data,p)
        self.assertEqual(raised_exception.exception.args[0], "'<' not supported operation")
#
    def test__data_range__correct_args__positive(self):
        data=[1,2,3,4,5,6,7]

        self.assertEqual(stat_func.data_range,6)


    def test__data_range__args_unsupported_compare__nonpositive(self):
        data = ['a', 2]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.data_range(data)
        self.assertEqual(raised_exception.exception.args[0], "'<' not supported operation")



    def test__data_range__args_not_ierable__nonpositive(self):
        data = 5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.data_range(data)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")
#

    def test__variance__correct_args__positive(self):
        data=[1,2,3,4,5]

        self.assertEqual(stat_func.variance(data),2.5)

    def test__variance__args_not_iterable__nonpositive(self):
        data=5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.variance(data)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")

    def test__variance__args_unsupported_plus__nonpositive(self):
        data = ['a',2]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.variance(data)
        self.assertEqual(raised_exception.exception.args[0], "unsupported operand ' + '")

    def test__variance__args_length_0__nonpositive(self):
        data=[]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.variance(data)
        self.assertEqual(raised_exception.exception.args[0], "division by zero")

#
    def test__std__correct_args__positive(self):
        data=[1,2,3,4,5]

        self.assertEqual(stat_func.std(data),1.581138)

    def test__std__args_not_iterable__nonpositive(self):
        data=5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.std(data)
        self.assertEqual(raised_exception.exception.args[0], "x object is not iterable")

    def test__std__args_unsupported_plus__nonpositive(self):
        data = ['a',2]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.std(data)
        self.assertEqual(raised_exception.exception.args[0], "unsupported operand ' + '")

    def test__std__args_length_0__nonpositive(self):
        data=[]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.std(data)
        self.assertEqual(raised_exception.exception.args[0], "division by zero")
#
    def test__dot__correct_args__positive(self):
        x=[1,2,3,4,5]
        y=[2,2,2,2,2]

        self.assertEqual(stat_func.dot(x,y),30)


    def test__dot__args_not_iterable_x__nonpositive(self):
        x = 5
        y = [2, 2, 2, 2, 2]

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.dot(x,y)
        self.assertEqual(raised_exception.exception.args[0], "x or y object is not iterable")


    def test__dot__args_not_iterable_y__nonpositive(self):
        x = [2, 2, 2, 2, 2]
        y = 5

        with self.assertRaises(ValueError) as raised_exception:
            stat_func.dot(x,y)
        self.assertEqual(raised_exception.exception.args[0], "x or y object is not iterable")

#
    def test_covariance__correct_args__positive(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 2, 2, 2, 2]

        self.assertEqual(stat_func.covariance(x,y),0.12221111)