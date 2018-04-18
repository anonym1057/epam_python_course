import datetime as dt
import traceback as tr
import time


class my_redirect_err:
    """
    A context manager that outputs information about the error that occurred
        to the file, the date, the code execution time.
    Above error rolls (reraise)
    """
    def __init__(self, name_file="error.txt"):
        """

        :param name_file: the path to the file
        """
        self._name_file = name_file

    def __enter__(self):
        self._date_start = dt.datetime.today()
        self._t1 = time.time()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value:
            #если есть ошибка
            with open(self._name_file, 'w') as fout:
                #дата начала, дата окончания
                print(f"Date start: {self._date_start},\nDate end: {dt.datetime.today()}", file=fout)
                self._t2 = time.time()
                t3 = self._t2 - self._t1
                #время выполнения
                print("Time execute: %.02f sec" % (t3), file=fout)
                #вид исключения
                print(f"Error: {exception_value}", file=fout)
                #строка где возникла ошибка
                print("Traceback: ", file=fout)
                tr.print_tb(traceback, file=fout)



if __name__=='__main__':
    with my_redirect_err("error.txt"):
        for i in range(100000):
            for j in range(1000):
                pass
        2/0