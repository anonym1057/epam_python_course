"""
Statistical operations module
"""

from collections import Counter
from math import floor
import matplotlib.pyplot as plt


def mean(x):
    """
    returns the mean value of x
    :param x: object for which you want to find the average value
    :type x: iterable object x supporting convert in list object
    :return: float -- mean value
    """
    try:
        list_x = list(x)
    except TypeError:
        raise TypeError('x object is not iterable')

    try:
        s = sum(list_x)
    except TypeError:
        raise TypeError("unsupported operand ' + '")

    try:
        res = s / len(x)
    except ZeroDivisionError:
        raise ZeroDivisionError('division by zero')

    return res


def median(x):
    """
    Returns median for x
    
    :param x: object for which you want to find the median
    :type x: iterable object x supporting convert in list object
    :return: float - median value
    """
    try:
        list_x = list(x)
    except TypeError:
        raise TypeError('x object is not iterable')

    n = len(list_x)

    try:
        sorted_x = sorted(list_x)
    except:
        raise TypeError("'<' not supported operation")

    mid = n // 2
    if n % 2 == 1:
        return sorted_x[mid]
    else:
        return (sorted_x[mid] + sorted_x[mid - 1]) / 2


def mode(x):
    """
    Returns mode value object x

    :param x: object for which you want to find the mode
    :type x: iterable object x supporting convert in list object
    :return: x[index] - object which consist of x
    """
    try:
        list_x = list(x)
    except TypeError:
        raise TypeError('x object is not iterable')

    counts = Counter(list_x)
    max_val = max(counts.values())
    return [k for k, count in counts.items() if count == max_val]


def quartile(x, p):
    """
    Returns quartile of x

    :param x: object for which you want returns quantile
    :type x: iterable object x supporting convert in list object
    :param p: probability of falling into an interval
    :type p: float
    :return: list
    """
    try:
        pf = float(p)
    except TypeError:
        raise TypeError("argument 'p' must be a string or a number")

    if pf < 0 and pf > 1:
        raise TypeError('p must be [0,1]')

    try:
        list_x = list(x)
    except TypeError:
        raise TypeError('x object is not iterable')

    p_idx = int(p * len(list_x))

    try:
        sorted_x = sorted(list_x)
    except:
        raise TypeError("'<' not supported operation")

    return sorted_x[p_idx]


def data_range(x):
    """
    Returns data range of x
    :param x: object for which you want returns range
    :type x: iterable object x supporting convert in list object
    :return: float
    """
    try:
        list_x = list(x)
    except TypeError:
        raise TypeError('x object is not iterable')

    try:
        ma = max(list_x)
        mi = min(list_x)
    except TypeError:
        raise TypeError('' < ' not supported operation')

    return ma - mi


def box_plot(x, title='', xlabel='', ylabel=''):
    """
    Plot box of x

    :param x:
    :param title: title graphics
    :type title:str
    :param xlabel: x axis label graphics
    :type xlabel:str
    :param ylabel: y axis label graphics
    :type ylabel: str
    :return: none
    """
    plt.boxplot(x)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def variance(x):
    """
    Returns variance for x

    :param x:
    :type x:
    :return: list
    """
    m = mean(x)
    return sum([(d - m) ** 2 for d in x]) / (len(x) - 1)


def std(x):
    """
    Returns the standard deviation for x

    :param x:
    :type x:
    :return: float
    """
    return variance(x) ** 0.5


def dot(x, y):
    """
    Return sum of  element-wise product of vectors x and y

    :param x: 1th vector
    :type x:
    :param y: 2th vector
    :type y:
    :return: list
    """
    try:
        list_x = list(x)
        list_y = list(y)
    except TypeError:
        raise TypeError('x or y object is not iterable')

    return sum([i * j for i, j in zip(list_x, list_y)])


def covariance(x, y):
    """
    Returns covariance for pair x,y

    :param x:
    :type x:
    :param y:
    :type y:
    :return:
    """
    m_x = mean(x)
    m_y = mean(y)
    dev_x = [i - m_x for i in x]
    dev_y = [i - m_y for i in y]
    return dot(dev_x, dev_y) / (len(x) - 1)


def correlation(x, y):
    """
    Returns correlation for x

    :param x:
    :type x:
    :param y:
    :type: y:
    :return:
    """
    std_x = std(x)
    std_y = std(y)
    if std_x > 0 and std_y > 0:
        return covariance(x, y) / std_x / std_y
    return 0


def make_buckets(x, bucket_size):
    """
    Returns bucket with bucket size for x

    :param x:
    :type x:
    :param bucket_size:
    :type bucket_size:
    :return:
    """
    return Counter([bucket_size * floor(i / bucket_size) for i in x])


def hist_plot(x, bucket_size, title='', xlabel='', ylabel=''):
    """
    Plot histogram for x  with bucket_size weight

    :param x:
    :type x:
    :param bucket_size:
    :type title:str
    :param xlabel: x axis label graphics
    :type xlabel:str
    :param ylabel: y axis label graphics
    :type ylabel: str
    :return:
    """

    hist_data = make_buckets(x, bucket_size)
    try:
        plt.bar(hist_data.keys(), hist_data.values(), width=bucket_size)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    except Exception:
        raise TypeError('Incorrect data x or bucket_size.')


def plot_(x, y, title='', xlabel='', ylabel=''):
    """
    Plot graph for x and y

    :param x:
    :type x:
    :param y:
    :type y:
    :type title:str
    :param xlabel: x axis label graphics
    :type xlabel:str
    :param ylabel: y axis label graphics
    :type ylabel: str
    :return:
    """
    try:
        plt.plot(x, y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    except Exception:
        raise TypeError("Incorrect data x or y.")
