import datetime as dt


class Wine:
    """ Class  for describe a wine
    """

    def __init__(self, name, trademark, country, date, *args):
        """

        :param name: str
        :param trademark: str
        :param country: str
        :param date: tuple of year,month,day
        :param args: note
        """
        self.name = name
        self.trademark = trademark
        self.country = country
        self.date_creation = dt.datetime(date[0], date[1], date[2]).date()
        self.note = args
        pass

    def set_name(self, str):
        """ set name of wine

        :param str: name of wine
        :return: none
        """
        self.name = str

    def set_trademark(self, str):
        """ set trademark of wine

        :param str:  trademark of wine
        :return: none
        """
        self.trademark = str

    def set_country(self, str):
        """ set country of origin of wine

        :param str: country the origin of wine
        :return: none
        """
        self.country = str

    def set_date_creation(self, str):
        """set date_creation

        :param str: date_creation
        :return: none
        """
        self.date_creation = str

    def set_note(self, *args):
        """ set note

        :param args: tuple of string
        :return: none
        """
        self.note = args

    def get_name(self):
        """ get name

        :return: str: name of wine
        """
        return self.name

    def get_trademark(self):
        """

        :return: str trademark of wine
        """
        return self.trademark

    def get_country(self):
        """

        :return: str : country origin of wine
        """
        return self.country

    def get_date_creation(self):
        """

        :return: str: date creation
        """
        return self.date_creation.__str__()

    def get_note(self):
        """

        :return: tuple of note
        """
        return self.note

    def aging_wine_days(self, date):
        """

        :param date: class datetime.datetime
        :return: int : aging in days
        """
        return (date - self.date_creation).days


if __name__ == '__main__':
    w = Wine('lala', 'trade', 'rus', (2008, 4, 23), 'aaa', 'bbb', 'ccc')
    print("name: ", w.get_name())
    print("name: ", w.get_country())
    print("date: ", w.get_date_creation())
    print("note: ", w.note)
    today = dt.datetime.today().date()
    print("aging: {} days".format(w.aging_wine_days(today)))
