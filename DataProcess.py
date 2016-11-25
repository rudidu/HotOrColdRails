# This will be used to process my rail temperature data from HBM at Proefplaas as well as learning some file processing and conversion techniques.
# Welcome to Rail Temperature Data Processor v1.o

print("Welcome to Rail Temperature Data Processor v1.0")
print('Please enter the number of files to process')
num_files = int(input())
num_measurements = 0

numbertestincrement = 1

DateList = [0] * 1
HourList = [0] * 1
MinuteList = [0] * 1
SecondsList = [0] * 1
TemperatureList =[0]*1

while numbertestincrement < num_files:

    TestNumber = numbertestincrement
    filestring = str(TestNumber)
    numbertestincrement += 1

    with open('PTest1 ('+filestring+').ASC') as f:
        DateTime = f.readlines()[2:]

    date = DateTime[0]
    time = DateTime[1]

    hour1 = time[0]
    hour2 = time[1]
    hours = int(hour1 + hour2)
    min1 = (time[3])
    min2 =(time[4])
    minutes = int(min1 + min2)
    seconds = 0

    Startmintime = float(min1 + min2)

    with open('PTest1 ('+filestring+').ASC') as f:
        temps = f.readlines()[38:]

    num_measure = len(temps)
    num_iteration = 0
    multiplier = 1
    timeslist = Startmintime
    timelisthours = [0] * (num_measure)
    timelistminutes = [0] * (num_measure)
    timelistseconds = [0] * (num_measure)
    timelistdata = [0] * (num_measure)
    num_measurements += num_measure

    while num_iteration < num_measure:
        minutesnew = int(Startmintime) + 50/60 * int(multiplier)

        num_iteration +=1
        multiplier += 1
        seconds = int((minutesnew % 1)*60)
        hourstring = str(hours)
        minutestring = str(int(minutesnew))
        secondsstring = str(seconds)

        if minutesnew > 59:
            minutesnew = 0
            Startmintime = 0
            hours += 1
            multiplier = 0
            continue

        tempdatastring = hourstring + ':'+minutestring+ ':' +secondsstring
        timelisthours[num_iteration-1] = hourstring
        timelistminutes[num_iteration-1] = minutestring
        timelistseconds[num_iteration-1] = secondsstring

    num_iteration = 0

    while num_iteration < num_measure:
        num_iteration +=1

        if int(timelisthours[num_iteration-1]) < 10:
            hourstring = '0' + str(timelisthours[num_iteration-1])
            timelisthours[num_iteration-1] = hourstring
            continue

    num_iteration = 0

    while num_iteration < num_measure:
        num_iteration +=1

        if int(timelistminutes[num_iteration-1]) < 10:
            minutestring = '0' + str(timelistminutes[num_iteration-1])
            timelistminutes[num_iteration-1] = minutestring
            continue

    num_iteration = 0

    while num_iteration < num_measure:
        num_iteration +=1

        if int(timelistseconds[num_iteration-1]) < 10:
            secondsstring = '0' + str(timelistseconds[num_iteration-1])
            timelistseconds[num_iteration-1] = secondsstring
            continue

    num_iteration = 0

    while num_iteration < num_measure:
        num_iteration +=1
        timelistdata[num_iteration-1] = timelisthours[num_iteration-1] + timelistminutes[num_iteration-1] + timelistseconds[num_iteration-1]
        temps[num_iteration-1] = float(temps[num_iteration-1] )

    print(timelistdata)
    print(temps)

    num_iteration = 0
    while num_iteration < num_measure:
        num_iteration +=1
        DateList.append(date)
        HourList.append(timelisthours[num_iteration-1])
        MinuteList.append(timelistminutes[num_iteration-1])
        SecondsList.append(timelistseconds[num_iteration-1])
        TemperatureList.append(temps[num_iteration-1])

num_iteration = 0

import csv
with open('out.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',') #,quotechar='', quoting=csv.QUOTE_MINIMAL)
    while num_iteration < num_measurements:
        num_iteration +=1
        StringDate = str(DateList[num_iteration-1])
        string0 ='\''+ str(HourList[num_iteration-1])
        string1 ='\'' + str(MinuteList[num_iteration-1])
        string2 = '\'' + str(SecondsList[num_iteration-1])
        string3 = str(TemperatureList[num_iteration-1])
        spamwriter.writerow([StringDate]+[string0] + [string1]+[string2]+ [string3])
print('Finished!')



#f.close()

#print(times[1:])

# Read data into data structure i.e. an array

# Close File

# Open next file - read new data and append to data structure

# Write data to data structure

# Export array to .csv or .xslx for further processing
