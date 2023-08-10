"""
Author: Chu Huang
Version: utf-8


To read all the given txts and delete all the special sentences in them,
then stored all of them in a basic txt file for futher modeling.
"""

import numpy as np
import pandas as pd


#
class BiGramModel:

    b_model_file = 'Probabilistic model.csv'

    def __init__(self, f_name):

        self.f_name = f_name
        # Create a
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

        #
        self.words_with_frequency = []
        #
        self.words_list = []
        #
        self.frequency_list = []
        #
        self.preparing_table_title()

        # first_thousand_words = self.words_list[:1000]
        # first_thousand_frequency_list = self.frequency_list[:1000]
        # total_word_number = len(self.words_list)
        # print(total_word_number)
        self.sentence_prob_table = pd.DataFrame(np.zeros((15880, 15880), dtype=int),
                                                index=self.words_list,
                                                columns=self.words_list)

        self.identify_bi_grams()

        # print(self.frequency_list)
        self.create_table = self.sentence_prob_table.add(1).div(np.array(
            self.frequency_list).reshape(1, len(self.words_list)) + len(self.words_list))
        self.create_table = self.create_table.iloc[:1000, :1000]

        self.g_statement(input('\nplase type in statemnet: '))

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

        for element in self.words_with_frequency:
            self.words_list.append(element[0])
            self.frequency_list.append(int(element[1]))

    def identify_bi_grams(self):

        # go through each list in the content list.
        for grams in self.content:
            # print(grams)
            for words in range(len(grams)):
                start_position = words
                end_position = words + 2
                # print(words)
                if end_position < len(grams):
                    bi_grams = grams[start_position: end_position]
                    if len(bi_grams) != 2:
                        continue
                    index = bi_grams[0]
                    column = bi_grams[1]
                    # print(column)
                    self.sentence_prob_table.loc[index, column] += 1

    def save_bi_gram_model(self):
        self.create_table.to_csv(self.b_model_file)

    def g_statement(self, statement):
        last_word = statement.lower().split(' ')[-1]
        grams = self.create_table.loc[last_word].idxmax()
        print(grams)

def main():
    run = BiGramModel('cleaned.txt')
    # run.save_bi_gram_model()
    run.create_table.head()
    print('Program successfully run')


if __name__ == '__main__':
    main()
