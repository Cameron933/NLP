"""
Author: Chu Huang
Student ID: 29250358
Version: utf-8
Date Created: 30 Sep 2020
Last Edit: 19 Oct 2020

This program is for the Assignment2 task3.
To read both of the txt file which was generated before and Use their data to make tables
then stored the table as a csv file.
"""
# The numpy library is for fast mathematical calculation.
# The pandas is for processing scientific tabular data.
import numpy as np
import pandas as pd


# define a class to model the Bi_gram
# calculate the probability of each bi_grams then fill in the table
# The table rows and columns are same, which is the first 1000 words from our vocab file.
# At the end, save it into a csv file(CSV files are generally used to process scientific data).
class BiGramModel():
    # define the output file name
    b_model_file = 'Probabilistic model.csv'

    # Define the constructor.
    def __init__(self, f_name):
        # It's attribute stand for filename.
        self.f_name = f_name
        # To create a empty list wait for store the data from the given file.
        self.content = []

        # first, the try statement try may be executed.
        try:
            # the with statement allows objects like files to be used in a safety way.
            with open(self.f_name, encoding='utf-16-le') as f_input:
                # Go through every line in the file.
                for lines in f_input:
                    # Append it after remove every \n strings in each line.
                    # Then spilt them by spaces.
                    self.content.append(lines.strip('\n').split(' '))
        # if file is not found,same error type makes statement after except run.
        except FileNotFoundError:
            # report error and f"{}" can use the input filename.
            print(f'file {self.f_name} is not found, please run A2_Q1 Pre_processing first')

        # To create a empty list wait for store all data from the vocab.txt.
        self.words_with_frequency = []
        # To create a empty list wait for store the words from the vocab.txt.
        self.words_list = []
        # To create a empty list wait for store the frequency from the vocab.txt.
        self.frequency_list = []
        # Call the preparing_table_title function, so we can get the words list for further usage.
        self.preparing_table_title()
        # I was inspired by pandas(2020) pandas.DataFrame
        # Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
        # create table and use np to fill in the blank, 15880 here is our table size(number of all words)
        self.sentence_prob_table = pd.DataFrame(np.zeros((15880, 15880), dtype=int),
                                                index=self.words_list,
                                                columns=self.words_list)

        # Call the identify_bi_grams function.
        self.identify_bi_grams()

        # I was inspired by Geek for Geeks(2020) numpy.reshape() in Python
        # Reference: https://www.geeksforgeeks.org/numpy-reshape-python/
        # I was inspired by Github(2020) Python Numpy Tutorial
        # Reference: https://cs231n.github.io/python-numpy-tutorial/
        # I was inspired by pandas(2020) Indexing and selecting data
        # Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
        # after identify all the bi_grams, our table have data within it.
        # The following mathematical operation is simulation equation 3 in the assignment task3.
        # We made the whole table here to guarantee the accuracy of probability.
        self.create_table = self.sentence_prob_table.add(1).div(np.array(
            self.frequency_list).reshape(1, len(self.words_list)) + len(self.words_list))
        # slicing the table of first 1000 rows and columns.
        self.create_table = self.create_table.iloc[:1000, :1000]

    # define a function to add the word and frequency to the empty list separately.
    def preparing_table_title(self):

        try:
            # the with statement allows objects like files to be used in a safety way.
            with open('vocab.txt', encoding='utf-16-le') as f_input:
                # Go through every line in the file.
                for lines in f_input:
                    # Append it after remove every \n strings in each line.
                    self.words_with_frequency.append(lines.strip('\n').split('\t'))
        # if file is not found,same error type makes statement after except run.
        except FileNotFoundError:
            # report error and f"{}" can use the input filename.
            print('file vocab.txt is not found, please run A2_Q2 Common_statistics first')

        # go through the whole list
        for element in self.words_with_frequency:
            # the first item in each element is the word
            self.words_list.append(element[0])
            # the last item in each element is the frequency
            # but all data in txt will be read in as strings, need to change it to int here.
            self.frequency_list.append(int(element[1]))

    # define a function to add data into our table
    def identify_bi_grams(self):
        # go through each list in the content list.
        # content is a list of list, all sentence in txt file is a list and one of content list items.
        for sentence in self.content:
            # print(sentence)
            # each list have different length, in order to get all bi_grams,
            # we need to slicing the list by 2
            for word_position in range(len(sentence)):
                start_position = word_position
                end_position = word_position + 2
                # print(words)
                # slicing will not return error,but we just want two word which can form a bi_gram.
                if end_position < len(sentence):
                    bi_grams = sentence[start_position: end_position]
                    # check its length again
                    if len(bi_grams) != 2:
                        continue
                    # take words as row index and column index respectively.
                    index = bi_grams[0]
                    column = bi_grams[1]
                    # print(column)
                    # I was inspired by pandas(2020) Indexing and selecting data
                    # Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
                    # add one to occur time in the corresponding position of the table
                    self.sentence_prob_table.loc[index, column] += 1

    # define save model function to save csv table.
    def save_bi_gram_model(self):
        # I was inspired by pandas(2020) pandas.DataFrame.to_csv
        # Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
        self.create_table.to_csv(self.b_model_file)

def main():
    run = BiGramModel('cleaned.txt')
    run.save_bi_gram_model()
    run.create_table.head()
    print('Program successfully run')

if __name__ == '__main__':
    main()
