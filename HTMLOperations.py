from BaseOperations import BaseOperations


class HTMLOperations(BaseOperations):
    def __init__(self, input_file, output_file):
        super(HTMLOperations, self).__init__(input_file, output_file, "Templates\\HTML")

    def generate_output_file(self, search_text=None):
        """Generates the output file"""
        container = self.get_template_file_contents("container.txt")
        normal_tr = self.get_template_file_contents("normal_tr.txt")
        special_tr = self.get_template_file_contents("special_tr.txt")
        separated_contents = self.get_separated_contents_from_message_lines()
        trs = ""
        if search_text is not None:
            search_text_lower = search_text.lower()

        for item in separated_contents:
            time_stamp, sender, content = item
            tr_template = normal_tr            
            content_lower = content.lower()
            sender_lower = sender.lower()
            if search_text is not None and (content_lower.find(search_text_lower) >= 0 or sender_lower.find(search_text_lower) >= 0):
                tr_template = special_tr

            tr = tr_template.format(time_stamp, sender, content)
            trs += tr + "\n"
        contents = container.format(self.input_file, trs)
        self.write_contents_to_file(contents)
