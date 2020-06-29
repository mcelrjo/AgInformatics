import pandas, time, urllib.request
import pylab

state = input("enter a two letter state abbreviation: ")

def dataPull(state):
    '''
    Pull data from website and store in a csvFile
    :param state: string,a two letter state abbreviation.
    :return: CSV file of state covid data written to memory.
    '''
    baseURL = 'http://coronavirusapi.com/getTimeSeries/'
    urlLiteral = baseURL + state #construct url to pass to request
    downloaded_data = urllib.request.urlopen(urlLiteral) #pulls data from website
    baseCSV = 'CovidData.csv'
    fullCSV = state + baseCSV #construct
    covData = open(fullCSV, 'w')
    for d in downloaded_data.readlines():
        covData.write(str(d.strip()).strip('b').strip('\''))
        covData.write('\n')

    return fullCSV

def openCSV(csvFile):

    output = pandas.read_csv(csvFile)
    return output

def addDays(pandasCSVFileObject):
    days = []
    for day in pandasCSVFileObject['seconds_since_Epoch']:
        days.append(time.strftime('%Y-%m-%d', time.localtime(day)))

    pandasCSVFileObject['days'] = days

def makeLibrary(modifedPandasCSV):
    covidLib = {}
    for index, row in modifedPandasCSV.iterrows():
        covidLib[row['days']] = [row['days'], row['tested'], row['positive'], row['deaths']]
    return covidLib

def makeFigures(state):

    csvFileName = dataPull(state)
    csvObject = openCSV(csvFileName)
    addDays(csvObject)
    covidLib = makeLibrary(csvObject)

    daysList = []
    testedList = []
    positiveList = []
    deathsList = []

    for entry in covidLib.keys():
        daysList.append(covidLib[entry][0])
        testedList.append(covidLib[entry][1])
        positiveList.append(covidLib[entry][2])
        deathsList.append(covidLib[entry][3])

    stateTitle = "Current Covid-19 Stats for " + state
    pylab.figure(1)
    pylab.subplot(2, 2, 1)
    pylab.suptitle(stateTitle)
    pylab.plot(testedList)
    pylab.ylabel("# tested since Mar. 31")
    pylab.xlabel('days since Mar. 31')
    pylab.subplot(2, 2, 2)
    pylab.plot(positiveList)
    pylab.ylabel("# tested positive since Mar. 31")
    pylab.xlabel("days since Mar. 31")
    pylab.subplot(2, 2, 3)
    pylab.plot(deathsList)
    pylab.ylabel("# deaths from Covid-19 since Mar. 31")
    pylab.xlabel("days since March. 31")

    dailyPositives = []

    for day in positiveList:
        if len(dailyPositives) == 0:
            dailyPositives.append(day)
            dayBefore = day
        else:
            dailyPositives.append(day - dayBefore)
            dayBefore = day

    pylab.subplot(2,2,4)
    pylab.bar(range(len(dailyPositives)), dailyPositives)
    pylab.ylabel("# positive per day since Mar. 31")
    pylab.xlabel("days since Mar. 31")
    pylab.show()

makeFigures(state)
