import sys
from data import Data
from flights import *
from statistics import *


def main():
    # path = argv[1]
    # features = argv[2]
    default_path = 'hw2_sample_input.csv'  # REMEMBER T0 CHANGE BEFORE HANDING
    default_features = ['Origin_airport', 'Destination_airport', 'Flights', 'Distance', 'Seats', 'Passengers']
    q1_features = ['Distance', 'Flights', 'Passengers', 'Seats']
    q1_leters = (['D', 'A', 'T', 'S', 'C', 'I', 'E', 'N'])
    statistic_functions = [mean, median]
    flights = Data(default_path)
    flights.select_features(default_features)
    flights = Flights(flights.data)
    flights.filter_by_airport_names('Origin_airport', q1_leters)
    print("Question 1:")
    flights.print_details(q1_features, statistic_functions)
    print("\nQuestion 2:")


if __name__ == "__main__":
    main()
