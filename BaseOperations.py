import os


class BaseOperations(object):
    def __init__(self, input_file, output_file, templates_location):
        self.input_file = input_file
        self.output_file = output_file
        self.sepatated_message_contents = None
        self.templates_location = templates_location       

    @staticmethod
    def open_file_and_read_contents(file_name):
        """Reads the file"""
        try:
            return [line for line in open(file_name, 'r', encoding="utf8")]
        except Exception as e:
            print ("An error occurred while reading the file {0}: {1}".format(file_name, str(e)))
            raise

    def write_contents_to_file(self, file_contents):
        """Write the file contents to the file name"""
        try:
            f = open(self.output_file, 'w', encoding="utf8")
            f.write(file_contents)
            f.close()
            print ("The output was written to the file: {0} successfully.".format(self.output_file))
        except Exception as e:
            print ("An error occurred while writing to the file: " + str(e))

    def get_separated_contents_from_message_lines(self, process_text=None):
        """Get the separated contents from the message lines ina 3 tuple (timestamp, sender, content)"""
        if self.sepatated_message_contents is None:
            self.sepatated_message_contents = []
            file_contents = self.open_file_and_read_contents(self.input_file)
            if file_contents is not None:
                print ("There were some messages found in the file")
                for whatsapp_message in file_contents:
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

                    if process_text is not None:
                        time_stamp = process_text(time_stamp)
                        sent_from = process_text(sent_from)
                        remaining_message_text = process_text(remaining_message_text)
                    self.sepatated_message_contents.append((time_stamp, sent_from, remaining_message_text))

        return self.sepatated_message_contents

    def get_template_file_contents(self, file_name):
        """Gets the template file content"""
        file_location = os.path.join(self.templates_location, file_name)
        file_contents = self.open_file_and_read_contents(file_location)
        return ''.join(file_contents)

    def generate_output_file(self, search_text=None):
        """Generate the output file"""
        pass
