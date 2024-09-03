# CSCI_435_Assignment_1
This tool highlights the leaf level GUI-components in screenshots of Android applications. 

## Description
This Python program ouputs annotated screenshots of Android applications, highlighting leaf level GUI-components with yellow boxes. 
Users can input a set of file pairs, with the pairs being made up of xml files and screenshots in the form of png files. The program then parses the xml files for leaf level components and creates new corresponding images identical to the original screenshots, but with yellow rectangles around each of these components. The output of the program is the set of these annotated images, grouped in a directory titled "AnnotatedImages." 

## Dependencies
This program uses the OpenCV library and the lxml XML toolkit. These packages can be installed by running the following command, where the requirements.txt file in this repository is present. 
```
pip install -r requirements.txt
```
This program uses the following built-in modules in Python: re, sys, os.

## Installing and Running the Program
Download Assigment1.py to the same directory as the input, the set of file pairs. 

Within that directory, run the following command with 'inputdirectory' being the folder containing the file pairs.
```
python Assignment1.py inputdirectory
```
Below is an example with the set of input provided for this assigment. 
```
python Assignment1.py Programming-Assignment-Data
```






