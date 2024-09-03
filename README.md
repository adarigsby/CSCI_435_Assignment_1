# CSCI_435_Assignment_1
This tool highlights the leaf level GUI-components in screenshots of Android applications. 

## Description
This python program ouputs annotated screenshots of Android applications, highlighting leaf level GUI-components with yellow boxes. 
Users can input a set of files pairs, with the pairs being made up of xml files and screenshots in the form of png files. The program then parses the xml files for leaf-level elements and creates new corresponding images identical to the original screenshots, but with yellow rectangles around each of these elemnts. The output of the program is the set of these annotated images, grouped in a directory titled "AnnotatedImages." 

## Getting Started

### Dependencies
This program uses OpenCV library.

### Installing and Running the Program
Download Assigment1.py to the same directory as the input, the set of file pairs. 

Within that directory, run the following command with 'inputdirectory' being the folder containing the file pairs.
```
python Assignment1.py inputdirectory
```





