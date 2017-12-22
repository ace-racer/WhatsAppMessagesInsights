"""Implement the aggregate operations"""
import os
import constants
import matplotlib.pyplot as plt
import collections
from BaseOperations import BaseOperations




class AggregateOperations(BaseOperations):
    """Contains the aggregate operations"""
    def __init__(self, input_file, output_file):
        super(AggregateOperations, self).__init__(input_file, output_file, None)

    def generate_output_file(self, search_text=None):
        separated_contents = self.get_separated_contents_from_message_lines()
        sender_counter = collections.Counter()
        for item in separated_contents:
            _, sender, _ = item
            if sender:
                sender_counter[sender] += 1

        print(sender_counter.most_common(5))
