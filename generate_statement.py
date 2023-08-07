"""
Author: Chu Huang
Student ID: 29250358
Version: utf-8
Date Created: 30 Sep 2020
Last Edit: 15 Oct 2020

This program is for the Assignment2 task1.
To read all the given txts and delete all the special sentences in them,
then stored all of them in a basic txt file for futher modeling.
"""

import pandas as pd


class GenerateStatement:

    def __init__(self, f_name):
        self.f_name = f_name
        self.data = pd.read_csv(self.f_name)

        self.sentence = []
        self.type_in()
        self.statement_maker()
        print(self.sentence)

    def type_in(self):
        statement = input('\nType in your statement: ')
        self.sentence.append(statement.lower().split(' '))

    def statement_maker(self):
        first_word_in_grams = self.sentence[0][-1]
        bi_grams = self.data.loc[first_word_in_grams].idxmax()
        print(bi_grams)


def main():
    word = []
    run = GenerateStatement('Probabilistic model.csv')
    print(run.data)



if __name__ == '__main__':
    main()
