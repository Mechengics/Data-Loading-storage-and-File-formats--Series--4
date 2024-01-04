#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data Loading Storage and File Formats


# In[2]:


#Data in raw form is present in different forms. Pandas uses various methods to help read and write data in various formats.


# In[3]:


#Reading and Writing Data in Text Format


# In[4]:


#Data may be present in various forms in case of python. The data can be read as 
#read_(file format)
#read_csv: read delimited data from file, URL or file-like object, use comma as a default delimiter
#read_fwf: Read the fixed width column format.
#read_clipboard: simple variation of csv that is used to read data from web pages.
#read_excel: read tabular data from excel.
#read_hdf: read HDF5 files that is written by pandas. 
#read_html: read all tables found in the given html document. 
#read_json: read data from JSON 
#read_feather: Read the Feather binary file.
#read_orc: Read the Apache ORC binary file format
#read_parquet:Read the Apache Parquet binary file format. 
#read_picke: Read an object sorted by pandas using the Python pickle format
#read_spss: Read a data file created by SPSS
#read_sql: Read the results of a SQL Query
#read_sql_table: Read a whole SQL table( This is important because after we finish reading the data handling part with python, we will move on to SQl)
#read_stata: Read Dataset from the stat file format
#read_xml: Read a table of Data from an XML file. 


# In[5]:


#The use of these functions is to convert data into dataframe.


# In[6]:


#You can apply different parameters to file formats while extracting the data you can read them on the pandas documentation.


# In[9]:


#I have attached a csv file. in the github repository. You can check that out and download it.
#Linux users can view the csv file by using cat command. cat example1.csv
#windows users can view the csv file by using type command. type example1.csv
#remember if you are using the vs code and you have given the path you can open the specify the name of the csv file by using the name of the file.
#it always better to give the full path as it helps to reduce the erros you encounter. From experience as a new user you may not have properly set the editor, so it is always better to provide the full path.
import pandas as pd
import numpy as np
pd.read_csv("C:\\Users\\user\\Desktop\\example1.csv", header=None)#Header=none will give the specified name to the columns itself.


# In[10]:


pd.read_csv("C:\\Users\\user\\Desktop\\example1.csv", names=["name", "age", " city"])
#The above code will give you the column names as the names.


# In[14]:


#want to make the specific column the index of your data.
name=["name", "age", "city"]
pd.read_csv("C:\\Users\\user\\Desktop\\example1.csv", names=name, index_col="city")


# In[15]:


#You can also specify multiple index to the data frame.
pd.read_csv("C:\\Users\\user\\Desktop\\example1.csv", names=name, index_col=["city","name"])


# In[23]:


#Sometimes the data we are dealing don't have a fixed delimiter. Lets suppose this case
#I have attached the csv file as example2 which doesnot have fixed delimiter to separate the data.
#Delimiter means that are those data that not particularly seperated by comma, semicolon or some special symbols, they mayhave whitespace in betweeen the values.
data2=pd.read_csv("C:\\Users\\user\\Desktop\\example2.csv", sep="\s+",names=["a","b","c"])
#this can be solved by the regular expression, \s+
data2


# In[33]:


#Sometimes you want specific lines beacuse it may contain unwanted things for this purpose you can use the skiprows method.
#I have given an example 3 to deal with this concept. 
data3=pd.read_csv("C:\\Users\\user\\Desktop\\example3.csv",skiprows=[0,2,5], names=["a","b","c"],sep="\s+")
data3


# In[39]:


#Want to deal with null values in the expnsion you can try 
#i have kept the na value in the example4. When NA is specified in the csv file format it meas that it is null value at that exact point
#you can use the isna to check it.
data4=pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv",names=name,sep="\s+" )
data4


# In[40]:


pd.isna(data4)


# In[53]:


#You can specify presence of certain stings in the dataframe as null by giving the command na_values=["string name"]
data5=pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv",names=["a","b","c"], na_values=["Null"],sep="\s+")
data5


# In[54]:


#pandas has many default NA representation.This can be made off by giving the command as default values as false"]
data5=pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv",names=["a","b","c"], keep_default_na=False,sep="\s+")
data5


# In[55]:


#You can Check After this. check 
pd.isna(data5)


# In[56]:


#See that the eveything is false so na value is considered to be null in the given dataframe.


# In[63]:


#If you want to specify the null values particularly in the given data frame you can work as.
NAVALUES={"a":[30],"c":["NA"]}
pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv", names=["a","b","c"], na_values=NAVALUES, keep_default_na=False,sep="\s+")


# In[65]:


