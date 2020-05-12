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
        dict_copy = data.copy()
        values_list = dict_copy.get(airports)
        index_list = []
        for i in range(len(values_list)):
            if values_list[i][0] not in letters:
                index_list.append(i)
        index_list.reverse()
        for index in index_list:
            for feature in dict_copy.keys():
                del dict_copy[feature][index]
        return dict_copy

    def print_details(self, features, statistic_functions):
        """
        :param features: a SET of features
        :param statistic_functions: a LIST of statistic functions from statistics.py
        :return: print statistic measures on features using the statistic functions from statistics.py
        """
        pass

    def compute_empty_seats(self):
        """
        :return: add a key (names Empty_seats) to data DICT. Its value is a LIST of number of empty seats
        in every record.
        """
        dict_copy = data.copy()
        empty_seats_list = []
        for i in range(dict_copy.get()[0]):
            difference = dict_copy.get("Seats")[i] - dict_copy.get("Passengers")[i]
            if difference > 0:
                empty_seats_list.append(difference)
        dict_copy["Empty_seats"] = empty_seats_list
        return dict_copy

    def count_bad_flights(self, num):
        """
        :param num: an INTEGER
        :return: the number of records that satisfy:
        abs((mean of empty seats in the couple's flights)-(number of empty seats in record no. i)) >= num
        """
        dict_copy = data.copy()
        empty_seats_mean = mean(dict_copy.get("Empty_seats"))
        for i in range():
            pass

