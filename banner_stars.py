'''
Anas Albedaiwi
albedaiwi1994@gmail.com
'''

import sys
dict_list = {'A':
             ["***** ",
              "* * ",
              "***** ",
              "* * ",
              "* * "],
             'B':["*** ",
                  "* * ",
                  "**** ",
                  "* * ",
                  "**** "],
             'C':["***** ",
                  "* ",
                  "* ",
                  "* ",
                  "***** "],
             'D':["**** ",
                  "* * ",
                  "* * ",
                  "* * ",
                  "**** "],
             'E':["***** ",
                  "* ",
                  "***** ",
                  "* ",
                  "***** "],
             'F':["***** ",
                  "* ",
                  "***** ",
                  "* ",
                  "* "],
             'G':["***** ",
                  "* ",
                  "* *** ",
                  "* * * ",
                  "***** "],
             'H':["* ",
                  "* ",
                  "***** ",
                  "* ",
                  "* "],
             'I':["***** ",
                  " * ",
                  " * ",
                  " * ",
                  "***** "],
             'J':["***** ",
                  " * ",
                  " * ",
                  " * ",
                  "*** "],
             'K':["* * ",
                  "* * ",
                  "* * ",
                  "* * ",
                  "* * "],
             'L':["* ",
                  "* ",
                  "* ",
                  "* ",
                  "***** "],
             'M':["* * ",
                  "* * * ",
                  "* * ",
                  "* * ",
                  "* * "],
             'N':["* ",
                  "** ",
                  "* * ",
                  "* * ",
                  "* * "],
             'O':["***** ",
                  "* * ",
                  "* * ",
                  "* * ",
                  "***** "],
             'P':["***** ",
                  "* * ",
                  "***** ",
                  "* ",
                  "* "],
             'O':["***** ",
                  "* * ",
                  "* * ",
                  "* ** ",
                  "*** * "],
             'R':["***** ",
                  "* * ",
                  "***** ",
                  "* * ",
                  "* * "],
             'S':["***** ",
                  "* ",
                  "***** ",
                  " * ",
                  "***** "],
             'T':["***** ",
                  " * ",
                  " * ",
                  " * ",
                  " * "],
             'U':["* * ",
                  "* * ",
                  "* * ",
                  "* * ",
                  "***** "],
             'V':["* * ",
                  "* * ",
                  "* * ",
                  " * * ",
                  " * "],
             'W':["* * ",
                  "* * ",
                  "* * ",
                  "* * * ",
                  " * * "],
             'X':["* * ",
                  " * * ",
                  " * ",
                  " * * ",
                  "* * "],
             'Y':["* * ",
                  " * * ",
                  " * ",
                  " * ",
                  " * "],
             'Z':["***** ",
                  " * ",
                  " * ",
                  " * ","***** "]}

def print_banner(string, orientation):
    pass

def print_horizontal(string):
    pass

def print_vertical(string):
    pass

def take_input():
    print("The arguments are: "), str(sys.argv)
    print_banner(sys.argv[1], sys.argv[2])


def print_banner(str_input, style):
    str_input = str_input.upper()
    print(str_input)
    if style != "horizontal":
        vertical = ""
        for i in str_input:
            for a in range(5):
                vertical += dict_list[i][a]
                vertical += "\n"
                print (vertical)
            else:
                    horizontal_line = ""
                    for a in range(5):
                        for b in str_input:
                            horizontal_line += dict_list[b][a]
                            horizontal_line += "\n"
                            print(horizontal_line)
                            take_input()
