from BaseOperations import BaseOperations


class XMLOperations(BaseOperations):
    def __init__(self, input_file, output_file):
        super(XMLOperations, self).__init__(input_file, output_file, "Templates\\XML")