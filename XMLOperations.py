from BaseOperations import BaseOperations


class XMLOperations(BaseOperations):
    def __init__(self, input_file, output_file):
        super(XMLOperations, self).__init__(input_file, output_file, "Templates/XML")

    def generate_output_file(self, search_text=None):
        """Generates the output file"""
        container = self.get_template_file_contents("container.txt")
        message_node_template = self.get_template_file_contents("message_node.txt")
        separated_contents = self.get_separated_contents_from_message_lines(self.replace_illegal_values)
        message_nodes = ""
        for item in separated_contents:
            time_stamp, sender, content = item
            message_node = message_node_template.format(time_stamp, sender, content.strip())
            message_nodes += message_node
        contents = container.format(message_nodes)
        self.write_contents_to_file(contents)

    @staticmethod
    def replace_illegal_values(content):
        """Process content by removing the illegal characters in XML"""
        if content is not None:
            content = content.replace('<', '')
            content = content.replace('>', '')
            content = content.replace('&', 'and')
        return content
