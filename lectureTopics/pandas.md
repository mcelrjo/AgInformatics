### Introductiont to Pandas

Pandas is a module that contains numerous tools for reading and writing to data in table form.  Excel files and csv files can be read and parsed using the pandas dataframe. See the [full documentation](https://pandas.pydata.org/pandas-docs/version/0.21/index.html) at the pandas documentation site.  

What I find pandas useful for is iterating through a table to extract data from a given column based on the value of another column.  For example, if a table is 20,000 lines long and you need to find the value contained in column D if a value in column A is greater than 17, or some other arbitrary number.  How to set this up is not trivial, nor is it exactly intuitive.  We will get to this problem later on.  For now, we will start off with how to generate some basic descriptive statistics and how to generate basic plots using pandas.

As example I am going to use a csv file (comma separated values) in order to demonstrate some basic functionality of _pandas_.

Start off my importing _pandas_.

```python
import pandas

#now use the pandas read_csv function to read a csv file into memory.

dataFile = pandas.read_csv('csvFileDataExample.csv')

print type(dataFile)

#what is the type of the centi object?

print dataFile

# what printed?  What does that tell you?
```
By importing data using "read_csv" a pandas dataframe was created.  There are dozens of modules and attributes that can be accessed using dot notation.  You will notice at the bottom when the centi object is printed the number of rows and columns in the dataframe -- in this case [1151 rows x 7 columns].  The dataframe is most easily viewed as an Excel spreadsheet or some other spreadsheet.  In fact, the csv file could easily be opened in Excel to view the data.  Excel will recognize the comma-deliminted format of the data and open it accordingly.  

Just so you know, delimiters can vary.  At some point you may open data with a different delimiter (or column seperator) such as tab delimited.  In this case, you may have to specific the delimiter.

Instead of using a different delimiter, one may need a different input-output (IO) tool.  "read_csv" is only one of several tools.  "read_table" reads values that are tab delimited.  "read_excel" reads data that are written in Microsoft Excel.  There are others.  See all the [IO Tools](https://pandas.pydata.org/pandas-docs/stable/io.html) on the Pandas Documentation Page.

Now that the dataframe is in memory, attributes about the dataframe can be accessed.

```python
print dataFile.columns

#what did you get from this?  A kind of odd looking list?

for header in dataFile.columns:
	print header

#Now this is a little more human readable.  A little easier to #understand.  It should simply print out the names of the headers.
```  
Now that all the column headers can be acquired, the header names can be used to access the data within a column.  This access is similar to the key-value pair access of a dictionary.  

```python
print dataFile['cultivar']
#this will yield a single column of data

cultivar = dataFile['cultivar']

print type(cultivar)

cultivar.value_counts()

```

In the above case, a single column of data could be printed by using the column header as the reference.  

If you are dealing with multiple data columns simultaneously, you are probably dealing with independent and dependent variables.  Independent variables are treatments, reps, locations, etc.  Whereas, dependent variables are what was measured and coded accorded to the independent variables.  

Multiple independent variables will probably require some data slicing in order to generate the descriptive statistics.  In the example data set for example, if you want to access only the data in "cultivar" column that was labeled as 'woodward', the following code could be implemented.  

```python
#first remember how to isolate the 'cultivar' column

dataFile['cultivar']

#second determine what in this column equals 'woodward'

dataFile['cultivar'] == 'woodward'

#but this just gives you a bunch of 'True' in a column

dataFile[dataFile['cultivar'] == 'woodward']
```
In the final case, the entire phrase that only selects the portion of the dataFile that contains the label 'woodward'.  The dataframe has essentially been sliced vertically in this instance.  The last line could be bound to a variable name and the type would remain a dataframe.   

```python
wood = dataFile[dataFile['cultivar'] == 'woodward']

type(wood)
```

How could you possible extract all the means for all the treatments within a given cultivar?  To this you would need to extract all unique values for treatments from their respective columns.  To make it readable focus on the column that is labled "pylex".

```python 

pylex = dataFile['pylex'].unique().tolist()

print pylex

#this could be done for all the independent variables

sprint = dataFile['sprint'].unique().tolist()

print sprint

```
One of the benefits of having lists of the headers or items in a column is that they can then be interated through to create data on specific slices of the dataframe.  In this case, one could iterate through cultivars, pylex rates, and sprint rates to find means and other descriptive statistics for each of those factor combinations.  In case you were wondering, the data we are looking at are in a factorial arrangement meaning there are all possible combinations of treatments.  

### Pivot Tables

Pivot tables can be useful to quickly generate means for given independent variables.  Pivot tables aggregate and average dependent variables based on the selected dependent variables.  If you have generated means in Excel you may have used pivot tables.  

```python
dataFile.pivot_table(values='control', index=['cultivar', 'pylex', 'sprint'])
```
This will generate a pivot tables with independent variables nested left to right.  By changing the order of the indexing, the label can change.  

Pivot tables are a nice integrated way to generate means for known independent variables. The nice thing as well is that you can actually plot directly from the pivot table using the plot method.  

```python
dataFile.pivot_table(values='control', index=['cultivar', 'pylex', 'sprint']).plot(kind='barh')
```
For more information see the [Pandas Dataframe Plot method](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.plot.html).

### Plotting with pandas

Direct plotting with pandas does not seem to have as much flexibility as with Pylab or matplotlib, but it seems to be a lot simplier and intuitive. Check out the [Pandas documentation on plotting](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.plot.html)for more information.  We will cover some of the useful stuff in class.  

### Using Groupby()

The _groupby()_ function is useful to compute summary statistics for unique items columns.  In the test datafile there are 'cultivars', 'trts', and 'reps' (also a factorial arrangement of _pylex_ and _sprint_ treatments).  Groupby can isolate the items in these columns to aid in computing summary statistics.  Try some of the following test cases.

```python

print dataFile.groupby('cultivar').sum()

print dataFile.groupby('cultivar').mean()

print dataFile.groupby('cultivar')['pylex'].mean()

```

In this data since there is a factorial arrangement, it would be useful to look at 'cultivar', 'pylex', and 'sprint' simultaneusly. Can you figure out how to do this? Also, can you plot this data as a horizontal bar chart only using 'control' as y-value?

[Aggregate](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.aggregate.html) can also be a useful function for isolating data across multiple columns.  Tak a look at the documentation on pandas aggregate.  With aggregate() one can call different summary statistics on a groupby data set with the option of isolating different dependent variables (in our case 'control')using a library call (see below).

```python
print dataFile.groupby('cultivar').aggregate(['mean', 'min', np.median, max])

print dataFile.groupby('cultivar').aggregate({'control':['mean', 'min', np.median, max]})

```

### Using the Index

I am, like many out there, a self-taught programmer.  I have taken some online classes over the years but there is a tremendous amount I have taught myself.  Google, try-and-check, Google it again.  Using Stack Exchange, different blogs, and official documentation -- this is the way I have learned. 

In learning this way, once I figure out a way to complete a task I tend to stick with it.  If I focused on a specific task I could probably do it faster or easier even, but if the job is getting done and my program is not running for over 24 hours, I tend to just keep doing what I have been doing.  

Having said all of that, I want to return to the initial question of how to look at one column of data and check for a certain value.  Based on that value, either write to another file or look up any other value in another column.  

I accomplish this using the index of the dataframe.  Every row in indexed in a dataframe.  So for a given dataframe, you could access a column of data, then access a specific data point in the table by additonally passing the row index.

Consider the population data in the previous "Special problems".

```python

print population['1980'][0]
print population['1981'][17]
```
Curiously, this dataframe is also indexed by the country names. To see this, print the different indexes.

```python

for i in population.index:
	print i
```
This will actually print all the indexes individually.  Now consider that this can allow you to do.  What if you wanted to create a line chart of all the countries that have greater than 100 million population starting in 1980.  

### Special Project

To learn more about Pandas dataframes and interesting attributes you are going to download a federal data set, manipulate the data, and create figures.  The dataset can be found [here](https://catalog.data.gov/dataset/population-by-country-1980-2010).  The data is population by country from 1980 to 2010.  Be advised that this is not a straight forward data set.  You are going to have to do a few manipulations before creating figures.  Just so you know the data are in millions of people.  

##### Part 1:  Understanding the data

For the first part of this project, come to an understanding of how the data is organized and arranged.  Create a figure of five different countries in a line graph that includes: legend, x label, y label, and title.  Save this image as a jpg with your last name as part of the name.  

Email me this figure as a jpg, tiff, or other image file.

##### Part 2:  Create a function

Create a usable function that a user can enter a country name and it will create a figure of population change for that country.  Adapt the function that allows a user to enter up to five country names.  Think about how you are going to resolve typos, misspelling, or capitalization.  Save this function with your last name as part of the name and drop it in the shared box folder.

Email me the function as a stand alone Python script that I can run on my computer.


### Special Project #2

Download the shortTrinotate file for this project.  This project is going to come in several parts.

##### Part 1

For this part you want to look in the "sprot_Top_BLASTX_hit" column and if there is not a period "." in in a given entry, write that row to a new file.  So in the end, you have a new trinotate file that has eliminated all the entries that were not annotated for that particular column.

Email me the number of lines in the new file.

##### Part 2

Develop a regular expression to extract all entries in 'gene_ontology_blast' the first entry of either "molecular_function", "cellular_component", or "biological_process".  Create a figure with this information with three vertical bars of three different colors with each column labeled, an x and y-label, title, and the figure adequately fit to screen.  Save this figure as a tiff or jpg and email to me.  

Email me this figure as a jpg, tiff, or other image file.