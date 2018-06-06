#Gutenberg solution

import re

#gutenberg = open('GUTINDEX.1997.iso-8859-1.txt', 'r')

def findAuthors(searchFile):
    '''Takes a Gutenberg-year text file and searches the file for using a 
    regular expression for authors.  
    searchFile: a text file or complete path to text file
    RETURNS: dict, of authors and the number of titles in the list
    '''

    openSearch = openFile(searchFile)
    
    #regex = r'by ([\D\s]+)\d*'
    regex = r'by (.*\S.*)'
    dictAuthors = {}
    
    for line in openSearch:
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
    '''Opens file in write mode and returns the open file object.
    fileToOpen:  text file or path to text file
    '''
    
    openFile = open(fileToOpen, mode)
    
    return openFile
    
def closeFile(fileToClose):
    '''Closes file object
    fileToClose: FILE object
    '''
    fileToClose.close()
    
    print "input files are closed"
            
        
def regexLine(regex, line):
    '''Conducts a regular expression search and returns the first item in 
    the tuple search.  
    regex: STR, regular expression phrase.
    line: STR, string to be searched
    RETURNS: STR from the regular expression search
    '''
    
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