#You can see the that those values that were destined in the dictionary are now converted into null values.
#parse__dates: this functionality helps to self categorize the data into dates
#keep_date_col: When you have multiple columns of year month and days you can use this particular method, to combine it into a single column of dates
#converter: They are particularly used to define a function that operates on certain columns
#dayfirst: Keep the day always first, dealing with potentially ambigious dates.
#date_praser: Function use to prase dates
#nrows: Counts the total number of rows from the dataframe doesnot include the header.
#iterator: for iterating over the dataframe
#chunksize: For iterating over multiple rows at a time.
#skip_footer: Specifies the number of lines that we are required to ignore at the end of a file
#verbose: Gives details about the time spent in each stage of file conversion and memomry use information
#encoding: gives the encoding of the given text.
#squeeze: if the prased data contains only one column than this returns a series.
#thousands: seperator for thousands integer. 
#decimal: decimal seperator in numbers
#engine: engine that is specified to prase the file. The engines can be "c","pyarrow","python", default is c but other items like pyarrow are much more faster. 
#The python engine is slower but it supports some additional functions.


# In[67]:


#While reading large datasets we don't study the whole data set, we look at the chunks and study them.
#for this purpose we use the process the method of reading the texr files in piecies. 
pd.options.display.max_rows=10#After the making the specification method more compact we can try to look at and read the coressponding data.
data5=pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv", sep="\s+",names=["a","b","c"])
data5


# In[71]:


#Since we are dealing with very small data so we, don't see this particular method in play.
#If you want to specify the condition without assigning the number the specific columns. We can proceed as:
pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv", nrows=5,names=["a","b","c"],sep="\s+")


# In[92]:


#To read certain number of rows in a data set we can use the method of chunker that helps, to select the certain data in the data set. 
chunker=pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv", chunksize=1, names=["a","b","c"],sep="\s+")
print(chunker)


# In[93]:


#Chunker have various unique functions, we can iterate over a particular deal read a particular and conduct operation on a particular data
#consider a operation like this
series1=pd.Series([])
for df in chunker:
    series1=series1.add(df["b"].value_counts(),fill_value=0)
series1=series1.sort_values(ascending=False)
print(series1)
#A particular code of counting the number of repetation of elements in the given chunks of the data frame.


# In[99]:


#We can also convert a non delimited data to delimited fomrat. 
#We know that example 4 is non delimited data
#first we import non delimited data into dataframe
data6=pd.read_csv("C:\\Users\\user\\Desktop\\example4.csv",sep="\s+")
data6


# In[100]:


#You can see the situation of data, want to make delimited by exporting it to csv format you can try
data6.to_csv("C:\\Users\\user\\Desktop\\out1.csv")
#I have attached this out 1 at the repository. You can check it there and proceed forward at looking the result.


# In[101]:


#Want to seperate the sapces between data by some other delimiters and want to print them in the terminal. 
import sys
data6.to_csv(sys.stdout,sep="|")
#Now we have data that is sperated by the seperator we assigned.


# In[104]:


#sometimes there may be missing values in the data. For this you should assign some string value to the data such that the null spots are detected in the data
data6.to_csv(sys.stdout,na_rep="Null")


# In[105]:


#Since our data has no such empty space so we don't have kept null in that place.


# In[113]:


#We can disbale the index names and column names so that the index doesnot have index and column names.
data6.to_csv(sys.stdout, index=False, header=False)


# In[121]:


#You can add your own column, this particular methods are used for looking at how our data looks when we add certain things. 
data6.to_csv(sys.stdout,index=False,header=["a","b","c","d"])


# In[133]:


import csv
#Want to deal with data that is odd and contains many symbols and signs
with open("C:\\Users\\user\\Desktop\\example4.csv") as f: 
    listc=list(csv.reader(f))
#the first line indicates that file is opened in the name of f
#the second line creates a list named as lines and the lines is the list of lists. 
#the csv.refer iterates over the dataframe and creates a list from each row. 
header,values=listc[0],listc[1:]
#the first line[0] selects the first list that is the header and lines[1:] slices the list, where element 0 is selcted from each inner lists and assigned to values
dictionary={k:v for k,v in zip(header,zip(*values))}
#in this process we are creating a dictionary, in this k is the key and v is the value
#the value k and v is assigned on the basis of the values present in the (header, zip(*values)), header for key and, zip(*values) for values
#than zip(*values) does what we call as the joining the multiple lists that is present in values.
#Remember that we have kept the first element of each list and assigned them to values
class my_dialect(csv.Dialect):
    lineterminator="\n"
    delimiter=";"
    quotechar='"'
    quoting=csv.QUOTE_MINIMAL
#This is a way of giving csv reader different dialects that can be present to seperate the elements in the data
#Finally we use the data by using these csv dialects.
#This can be done as follows, remember you need to reopen the file since we have already existed the with block
with open("C:\\Users\\user\\Desktop\\example4.csv") as f:
    reader=csv.reader(f, dialect=my_dialect)
    for row in reader:
        print(row)


# In[147]:


