import csv
from matplotlib import pyplot as plt
import matplotlib
import datetime
import time


def displayPlot(data, systolic, diastolic):
    listDates = []
    for time in data:
        listDates.append(datetime.datetime.fromtimestamp(float(time)))

    plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%m/%d/%y'))
    plt.gca().xaxis.set_major_locator(matplotlib.dates.DayLocator())
    plt.plot(listDates, systolic, 'r')
    plt.plot(listDates, diastolic, 'g')
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
        print '(2) Display Systolic and Diastolic Data'
        inp = raw_input("in<")

        if inp == '1':
            #Input New Entry
            file = open('data.csv', 'a')
            date = time.time()
            morn = raw_input("Morning or Night (m/n): ")
            read1 = raw_input("First Reading(Ex: 100/50): ")
            read2 = raw_input("Second Reading(Ex: 100/50): ")
            read3 = raw_input("Third Reading(Ex: 100/50): ")
            #Calculate Average Blood Pressure
            A = read1[:read1.index('/')]
            B = read2[:read2.index('/')]
            C = read3[:read3.index('/')]
            avgSystolic = (int(A)+int(B)+int(C))/3
            a = read1[read1.index('/')+1:]
            b = read2[read2.index('/')+1:]
            c = read3[read3.index('/')+1:]
            avgDiastolic = (int(a)+int(b)+int(c))/3
            avgBP = str(avgSystolic) + '/' + str(avgDiastolic)
            #Option to Enter Weight
            weight = raw_input("Enter Weight? ('n' for none): ")
            
            file.write(str(date)+','+morn+','+read1+
                    ','+read2+','+read3+
                    ','+avgBP+','+weight);
            file.close()
        elif inp == '2':
            #Display Systolic and Diastolic Data
            reader = csv.reader(fileIO())
            data = []
            for row in reader:
                data.append(row[0])

            systolic = [118, 129, 113, 136, 125, 136]
            diastolic = [75, 77, 69, 84, 81, 80]
            displayPlot(data[1:], systolic, diastolic)


if __name__ == '__main__':
    main()
