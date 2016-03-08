import csv
from matplotlib import pyplot as plt
import matplotlib
import datetime
import time

def displayPlot(data, systolic):
    listDates = []
    for time in data:
        listDates.append(datetime.datetime.fromtimestamp(float(time)))

    plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m/%d/%y'))
    plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator())
    plt.plot(listDates, systolic)
    plt.show()

def fileIO():
    #Attempt to open file
    try:
        file = open('data.csv', 'r+')
    except IOError:
        inp = raw_input("Cannot find file. Create one? (y/n)")
        if inp == 'y':
            print "Created file."
            file = open('data.csv', 'w+')
        else:
            print "Ending."
    return file

def main():
    inp = ''
    while inp != '/':
        print "Welcome to Blood Pressure Monitor."
        print "Please Select an Option. '/' to Exit"
        print '(1) Input New Entry'
        inp = raw_input("in<")


    #reader = csv.reader(fileIO())

    #data = []
    #for row in reader:
     #   data.append(row[0])

    #systolic = [118, 129, 113, 136, 125]

    #displayPlot(data[1:], systolic)



if __name__ == '__main__':
    main()
