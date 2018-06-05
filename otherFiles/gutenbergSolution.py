#Gutenberg solution

import re

#gutenberg = open('GUTINDEX.1997.iso-8859-1.txt', 'r')

def findAuthors(searchFile):
    openSearch = openFile(searchFile)
    
    #regex = r'by ([\D\s]+)\d*'
    regex = r'by (.*\S.*)'
    dictAuthors = {}
    
    for line in openSearch:
        if line.startswith(' '):
            pass
        else:
            result = regexLine(regex, line)
            if result in dictAuthors.keys():
                dictAuthors[result] += 1
            elif result == 0:
                pass
            else:
                dictAuthors[result] = 1
                
    closeFile(openSearch)
                
    return dictAuthors
            
            
def openFile(fileToOpen, mode='r'):
    
    openFile = open(fileToOpen, mode)
    
    return openFile
    
def closeFile(fileToClose):
    
    fileToClose.close()
    
    print "input files are closed"
            
        
def regexLine(regex, line):
    
    output = re.search(regex, line)
    try:
        result = output.groups()[0]
        result = re.sub(r'[^\x00-\x7f]',r' ',result) #this line scrubs out unicode https://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space
        result = result[:-6].strip()
    except AttributeError:
        result = 0
    
    return result
    
newDict = findAuthors('GUTINDEX.1997.iso-8859-1.txt')

print newDict

# regex = r'by ([\w\s]+)[ \t]\d+'
# 
# r = regexLine(regex, 'Cymbeline, by William Shakespeare                                         1133C')
# 
# print r

def sortByValue(dictionary):
    sortedDict = sorted(dictionary.items(), key = lambda t: t[1])
    return sortedDict
    

    
sortedAuthors = sortByValue(newDict)

topTen = sortedAuthors[-10:]

def getAuthorValues(authorList):
    author = []
    number = []
    for item in authorList:
        author.append(item[0])
        number.append(item[1])
        
    return author, number
    
authors, books = getAuthorValues(topTen)

import pylab, numpy

width = numpy.arange(len(books))

pylab.barh(width, books)

pylab.yticks(width, authors)

pylab.show()

l = []
for i in range(1,100):
    l.append((i**3)/2.0)
    
pylab.plot(l, linewidth = 10, color='r')
pylab.show()