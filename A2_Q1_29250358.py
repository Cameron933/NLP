"""
Author: Chu Huang
Student ID: 29250358
Version: utf-8
Date Created: 30 Sep 2020
Last Edit: 15 Oct 2020

This program is for the Assignment2 task1.
To read all the given txt files and delete all the special sentences in them,
then stored all of them in a txt file called cleaned.txt for further modeling.
"""
# This library provides a portable way of using operating system dependent functionality.
# I don't know what system the tester will use. This module can avoid format errors.
import os


# Defining a class to pre_processing data in the txt files then store them.
# Pre_processing means to read all the given txts and delete all the special sentences in them.
class PreProcess:

    # define output file name
    processed_f = 'cleaned.txt'

    # the constructor is the first method to be invoked by default.
    # It is used to initialise the values of internal variables (instance variables) of the object.
    # To provide default values for filenames.
    def __init__(self, catalog, f_names=None):
        # It's attribute are catalog(stand for file location) and f_names.
        self.catalog = catalog
        # Initialize an empty list to receive all the required files in the folder.
        self.f_names = []

        # For the following code blocks
        # I was inspired by CSDN(2020) Three methods of Python traversing directory folder and file are explained in
        # detail on 07/10/2020
        # Reference: https://blog.csdn.net/qq_39839807/article/details/104070761?biz_id=102&utm_term=os.scandir&utm_me
        # dium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-4-104070761&spm=1018.2118.3001.4187
        # I was inspired by Python Tutorial(2020) os—Miscellaneous operating system interfaces on 01/10/2020
        # Reference: https://docs.python.org/3/library/os.html?highlight=os#os.fsencode
        if f_names is None:
            # Lists and arranges all file names in the specified folder.
            for f_name in sorted(os.listdir(catalog)):
                # To check whether it is the .txt files
                if f_name[-4:] in ['.txt']:
                    # Then add it to the file name list one by one
                    self.f_names.append(os.path.join(catalog, f_name))
                    
        # To create a empty list wait for store the data which has been processed.
        self.cleaned_txt = []

    # For the following code blocks
    # I was inspired by CSDN(2017) Three methods of reading TXT file in Python on 08/10/2020
    # Reference: https://blog.csdn.net/shandong_chu/article/details/70173952
    # This function is used to clean up unnecessary parts of a .txt file.
    def clean_a_txt(self, f_name, encoding):
        # Initialize an empty list to store all the lines we need.
        process_line = []
        # open the txt file with its same encoding
        with open(f_name, encoding=encoding) as f_input:
            # read the txt file line by line.
            for line in f_input.readlines():
                # The very first processing step.
                # Get rid of the read in '\n' and '\ufeff' string.
                line = line.strip('\n').strip('\ufeff')
                # Each line we do not want start with '<'.
                if '<' in line:
                    # Setting a falg which is stand for add or not.
                    whether_to_add = False
                # If the line is empty, do not add.
                elif len(line) == 0:
                    whether_to_add = False
                # All the lines left here are mainly words we need.
                else:
                    whether_to_add = True
                    
                # Appending it to our processing line list.
                if whether_to_add:
                    process_line.append(line)
                    
        # Initialize a counter
        i = 0
        # Initialize an empty list for final result
        ready_line = []
        # To go through every item in the processing line list.
        # Each item from the list stands for a line in txt file.
        while i < len(process_line):
            # To get every line as a String element in the list from the start.
            # TO get rid of the blank at the start of each line.
            sentence = process_line[i].strip()
            # Initialize an empty String for receiving every character in the sentence.
            new_sentence = ''
            # Going through every character to check it and to add.
            for each in sentence:
                # To check every character is letters or spaces.
                if each.isalpha() or each.isspace():
                    new_sentence += each
                else:
                    # Else we add a space instead of a punctuation symbol.
                    # In this way we will not splicing words and causing inaccuracy.
                    # For example, 'my,lord' --> 'mylord' will loss accuracy.
                    new_sentence += ' '
            # To change the whole string into lower cases.        
            process_line[i] = new_sentence.lower()
            # Update the counter, go for next one in the list.
            i += 1

        # After we change symbols into spaces, there are maybe more than one space between words.
        # This block helps us get rid of additional spaces.
        for line in process_line:
            new = ' '.join(line.split())
            ready_line.append(new)

        # return the list to the function.
        return ready_line

    # Defining a function to clean all the file
    def clean_all(self):
        # Going through every .txt files in given folder.
        for file in self.f_names:
            # I was inspired by Geek for Geeks(2020) append() and extend() in Python
            # Reference: https://www.geeksforgeeks.org/append-extend-python/
            # Calling the clean_a_txt method to process every file then extend them all in one.
            self.cleaned_txt.extend(self.clean_a_txt(file, encoding='utf-16-le'))

    # Defining a write data function to write all data to the file at once.
    def save_txt(self):
        # Opening a file ready to do changes.
        # The with statement allows objects like files to be used in a way that
        # ensures they are always cleaned up promptly and correctly.
        with open(self.processed_f, mode='w', encoding='utf-16-le') as f_output:
            # To write the data line by line.
            for each_line in self.cleaned_txt:
                # Here we need to add '\n' string because we deleted it earlier.
                f_output.write(each_line + '\n')


# Define the main function.
def main():
    run = PreProcess(catalog='dataset')
    # print all the file names
    print(f'All processed files listed: {run.f_names}')
    # call the clean_all function.
    run.clean_all()
    # At the last, call save_txt function to save the output.
    run.save_txt()


# using main as name, code will run from this statement.
if __name__ == "__main__":
    main()
