"""Implement the aggregate operations"""
import os
import constants
import matplotlib.pyplot as plt
import numpy as np
import collections
import datetime
import configurations
from BaseOperations import BaseOperations


class AggregateOperations(BaseOperations):
    """Contains the aggregate operations"""

    def __init__(self, input_file, output_file):
        super(AggregateOperations, self).__init__(
            input_file, output_file, None)

    def generate_output_file(self, search_text=None):
        separated_contents = self.get_separated_contents_from_message_lines()
        sender_counter = collections.Counter()
        send_time_counter = collections.Counter()
        for item in separated_contents:
            timestamp, sender, _ = item
            if sender:
                sender_counter[sender] += 1

            datetime_object = self.get_datetime_from_timestamp(timestamp)
            if datetime_object:
                send_time_counter[datetime_object.time().hour] += 1

        most_common_senders = sender_counter.most_common(configurations.NUMBER_MOST_COMMON_SENDERS)
        print("The {0} most common message senders in the group are: ".format(
            configurations.NUMBER_MOST_COMMON_SENDERS))
        print(most_common_senders)
        
        most_active_hours = send_time_counter.most_common(configurations.NUMBER_MOST_ACTIVE_HOURS)
        print("The {0} most common hours for sending message in the group is: ".format(
            configurations.NUMBER_MOST_ACTIVE_HOURS))
        print(most_active_hours)        

        # plot the most active members
        self.plot_barchart_from_list_of_tuples(most_common_senders, "Most active members")

        # plot the most active hours
        self.plot_barchart_from_list_of_tuples(most_active_hours, "Most active hours")

        plt.show()

    def get_datetime_from_timestamp(self, timestamp):
        """Get the date time object from time stamp string
        Sample date time format - 03/11/2017, 12:06    
        """
        if timestamp:
            timestamp = timestamp.strip()
            if len(timestamp) == constants.DATETIME_LENGTH:                
                if timestamp[0].isdigit() and timestamp[-1].isdigit():
                    try:
                        return datetime.datetime.strptime(timestamp, constants.DATETIME_FORMAT)
                    except Exception as e:
                        print("Error parsing date: {0} with error: {1}".format(timestamp, str(e)))
        return None


    def plot_barchart_from_list_of_tuples(self, data_with_labels, plot_name):
        """Plot barcharts from the list of tuples"""
        labels = [item[0] for item in data_with_labels]
        frequencies = [int(item[1]) for item in data_with_labels]
        indexes = np.arange(len(labels))
        width = 1
        plt.figure(figsize=(20, 3))
        plt.bar(indexes, frequencies, width=0.3,align='center')
        plt.xticks(indexes, labels)
        plt.title(plot_name)
        output_file_location = os.path.join(constants.OUTPUT_FILES_FOLDER_NAME, plot_name + constants.IMAGE_EXTENSION)
        plt.savefig(output_file_location)

