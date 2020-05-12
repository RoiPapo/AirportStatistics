class Flights:

    def __init__(self, data):
        self.data = data

    def filter_by_airport_names(self, airports, letters):
        """
        :param airports: a STRING from the group {"Origin_airport", "Destination_airport"}
        :param letters: a SET of letters
        :return: data (DICT) which contain only records in which the airport's name (according to airports STRING)
        starts with the letters from letters SET.
        """
        pass

    def print_details(self, features, statistic_functions):
        """
        :param features: a SET of features
        :param statistic_functions: a LIST of statistic functions from statistics.py
        :return: print statistic measures on features using the statistic functions from statistics.py
        """
        print("Question 1:")
        for key, value in self.data.items():
            if key in features:
                print(f"{key.title()}: ", end='')
                for index, func in enumerate(statistic_functions):
                    if index == len(statistic_functions) - 1:
                        print(f"{func(value)}")
                    else:
                        print(f"{func(value)}, ", end='')

    def compute_empty_seats(self):
        """
        :return: add a key (names Empty_seats) to data DICT. Its value is a LIST of number of empty seats
        in every record.
        """
        pass

    def count_bad_flights(self, num):
        """
        :param num: an INTEGER
        :return: the number of records that satisfy:
        abs((mean of empty seats in the couple's flights)-(number of empty seats in record no. i)) >= num
        """
        pass
