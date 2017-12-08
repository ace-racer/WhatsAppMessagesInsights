# Python application to gather insights from WhatsApp group messages #

## Motivation ##
1. Help to gather some insights from WhatsApp group chats - E.g. who is the most active member, what is the recurring topic of discussion, how active is the group, etc.
2. Have fun!
3. This is not meant to be a production application which can be used to earn money, since the intention is just points 1 and 2 above.

## How to run ##
1. Install Python in your machine. The current version has been tested on Python 2.7.12 and runs there
2. Get the chat as a Text file from the WhatsApp group by following the below steps:
    a. Click on the 3 vertical ellipses on the top right corner of the group
    b. Click on More
    c. Click on Email chat
    d. Select without media to keep the size manageable to be sent as an email (most have a 25 MB limit)
3. Create a folder called "TestFiles" in the same location as the main.py and the other Python scripts
4. Create a folder called "Output" in the same location as the main.py and the other Python scripts
5. Download the chat text file from your email inbox and save it inside the folder "TestFiles" created in step # 3 above
6. Run the main.py application from the command line in the below manner:
    * python main.py {Name of the TXT file with the chat details}. E.g. python main.py my_fantastic_group_convo.txt

          This will create the outputs (HTML and XML) corresponding to this file in the Output folder created in step # 4 above
    * python main.py {Name of the TXT file with the chat details} {Search Text}. E.g. python main.py my_fantastic_group_convo.txt music

          This will create the outputs (HTML and XML) corresponding to this file in the Output folder created in step # 4 above with the contents of the HTML file formatted to show messages where the SearchText (music in case of the example) appears
7. Open the Output folder and you would find 2 files X.html and X.xml where X is the name of the original input file that contains the messages in the chat nicely formatted in HTML and XML respectively.
8. All referencing files (CSS, JS Scripts) for the HTML file can be found in the Libraries folder
9. Optional: The generated XML file can be imported into a SpreadSheet software like Microsoft Excel (TM) which can be used to create Pivot tables and charts to answer some basic questions on the group.

## How to contribute ##
1. The application is developed using OOPs principles and maintaining a modular approach
2. The starting point is main.py which passes the parameters from the command line to instatiate the required objects and create the output
3. The base operations like reading from a file, writing to a file and breaking the file contents into a 3 tuple is written in the BaseOperations class.
   Kindly note that the format of the messages from a WhatsApp message dump is:
   TimeStamp-Sender:Content\n
   So, the above is parsed and stored in an in memory list
4. Specific operations for creating HTML and XML outputs are in the derived classes respectively and override the base method 'generate_output_file'
5. Templates for creating the outputs can be found as text files in the Templates folder. Please note that do not modify any file here unless really required as it can break the functionality.
6. Please feel free to add functionality to generate other output files for gathering better insights
### 7. Have fun! ###