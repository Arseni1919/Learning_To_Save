# Learning To Save

## Content

- [As a File]()

## As a File 

#### Open Files

The key function for working with files in Python is the `open()` function.

The `open()` function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

- "r" - Read - Default value. Opens a file for reading, error if the file does not exist

- "a" - Append - Opens a file for appending, creates the file if it does not exist

- "w" - Write - Opens a file for writing, creates the file if it does not exist

- "x" - Create - Creates the specified file, returns an error if the file exists

In addition, you can specify if the file should be handled as binary or text mode

- "t" - Text - Default value. Text mode

- "b" - Binary - Binary mode (e.g. images)

```python
f = open("demofile.txt")
f = open("demofile.txt", "rt")
```

Because "r" for read, and "t" for text are the default values, you do not need to specify them.

The `open()` function returns a file object, which has a `read()` method for reading the content of the file:

```python
f = open("demofile.txt", "r")
print(f.read())
```

#### Close Files

It is a good practice to always close the file when you are done with it.

```python
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```
#### Write to a File

Open the file "demofile2.txt" and append content to the file:

```python
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```

Open the file "demofile3.txt" and overwrite the content:
```python
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
```

#### Delete a File

To delete a file, you must import the OS module, and run its `os.remove()` function:

Remove the file "demofile.txt":
```python
import os
os.remove("demofile.txt")
```

####  Check if File exist
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Check if file exists, then delete it:
```python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

#### Delete Folder
To delete an entire folder, use the `os.rmdir()` method:

Remove the folder "myfolder":

```python
import os
os.rmdir("myfolder")
```

## As JSON


## As Numpy


## As PyTorch


## Credits

- [w3schools | File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- []()
- []()
- []()
- []()
- []()
- []()