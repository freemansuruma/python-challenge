#import dependencies
import re
import numpy as np 

#load data to use in analysis
file = 'paragraph_1.txt'
#open data file and read the data in for analysis
with open(file,'r') as text_file:
    data = text_file.read()
    #split the paragraph into sentences based on .?! then get the length of each sentence
    sentences_list = re.split("(?<=[.!?]) +",data)
    sentence_count = len(sentences_list)
    #create empty list to hold the number of words in each sentence
    words_per_sentence = []
    #loop through the sentence list to get the number of words in each sentence
    for sentence in sentences_list:
        words = sentence.split(" ")
        words_per_sentence.append(len(words))
    #calculate the average number of words in each sentence
    average_sentence_len = np.mean(words_per_sentence)
    #split the paragraph by spaces to get the word count
    words_list = data.split(" ")
    word_count = len(words_list)
    letters_per_word = []
    #loop through word list to get the lenght of each word
    for word in words_list:
        letters_per_word.append(len(word))
    #fine the average word length of the data
    average_word_length = np.mean(letters_per_word)
#print out the analsysis
print('Paragraph analysis')
print('---------------------------------------------------')
print(f'Approximate word count: {word_count}')
print(f'Approximate sentence count: {sentence_count}')
print(f'Average sentence length: {average_sentence_len}')
print(f'Average word length: {average_word_length}')
    