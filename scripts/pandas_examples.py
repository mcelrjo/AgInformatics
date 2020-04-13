import pandas

import numpy as np 

import seaborn as sns

other = pandas.read_csv('anotherCSV.csv', na_values='.')

for index in dataFile.index:
    if dataFile['control'][index] == 100:
        print dataFile['pylex'][index]

dataFile = pandas.read_csv('csvFileDataExample.csv')

dataFile.describe()

dataFile.groupby('cultivar').describe()

dataFile.groupby('cultivar').sum()

dataFile.groupby(['dat', 'pylex']).mean().plot(kind='barh')

dataFile.groupby('cultivar')['pylex'].mean()

print dataFile.groupby('cultivar').aggregate(['mean', 'min', np.median, max])

print dataFile.groupby('cultivar').aggregate({'control':['mean', 'min', np.median, max]})

print dataFile.groupby(['cultivar','pylex', 'sprint']).aggregate({'control':['mean', 'min', np.median, max]})

for (method, group) in dataFile.groupby('cultivar'):
    print method, group.shape
    
sns.set()  # compare import seaborn and making figure and not importing seaborn
dataFile.groupby(['cultivar','pylex', 'sprint']).mean().plot(y='control', kind='barh')

pylab.xlabel("Percent control relative to the non-treated")

dataFile.groupby(['cultivar','pylex', 'sprint']).aggregate({'control':['mean', 'min', np.median, max]})

dataFile.groupby(['cultivar','pylex', 'sprint']).aggregate({'control':['mean', 'min', np.median, max]})

def filterFunc(x):
    return x['control'].mean() > 80
    
dataFile.groupby(['cultivar', 'pylex', 'sprint']).mean()

dataFile.groupby(['cultivar', 'pylex', 'sprint']).std()

dataFile.groupby(['cultivar', 'pylex', 'sprint']).median()

grouped = dataFile.groupby(['cultivar', 'pylex', 'sprint'])

dataFile.pivot_table('control', index=['cultivar', 'pylex', 'sprint']).boxplot()

sns.violinplot(x='pylex', y='control', data=dataFile)

sns.PairGrid(dataFile, 

dat = dataFile.groupby('dat')

dataFile[dataFile['dat']==42].boxplot(by=['pylex', 'sprint'], column='control', rot=45)

d = sns.load_dataset(dat)

#uses of .boxplot on a dataframe

dat.boxplot(by=['pylex', 'sprint'], column='control')

dataFile[dataFile['dat']==42].boxplot(by=['pylex', 'sprint'], column='control')

dataFile[dataFile['dat']==42].boxplot(by=['pylex', 'sprint'], column='control', rot=45)

dataFile[dataFile['dat']==42].boxplot(by=['pylex', 'sprint'], column='control', rot=45, grid=False)

dataFile.groupby(['cultivar', 'pylex', 'sprint']).filter(filterFunc)

m = dataFile.groupby(['cultivar', 'pylex', 'sprint']).mean()

m.plot(kind='barh')

def removePeriods(x):
    if x == '.':
        x = ''
    return x
    
dataFile.apply(removePeriods)

dataFile['cover'].replace('.', np.NaN)

#to replace periods with missing values (NaN) when reading in the data indicate
#what the na values are
#other = pandas.read_csv('anotherCSV.csv', na_values='.')
#
trinotate = pandas.read_table('shortTrinotate.xls')

print trinotate.columns

print trinotate['#gene_id']

print trinotate['#gene_id'][0]



for i in trinotate['#gene_id']:
    if i == "TRINITY_DN30576_c0_g1":
        print trinotate['transcript_id'], trinotate['Kegg']
        
        
dataFile = pandas.read_csv('csvFileDataExample.csv')

locations =  dataFile['location'].unique().tolist()

meanList = []

for i in locations:
    meanList.append(dataFile[dataFile['location']==i]['injury'].mean())
        
        
population = pandas.read_csv('populationbycountry19802010millions.csv', index_col = "Unnamed: 0")
pops = population.T

print pops.columns

pops['North America']

na = pops['North America']

na.convert_objects(convert_numeric = True).plot(kind = 'line')
