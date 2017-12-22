import os
import sys
import constants
from BaseOperations import BaseOperations
from HTMLOperations import HTMLOperations
from XMLOperations import XMLOperations


if __name__ == "__main__":
    num_arguments = len(sys.argv)
    if num_arguments == 1:
        print ("Usage: python {0} {1} {2}".format(sys.argv[0], "<<WhatsApp message file with txt extension in the Inputs folder in same path as current script>>", "<<Optional Search Text to highlight in results>>"))
    else:
        filename = sys.argv[1]
        if num_arguments == 3:
            search_text = sys.argv[2]
        else:
            search_text = None

        if search_text is not None:
            print ("Search Text: " + search_text)
        print ("File name: " + filename)
        filename_without_extension = filename.strip().split('.')[0]
        print ("File name without extension: " + filename_without_extension)
        html_filename = filename_without_extension + ".html"
        xml_filename = filename_without_extension + ".xml"
        input_file_complete_location = os.path.join(constants.INPUT_FILES_FOLDER_NAME, filename)

        # Create the output folder if it does not exist
        if not os.path.exists(constants.OUTPUT_FILES_FOLDER_NAME):
            os.makedirs(constants.OUTPUT_FILES_FOLDER_NAME) 

        html_output_file_complete_location = os.path.join(constants.OUTPUT_FILES_FOLDER_NAME, html_filename)
        xml_output_file_complete_location = os.path.join(constants.OUTPUT_FILES_FOLDER_NAME, xml_filename)

        # Generate the HTML output
        operations = HTMLOperations(input_file_complete_location, html_output_file_complete_location)
        operations.generate_output_file(search_text)

        # Generate the XML output
        operations = XMLOperations(input_file_complete_location, xml_output_file_complete_location)
        operations.generate_output_file(search_text)