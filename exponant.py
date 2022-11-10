#!/usr/bin/env python3
# Created by: Lucas LeBlanc
# Created on: Nov 2022
# This program uses for while loops


def main():

    loop_counter = 0

    # This function finds the square of all positive integers
    #  up to the given input

    # Input
    positive_string = input("Enter an integer >= 0: ")

    # Process and output
    try:
        positive_float = float(positive_string)
        positive_integer = int(positive_float)
        if positive_integer == positive_float:
            if positive_integer >= 0:
                for loop_counter in range(positive_integer + 1):
                    squared_number = loop_counter * loop_counter
                    print("{0}² = {1}".format(loop_counter, squared_number))
            else:
                print("this is not a positive.".format(positive_integer))
        else:
            print("this is not an integer".format(positive_float))
    except ValueError:
        print("this is not a valid input".format(positive_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
