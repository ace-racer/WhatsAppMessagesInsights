import sys


def get_details_from_wa_file(filename):
    """Get the lines in the WhatsApp file"""
    try:
        return [line for line in open(filename, 'r')]
    except Exception, e:
        print "An error occurred while opening the file: " + str(e)
        return None


def set_row_format_based_on_search_text(search_text, timestamp, message):
    """Format the table row based on whether the message contains the search text or not"""
    if message:
        row_format_to_use = """<tr>\n\t<td>{0}</td>\n\t<td>{1}</td>\n</tr>\n"""
        special_table_row = """<tr>\n\t<td>{0}</td>\n\t<td class = 'highlighted'>{1}</td>\n</tr>\n"""

        if search_text is not None:
            search_text_lower = search_text.lower()
            if message.lower().find(search_text_lower) >= 0:
                row_format_to_use = special_table_row

        return row_format_to_use.format(timestamp, message.strip())


def write_contents_to_file(file_contents, file_name):
    """Write the file contents to the file name"""
    f = open(file_name, 'w')
    f.write(file_contents)
    f.close()
    print "The output was written to the file: {0} successfully.".format(file_name)


def generate_html_content_from_whatsapp_messages(html_file_name, whatsapp_messages_from_file):
    """Generate the HTML contents from the Whatsapp messages"""
    if whatsapp_messages_from_file is not None:
        print "There were some messages found in the file"

        # the first part contains the date and time and the second part contains the actual message
        whatsapp_messages_from_file_divided = [
            (line.split('-')[0], line.split('-')[1]) if line.find('-') >= 0 else ('', line) for line in
            whatsapp_messages_from_file]

        # the HTML container format
        html_container = """
    				<html>
    					<head>
    						<title>{0}</title>
    						<link rel='stylesheet' href='styles.css' />
    					</head>
    					<body>
    						<table>
    							<tr>
    								<th>Timestamp</th>
    								<th>Message</th>
    							</tr>
    							{1}
    						</table>
    					</body>
    				</html>
    				"""

        table_contents_separated = [
            set_row_format_based_on_search_text(search_text, line_timestamp_message[0], line_timestamp_message[1]) for
            line_timestamp_message in whatsapp_messages_from_file_divided]
        table_contents_joined = ''.join(table_contents_separated)
        html_file_contents = html_container.format(filename_without_extension, table_contents_joined)
        write_contents_to_file(html_file_contents, html_file_name)


def generate_xml_content_from_whatsapp_messages(xml_file_name, whatsapp_messages_from_file):
    """Generates XML contents from the WA messages"""
    xml_container = "<?xml version='1.0' encoding='UTF-8'?>\n<messages>{0}</messages>"
    xml_contents = "<message>\n\t<timestamp>{0}</timestamp>\n\t<sender>{1}</sender>\n\t<content>{2}</content>\n</message>\n"
    xml_value = ""
    if whatsapp_messages_from_file is not None:
        print "There were some messages found in the file"
        for whatsapp_message in whatsapp_messages_from_file:
            if whatsapp_message.find('-') >= 0:
                time_stamp = whatsapp_message.split('-')[0]
                message = whatsapp_message.split('-')[1]
            else:
                time_stamp = ''
                message = whatsapp_message
            if message.find(':') >= 0:
                sent_from = message.split(':')[0]
                remaining_message_text = message.split(':')[1]
            else:
                sent_from = ''
                remaining_message_text = message

            # remove < and > characters from the remaining message text
            remaining_message_text = remaining_message_text.replace('<', '')
            remaining_message_text = remaining_message_text.replace('>', '')
            remaining_message_text = remaining_message_text.replace('&', '&amp;')
            xml_value += xml_contents.format(time_stamp, sent_from, remaining_message_text.strip())
        xml_container = xml_container.format(xml_value)
        write_contents_to_file(xml_container, xml_file_name)


if __name__ == "__main__":
    num_arguments = len(sys.argv)
    if num_arguments == 1:
        print "Usage: python {0} {1} {2}".format(sys.argv[0], "<<WhatsApp message file with txt extension>> <<Search Text>>")
    else:
        filename = sys.argv[1]
        if num_arguments == 3:
            search_text = sys.argv[2]
        else:
            search_text = None

        print "Search Text: " + search_text
        print "File name: " + filename
        filename_without_extension = filename.strip().split('.')[0]
        print "File name without extension: " + filename_without_extension
        html_filename = filename_without_extension + ".html"
        xml_filename = filename_without_extension + ".xml"
        whatsapp_messages_from_file = get_details_from_wa_file(filename)
        generate_html_content_from_whatsapp_messages(html_filename, whatsapp_messages_from_file)
        generate_xml_content_from_whatsapp_messages(xml_filename, whatsapp_messages_from_file)