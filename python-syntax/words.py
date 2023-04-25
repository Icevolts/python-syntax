def print_upper_words(words_list):
		'''Take in any words and return them in uppercase'''
		for words in words_list:
			print(words.upper())

def print_upper_words2(words_list):
    '''Take in words and return only the ones that start with e in uppercase'''
    for words in words_list:
        if words.startswith('e') or words.startswith('E'):
            print(words.upper())

def print_upper_words3(words_list, start_letter):
    '''Take in words and a letter(s). Only words starting with the letter(s) defined will be returned in uppercase'''
    for words in words_list:
        for letter in start_letter:
            if words.startswith(letter):
                print(words.upper())