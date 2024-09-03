# Solution

## Natural Language Description of my Solution

My programming solution starts by checking the command line arguments to ensure that the user has included the input, which should be in the form of a directory containing the set of file pairs. If there is an issue with the arguments, the user is alerted through an error message. 

The program then creates a new directory titled 'AnnotatedImages', which will store the outputted set of annotated images in the form of png files. I decided to make a new directory in order to keep the output organized and easy to access. 

The program loops through all of the inputted files, identifying xml files. When an xml file is found, it is parsed using the lxml XML toolkit. I decided to use this toolkit because of its ability to parse through xml files with more minor issues, such as mismatched tags.  

There are some issues though that lxml cannot address, so if this toolkit is not able to parse through the xml file, the user is alerted that there is an error and the corresponding screenshot is not annotated. I decided to handle errors in this way to keep the user informed and avoid producing inaccurate output. 

If an error does not occur, the program iterates through the node elements in the xml file. The program checks to see if each of these node elements are leaf level components by checking their length, in turn checking if they have any children/subelements. I found this to be a simple and efficient way to identify the desired components.

For each leaf level component, the program uses OpenCV to draw a yellow rectangle around the component according to its bounds attribute in the xml file. This rectangle is drawn onto a corresponding screenshot of the Android Application. I decided to use OpenCV because it supports Python, is easy to install and use, and really only required me to use one function for the actual annotation.

Once all leaf level components have been highlighted, the program uses OpenCV to save the image to a new file. The names of these new png files start with "output_" and are followed by <app.package>-<screen#>. I decided to follow this naming convention in favor of consistency and clarity in which inputted files and outputted files correspond to each other.
