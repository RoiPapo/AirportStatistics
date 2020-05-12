import sys
from data import Data
from flights import *
from statistics import *


def main():
    print("hi hhhaaa")
    # path = argv[1]
    # features = argv[2]
    default_path = 'hw2_sample_input.csv'  # REMEMBER T0 CHANGE BEFORE HANDING
    default_features = ['Origin_airport', 'Destination_airport', 'Flights', 'Distance', 'Seats', 'Passengers']
    q1_features = ['Distance', 'Flights', 'Passengers', 'Seats']
    statistic_functions = [mean, median]
    flights = Data(default_path)
    flights.select_features(default_features)
    flights = Flights(flights.data)
    flights.print_details(q1_features, statistic_functions)


if __name__ == "__main__":
    main()