#Json Data
#Json (short for javascript object notation) has become one of the standard formats for sending data by http request between web browser and other application
#It is much more free form and text like than csv file, where csv file is in text form. 
#The json file looks like this: 
import json
obj="""
{
  "person": "Alice",
  "visited_cities": ["Paris", "Tokyo", "Sydney", "Barcelona"],
  "pet": "dog",
  "family_members": [
    {"name": "Bob", "age": 28, "hobbies": ["reading", "gardening"]},
    {"name": "Eva", "age": 35, "hobbies": ["painting", "traveling"]}
  ]
}

"""
#the json is like a python except it has three apostrophes at the last, 


# In[151]:


loaded=json.loads(obj)
loaded


# In[149]:


#Want to reverse the process. You can try as follows: 
reverse=json.dumps(loaded)
reverse


# In[153]:


#You can interpret the json data and convert them in datframe.
#you can choose a subset and create a data frame from the json file 
data7=pd.DataFrame(loaded["family_members"],columns=["name","age","hobbies"])
data7


# In[ ]:


#XML and HTML: Web Scraping
#python has many libraries for reading and writing data in the unbiquitous HTML, and XMl fromats
#These include lxml, Beautiful Soup, html5lib
#While lxml is comaritively faster, other libraries helps to deal with malformed data more easily.
#Pandas has built in function, pandas.read_html, which uses all of these libraries to automatically, prase tables out of html files as DataFrame objects. 
#for conducting this operation you need to install all libraries in python
#if you have anaconda installed on your system you can try.
#conda install lxml beautifulsoup4 html5lib
#if not you have not install anaconda you can simply type pip install and corresponding libraries


# In[ ]:


#The pandas.read_html function has a number of options but by default it searches for and attempts to parse all tabular data contained within <table> tags. 
#I have attached a sample html page in the repository you can check it out to learn more.


# In[162]:


#Want to read that html using pandas. 
table1=pd.read_html("C:\\Users\\user\\Desktop\\html1.html")
len(table1)


# In[163]:


#access the table using the command
tables1=table1[0]
tables1.head()


# In[168]:


#You can observe how the table from the html page is now converted into a dataframe format.


# In[169]:


#Using python to deal with xml format. 


# In[173]:


#Introduction to XML and Prasing
#XML is a extensible markup language that is similar to html in it's appearence, xml is used for data presentation nd is exclusively designed to send and recive data. 
#Parsing XML: Parsing means to read information from a file and split it into picies by identifying parts of that particular XML file. 


# In[174]:


pd.read_xml("C:\\Users\\user\\Desktop\\xml1.xml")#You can use that bug for loop with lxml but that is not necessary.


# In[177]:


#Binary Data Formats. 
#One simple way to store(or serialize) data in binary format is using python built in pickle. But it is not recommended to store the data in the pickle because the data is not gaurenteed to be stable over time. 
frame=pd.read_csv("C:\\Users\\user\\Desktop\\example1.csv")
frame


# In[178]:


#you can convert this into a pickle file using the pickle command, This proceeds as follows.
frame.to_pickle("C:\\Users\\user\\Desktop\\output2.pcikle")


# In[179]:


pd.read_pickle("C:\\Users\\user\\Desktop\\output2.pcikle")


# In[180]:


#From this way you can store and extract the data from the pickle library.


# In[181]:


#Pandas has also different other binary data stored format but we are not discussing about them here. Maybe in our comming series we will discuss about them.


# In[182]:


#Reading Microsoft Excel Files.
#I don't think i should introduce you about what an excel is.


# In[186]:


excel1=pd.read_excel("C:\\Users\\user\\Desktop\\excel1.xlsx")
excel1


# In[187]:


# #Using HDF5 Format
# HDF5 is a respected file format intended for storing large quantities of scientific array data.
# It is avilable as a C library and it has interfaces avilable in many other languages, including Java, Julia, Matlab and Python
# HDF stands for hierarchical data fromat. 
# Each HDF5 file can store multople datasets and supporting metadata. 
# Data with repeated patterns are more easily stored in HDF5 formats. 
# HDF5 can be a good choice for working with large datasets over exceeding the memory as it can be helpful in reading and writing small sections of much larger arrays.
#To learn about this you can go to data analysis with python book by wes mckinney


# In[188]:


#Interacting with the API to extract data is another popular method for extracting data. 
#Some websites have their own api source for providing the data to the source. 


# In[189]:


# #Another important field is interacting with a database. 
# In professional business setting a lot of data may not be stored in excel file formats. 
# SQL based relational databse are in wide use. 
# We will learn about these things further in our comming lessons about SQL databse.


# In[190]:


#And here ends the journey of learning the data loading, storage and file formats.
#If you have made this far You have lerant a lot of information.
#You can check all the file formats in the github repository.


# In[ ]:


#Regards
#Mechengics
#Ankit Sangroula

