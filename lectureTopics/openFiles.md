
# Opening, reading, and writing to documents

Most Python programs you will be writing will need to extract data from somewhere in order to use it in the script/program to make some calculation, do some counting, or other processing needs you may have.  In this lesson we will be discussing the processing of information from files.  How to access and handle those files and utilize the information in your Python scripts.

### The _Open_ Statement

Files are opened very simply by using the _open_ statement.  _open_ statements must include a call that declares if a file is open for reading, writing, or both.  

```python
myFile = open(myFile.txt, "r")

print myFile
```