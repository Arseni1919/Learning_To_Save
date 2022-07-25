# Learning To Save

## Content

- [As a File](#as-a-file)
- [JSON](#as-json)
- [Numpy](#as-numpy)
- [PyTorch](#as-pytorch)

## As a File 
[(back)](#content)

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
[(back)](#content)

#### Method 1: Writing JSON to a file in Python using `json.dumps()` 

The JSON package in Python has a function called `json.dumps()` that helps in converting a dictionary to a JSON object. It takes two parameters:

- dictionary – the name of a dictionary which should be converted to a JSON object.
- indent – defines the number of units for indentation
After converting the dictionary to a JSON object, simply write it to a file using the “write” function.

```python
import json
 
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
```

#### Method 2: Writing JSON to a file in Python using `json.dump()` 

Another way of writing JSON to a file is by using `json.dump()` method The JSON package has the “dump” function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object. It takes 2 parameters:

- dictionary – the name of a dictionary which should be converted to a JSON object.
- file pointer – pointer of the file opened in write or append mode.
```python
# Python program to write JSON
# to a file
 
 
import json
 
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
```

#### Reading JSON from a file using  `json.load()`

The JSON package has `json.load()` function that loads the JSON content from a JSON file into a dictionary. It takes one parameter:

- File pointer: A file pointer that points to a JSON file.

```python
import json
 
# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))
```

#### `json.loads()`

If you have a JSON string, you can parse it by using the `json.loads()` method.json.loads() does not take the file path, but the file contents as a string, using fileobject.read() with json.loads() we can return the content of the file.

```python
# Python program to read
# json file
  
  
import json
  
  
# JSON string
a = '{"name": "Bob", "languages": "English"}'
  
# deserializes into dict 
# and returns dict.
y = json.loads(a)
  
print("JSON string = ", y)
print()
  
  
  
# JSON file
f = open ('data.json', "r")
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()
```

## As Numpy 
[(back)](#content)

```python
import numpy as np
with open('test.npy', 'wb') as f:
    np.save(f, np.array([1, 2]))
    np.save(f, np.array([1, 3]))
with open('test.npy', 'rb') as f:
    a = np.load(f)
    b = np.load(f)
print(a, b)
```

## As PyTorch 
[(back)](#content)

#### Save/Load state_dict (Recommended)

Save:
```python
torch.save(model.state_dict(), PATH)
```

Load:
```python
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.eval()
```

#### Save/Load Entire Model
Save:
```python
torch.save(model, PATH)
```

Load:
```python
# Model class must be defined somewhere
model = torch.load(PATH)
model.eval()
```

## As Pickle
[(back)](#content)

```python
# Save a dictionary into a pickle file.
import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }

pickle.dump( favorite_color, open( "save.p", "wb" ) )

# Load the dictionary back from the pickle file.
import pickle

favorite_color = pickle.load( open( "save.p", "rb" ) )
# favorite_color is now { "lion": "yellow", "kitty": "red" }
```

## Credits

- [w3schools | File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [geeksforgeeks | json](https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/)
- [numpy | save](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
- [pytorch | save](https://pytorch.org/tutorials/beginner/saving_loading_models.html)
- [realpython | pickle](https://realpython.com/python-pickle-module/)
