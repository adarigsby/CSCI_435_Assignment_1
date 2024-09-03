import cv2
import sys 
import os
import re
from lxml import etree

#check for all necessary command line arguments and return the path to the set of screenshot/xml file pairs
def check_arguments():
    if (len(sys.argv) == 2):
        return sys.argv[1]
    else:
        return False

#find the screenshot that corresponds to the given xml file 
def find_png_file(xml):
    split_filename = os.path.splitext(xml)
    png = split_filename[0] + '.png'
    return png

#name the file for the new annotated screenshot and add that file to the AnnotatedImages directory
def add_image_to_directory(original_png, annotated_image):
    basename = os.path.basename(original_png)
    filename_without_ext = os.path.splitext(basename)[0]
    
    new_path = 'AnnotatedImages/output_' + filename_without_ext + '.png'
    cv2.imwrite(new_path, annotated_image)
    return 
    
#loop through the files to find all xml files, parse the xml files, and when possible annotate a screenshot based on the bounds of the leaf level components found
def annotate(path_to_files):
    color = (0, 255, 255)
    thickness = 4

    for file in os.scandir(path_to_files):
        if file.path.endswith('.xml'):
            xml_file = file 
            png_file = find_png_file(xml_file)
            image = cv2.imread(png_file)

            try:
                parser = etree.HTMLParser(recover = True)
                tree = etree.parse(xml_file, parser)
            except:
                print("Unable to parse the following xml file:", xml_file)
            else: 
                #looping through nodes in the xml file and checking to see if they are leaf-level nodes
                for node in tree.iter('node'):
                    if len(node) == 0:
                        
                        #getting the bounds of the node
                        bounds = node.get('bounds')
                        individual_bounds = re.findall('\d+', bounds)

                        #using bounds for the start point and end point of the rectangle
                        start_point = (int(individual_bounds[0]), int(individual_bounds[1]))
                        end_point = (int(individual_bounds[2]), int(individual_bounds[3]))    

                        #adding the yellow rectangle to the image 
                        image = cv2.rectangle(image, start_point, end_point, color, thickness)

                add_image_to_directory(png_file, image)
    return 

def main():
    inputted_path = check_arguments()
    if not inputted_path:
        print("Error with command line arguments.")

    #making new directory to store output
    os.mkdir("AnnotatedImages")

    annotate(inputted_path)
    return 

if __name__ == "__main__":
    main()
