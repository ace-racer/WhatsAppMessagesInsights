import os
import subprocess
from shutil import copyfile

SAMPLE_INPUTS_LOCATION = os.path.join(os.getcwd(), 'functional_tests', 'sample_inputs')
print('Sample inputs location: {}'.format(SAMPLE_INPUTS_LOCATION))

def test_usage_custom_input_location():
    input_file_name = 'small_test'
    input_file_location = os.path.join(SAMPLE_INPUTS_LOCATION, input_file_name + '.txt')
    subprocess.call(['python', 'main.py', input_file_location])


def test_usage_only_input_file_name():
    inputs_location = os.path.join(os.getcwd(), 'Inputs')
    if not os.path.exists(inputs_location):
        os.makedirs(inputs_location)
    inputs_location = os.path.join(inputs_location, 'small_test.txt')

    sample_input_file_location = os.path.join(SAMPLE_INPUTS_LOCATION, 'small_test.txt')
    copyfile(sample_input_file_location, inputs_location)

    subprocess.call(['python', 'main.py', 'small_test.txt'])


def test_usage_no_show_graphs():
    inputs_location = os.path.join(os.getcwd(), 'Inputs')
    if not os.path.exists(inputs_location):
        os.makedirs(inputs_location)
    inputs_location = os.path.join(inputs_location, 'small_test.txt')

    sample_input_file_location = os.path.join(SAMPLE_INPUTS_LOCATION, 'small_test.txt')
    copyfile(sample_input_file_location, inputs_location)

    subprocess.call(['python', 'main.py', 'small_test.txt', '--show_graphs'])


def test_usage_show_graphs():
    inputs_location = os.path.join(os.getcwd(), 'Inputs')
    if not os.path.exists(inputs_location):
        os.makedirs(inputs_location)
    inputs_location = os.path.join(inputs_location, 'small_test.txt')

    sample_input_file_location = os.path.join(SAMPLE_INPUTS_LOCATION, 'small_test.txt')
    copyfile(sample_input_file_location, inputs_location)

    subprocess.call(['python', 'main.py', 'small_test.txt', '--show_graphs', 'y'])


def test_usage_provide_search_text():
    inputs_location = os.path.join(os.getcwd(), 'Inputs')
    if not os.path.exists(inputs_location):
        os.makedirs(inputs_location)
    inputs_location = os.path.join(inputs_location, 'small_test.txt')

    sample_input_file_location = os.path.join(SAMPLE_INPUTS_LOCATION, 'small_test.txt')
    copyfile(sample_input_file_location, inputs_location)

    subprocess.call(['python', 'main.py', 'small_test.txt', '--show_graphs', 'n', '--search_text', 'hi'])

if __name__ == '__main__':
    test_usage_custom_input_location()
    test_usage_only_input_file_name()
    test_usage_no_show_graphs()
    test_usage_show_graphs()
    test_usage_provide_search_text()