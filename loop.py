#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Nov 2022
# This program uses a for loop


def main():
    # this function uses a for loop

    # input
    positive_integer = int(input("Enter how many times to repeat: "))
    print("")

    # process & output
    for loop_counter in range(positive_integer):
        print("{0} time through loop.".format(loop_counter))


if __name__ == "__main__":
    main()