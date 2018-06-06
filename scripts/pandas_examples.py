import pandas

trinotate = pandas.read_table('short_trinotate.xls')

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
