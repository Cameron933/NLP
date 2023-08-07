"""
Author: Chu Huang
Student ID: 29250358
Version: utf-8
Date Created: 30 Sep 2020
Last Edit: 17 Oct 2020

This program is for the Assignment2 task2.
To generate a frequency of word txt file and two frequency Graphs based on the previously generated txt,
then stored all of them for further work.
There are 3 outputs:
1. File: vocab.txt;
2. Graph of frequency against first 100 words in sorted vocab;
3. Graph of words that occur n time against word occurrence.
"""

# We use Matplotlib as a library for creating visualizations in Python.
import matplotlib.pyplot as plt


# Defining a class as common statistics to sort data in the given txt file then store them.
# By common statistics, it comes from Zipf’s Law.
# Word distribution shows that in a large corpus,
# the frequency of each word is inversely proportional to its ranking in the frequency table.
class CommonStatistics:
    # # define output files name
    v_txt = 'vocab.txt'
    top_word_frequency_pic_file = 'top100_word_frequency.png'
    numb_of_word_occur_time_pic_file = 'numb_of_word_occur_time.png'

    # Define the constructor.
    def __init__(self, f_name):
        # It's attribute stand for filename.
        self.f_name = f_name

        # To create a empty list wait for store the data from the given file.
        self.content = []
        # To create a empty dict wait for store the words and frequency from the content list.
        self.words = {}
        # Create two picture, define aspect ratio, resolution, and draw board.
        self.top_word_frequency_pic = plt.subplots(figsize=(8, 6), dpi=300, nrows=1, ncols=1)
        self.word_occur_time_pic = plt.subplots(figsize=(8, 6), dpi=300, nrows=1, ncols=1)

        # first, the try statement try may be executed.
        try:
            # the with statement allows objects like files to be used in a safety way.
            with open(self.f_name, encoding='utf-16-le') as f_input:
                # Go through every line in the file.
                for lines in f_input:
                    # Append it after remove every \n strings in each line.
                    self.content.append(lines.strip('\n'))
        # if file is not found,same error type makes statement after except run.
        except FileNotFoundError:
            # report error and f"{}" can use the input filename.
            print(f'file {self.f_name} is not found, please run A2_Q1 Pre_processing first')

        # To call these functions one by one, add words then save the data into a file.
        self.add_words()
        self.save_words()

    # This function is used for get single word from the list and count its frequency,
    # then save them both in the dict.
    def add_words(self):
        # go through each list in the content list.
        for line in self.content:
            # split them with spaces to get them individually.
            for word in line.split(' '):
                # If the word already in our object, add its frequency by one.
                if word in self.words:
                    self.words[word] += 1
                # If the word not in our object, set its original frequency as one.
                else:
                    self.words[word] = 1

    # This function is used for save all the word and frequency as a pair in file line by line.
    def save_words(self):
        # Dictionary items() method is used to return the list with all dictionary keys with values.
        # I was inspired by Geek for Geeks(2018) Python Dictionary | items() method
        # Reference: https://www.geeksforgeeks.org/python-dictionary-items-method/#:~:text=In%20Python%20Dictionary%2C%
        # 20items(),all%20dictionary%20keys%20with%20values.&text=Parameters%3A%20This%20method%20takes%20no,key%2C%20v
        # alue)%20tuple%20pair.
        # I was inspired by Geek for Geeks(2018) Sorting HOW TO
        # Reference: https://docs.python.org/3/howto/sorting.html
        # I was inspired by realpython(2020) How to Use Python Lambda Functions
        # Reference: https://realpython.com/python-lambda/
        # when we start counting word and its frequency, it has no word-order.
        # Same as in the dict, so we need to sort it then use lambda to make both of them as a pair.
        ordered_word_frequency = sorted(self.words.items(), key=lambda pair: pair[1], reverse=True)
        with open(self.v_txt, mode='w', encoding='utf-16-le') as f_output:
            # un zip both of them from the iterable list
            for word, frequency in ordered_word_frequency:
                # re-format them and write them in file.
                f_output.write(f'{word}\t{frequency}\n')

    # This function is used for generate the first picture
    # which is the top 250 word frequency png.
    def generate_pic_one(self):
        # I was inspired by PSF(2000) PEP 201--Lockstep Iteration on 17/10/2020
        # Reference: https://www.python.org/dev/peps/pep-0201/
        # I was inspired by PSF(2020) Built-in Functions on 17/10/2020
        # Reference: https://docs.python.org/3/library/functions.html#zip
        # I was inspired by CSDN(2020) Zip Functions in python on 17/10/2020
        # Reference: https://blog.csdn.net/alxe_made/article/details/80494214?biz_id=102&utm_term=python%20zip%E5%87
        # %BD%E6%95%B0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-80494214&spm=10
        # 18.2118.3001.4187
        # Dictionary items() method is used to return the list with all dictionary keys with values.
        # I was inspired by Geek for Geeks(2018) Python Dictionary | items() method
        # Reference: https://www.geeksforgeeks.org/python-dictionary-items-method/#:~:text=In%20Python%20Dictionary%2C%
        # 20items(),all%20dictionary%20keys%20with%20values.&text=Parameters%3A%20This%20method%20takes%20no,key%2C%20v
        # alue)%20tuple%20pair.
        # I was inspired by Geek for Geeks(2018) Sorting HOW TO
        # Reference: https://docs.python.org/3/howto/sorting.html
        # I was inspired by realpython(2020) How to Use Python Lambda Functions
        # Reference: https://realpython.com/python-lambda/
        # In week9 tutorial, Jammeel shows us a Iterator function: map ()
        # So I wondered if there was a similar function that could speed up the program.
        # Then I found zip() function and use it replace two for loop.
        # The for loops still used in next function.
        # I guess this is with in the unit scope.
        top_words = sorted(self.words.items(), key=lambda pair: pair[1], reverse=True)[:100]
        # In conjunction with the * operator can be used to unzip a list.
        word, frequency = zip(*top_words)

        # I was inspired by PSF(2000) PEP 201--Lockstep Iteration on 10/10/2020
        # Reference: https://www.python.org/dev/peps/pep-0201/
        # I was inspired by PSF(2020) Built-in Functions on 10/10/2020
        # Reference: https://docs.python.org/3/library/functions.html#zip
        # I was inspired by Matplotlib(2020) Horizontal bar chart on 10/10/2020
        # Reference: https://matplotlib.org/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-
        # and-markers-barh-py
        # define the picture
        pic1, ax1 = self.top_word_frequency_pic
        ax1.set_title('Graph of frequency against first 100 words(in descending order)')
        ax1.barh(word, frequency, color='red')

    def generate_pic_two(self):
        # Dictionary items() method is used to return the list with all dictionary keys with values.
        # I was inspired by Geek for Geeks(2018) Python Dictionary | items() method
        # Reference: https://www.geeksforgeeks.org/python-dictionary-items-method/#:~:text=In%20Python%20Dictionary%2C%
        # 20items(),all%20dictionary%20keys%20with%20values.&text=Parameters%3A%20This%20method%20takes%20no,key%2C%20v
        # alue)%20tuple%20pair.
        # I was inspired by Geek for Geeks(2018) Sorting HOW TO
        # Reference: https://docs.python.org/3/howto/sorting.html
        # I was inspired by realpython(2020) How to Use Python Lambda Functions
        # Reference: https://realpython.com/python-lambda/
        # List all word and its matched occur times.
        all_words = sorted(self.words.items(), key=lambda pair: pair[1], reverse=True)
        # To build a dictionary from the list.
        pair_dic = dict(all_words)
        # The frequency is the value of the dictionary, so we just collect them here.
        # Then we build a list from the dictionary, so we have a list of numbers of frequency.
        word_occur_time = list(pair_dic.values())
        # Initialize an empty list to get all numbers of frequency result.
        frequency_under_250 = []
        # We just want the frequency below 250 so we append it to the empty list.
        for frequency in word_occur_time:
            if frequency <= 250:
                frequency_under_250.append(frequency)

        # Initialize an empty list to store result of number of same word frequency.
        words_in_same_freq_list = []
        # To check every number in the frequency list, see how many words' frequency are same.
        # Turn the list into a set, each repeating element is recorded only once in the set.
        for numb in set(frequency_under_250):
            # Counting the number of words which in same frequency.
            words_in_same_freq = frequency_under_250.count(numb)
            # Append every numbers to our empty list.
            # Notice here, when we change list into set, the number in set start with reversed order.
            words_in_same_freq_list.append(words_in_same_freq)

        # Turn the list into a set, each repeating element is recorded only once in the set.
        # This way the number of elements will be same in the two list.
        # Notice here, when we change list into set, the number in set start with reversed order.
        # So the order of two list match what we want as frequency under 250: words in same frequency.
        frequency_under_250_list = list(set(frequency_under_250))

        # I was inspired by Matplotlib(2020) Bar chart with gradients on 10/10/2020
        # Reference: https://matplotlib.org/gallery/lines_bars_and_markers/gradient_bar.html#sphx-glr-gallery-lines-
        # bars-and-markers-gradient-bar-py
        # define the picture
        pic1, ax1 = self.word_occur_time_pic
        ax1.set_title('Graph of words that occur n time against word occurrence')
        ax1.bar(frequency_under_250_list, words_in_same_freq_list, color='yellow')

        # If you want to preview the image, uncomment the following function.
        # def show_pics(self):
        #     plt.show()

    # define a function to save pictures
    def save_pics(self):
        # I was inspired by Matplotlib(2020) save figure on 10/10/2020
        # Reference: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html
        self.top_word_frequency_pic[0].savefig(self.top_word_frequency_pic_file, format='png')
        self.word_occur_time_pic[0].savefig(self.numb_of_word_occur_time_pic_file, format='png')

def main():
    run = CommonStatistics('cleaned.txt')
    run.generate_pic_one()
    run.generate_pic_two()
    # If you want to preview the image, uncomment the following line of code.
    # run.show_pics()
    run.save_pics()
    print('All three files generated successfully')
    print('There is too much data in both figures. Please zoom in to see the detailed data')


if __name__ == '__main__':
    main()
