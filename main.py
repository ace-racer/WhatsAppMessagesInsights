import os
import sys
import constants
import argparse
from HTMLOperations import HTMLOperations
from XMLOperations import XMLOperations
from AggregateOperations import AggregateOperations

parser = argparse.ArgumentParser(description="Generate insights from text snapshots of your Whatsapp group chats.")
parser.add_argument("filename", type=str, help="Name of the text snapshot as a .txt file stored in the Inputs folder")
parser.add_argument("--show_graphs", type=str, help="Show graphs showing aggregate metrics (y/yes), default not shown", nargs="?", const="n", default="n")
parser.add_argument("--search_text", type=str, help="Optional search text to highlight in the generated output")

if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename
    show_graphs = args.show_graphs
    search_text = args.search_text

    os.environ["show_graphs"] = show_graphs

    head, tail = os.path.split(filename)
    file_path = filename
    print('Head: ' + head)
    print('Tail: ' + tail)

    filename = tail
    print ("Input File name: " + filename)
    filename_without_extension = filename.strip().split('.')[0]
    print ("File name without extension: " + filename_without_extension)
    html_filename = filename_without_extension + ".html"
    xml_filename = filename_without_extension + ".xml"

    if not head:
        input_file_complete_location = os.path.join(constants.INPUT_FILES_FOLDER_NAME, filename)
    else:
        input_file_complete_location = file_path

    # Create the output folder if it does not exist
    if not os.path.exists(constants.OUTPUT_FILES_FOLDER_NAME):
        os.makedirs(constants.OUTPUT_FILES_FOLDER_NAME) 

    html_output_file_complete_location = os.path.join(constants.OUTPUT_FILES_FOLDER_NAME, html_filename)
    xml_output_file_complete_location = os.path.join(constants.OUTPUT_FILES_FOLDER_NAME, xml_filename)

    # Generate the HTML output
    operations = HTMLOperations(input_file_complete_location, html_output_file_complete_location)
    operations.generate_output_file(search_text)
    print("Completed generating the HTML for the messages")

    # Generate the XML output
    operations = XMLOperations(input_file_complete_location, xml_output_file_complete_location)
    operations.generate_output_file(search_text)
    print("Completed generating the XML for the messages")

    # Generate the aggregate analysis
    operations = AggregateOperations(input_file_complete_location, None)
    operations.generate_output_file(None)
    print("Completed generating the images")
    print("All files are present in the Output folder in the same location as main.py script...")