#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 30, 2023
# This program converts a level mark to a percentage.


def calc_mark(level):
    match level:
        case "4+":
            mark = 98
            return mark
        case "4":
            mark = 91
            return mark
        case "4-":
            mark = 83
            return mark
        case "3+":
            mark = 78
            return mark
        case "3":
            mark = 75
            return mark
        case "3-":
            mark = 71
            return mark
        case "2+":
            mark = 68
            return mark
        case "2":
            mark = 65
            return mark
        case "2-":
            mark = 61
            return mark
        case "1+":
            mark = 58
            return mark
        case "1":
            mark = 55
            return mark
        case "1-":
            mark = 51
            return mark
        case "0":
            mark = 49
            return mark
        case _:
            mark = -1
            return mark


def main():
    # introduce program to user
    print("Hello, this program converts your level mark to a percentage.")

    # get user mark
    user_mark = input("Please enter a mark: ")

    # call function
    user_percent = calc_mark(user_mark)

    # check if negative or invalid input
    if user_percent == -1:
        print("Please input a valid mark")

    elif (user_percent == 49):
        print("{} is a failing level. It is under 50%.". format(user_mark))

    # display mark
    else:
        print("Your mark of {} is {}%.".format(user_mark, user_percent))


if __name__ == "__main__":
    main()
