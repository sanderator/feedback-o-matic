#! /usr/bin/env python3

import csv
import sys


'''feedback-o-matic
A very quick-and-dirty hack to provide student project feedback.
Input is a CSV file containing a marking scheme and student marks.
Output is a CSV file per student containing only their own feedback.
Run as: feedback-o-matic allmarks.csv

Bug: doesn't do merged cells.

@author: (c)2015 Peter Sander
'''


def read_the_file(filename):
    with open(filename, mode='r', newline='') as read_csv_file:
        csv_reader = csv.reader(read_csv_file, delimiter=',')

        stuff = []
        for row in csv_reader:
            stuff.append(row)
        # gets common header
        header = stuff[0:4]
        stuff = stuff[4:]
        # processes each luser
        for luser in stuff:
            with open(luser[0] + '.csv', 'w', newline='') as write_csv_file:
                csv_writer = csv.writer(write_csv_file, delimiter=',',
                                        quotechar='"',
                                        quoting=csv.QUOTE_MINIMAL)
                for line in header:
                    csv_writer.writerow(line)
                csv_writer.writerow(luser)
                write_csv_file.close()
            input()


def main():
    if len(sys.argv) == 1:
        print('Usage: feedback-o-matic allmarks.csv')
    else:
        file_name = sys.argv[1]
        read_the_file(file_name)


if (__name__ == '__main__'):
    main()
