import sys
from collections import defaultdict, Counter

def get_unique_words(filepath):
	'''
	INPUT: string
	OUTPUT: iterable object of strings

	Takes given filepath of a text file and returns the unique words in file.
	'''
	unique_words = []
	with open(filepath) as f_in:
		for line in f_in:
			for word in line.lower().split():
				if word not in unique_words:
					unique_words.append(word)
	return unique_words

def get_unique_words_sets(filepath):
	'''
	INPUT: string
	OUTPUT: iterable object of strings

	Takes given filepath of a text file and returns the unique words in file.
	'''
	unique_words = set()
	with open(filepath) as f_in:
		for line in f_in:
			unique_words.update(line.lower().split())
	return unique_words

def get_word_frequencies(word, filepath):
	'''
	INPUT:
		word - string
		filepath - string
	OUTPUT: int

	Takes a given word and filepath, and find the frequency of the word in
	the text file designated by the filepath.
	'''
	word_freq = dict()
	with open(filepath) as f_in:
		for line in f_in:
			for f_word in line.lower().split():
				word_freq[f_word] = word_freq.get(f_word, 0) + 1
	return word_freq[word]

def get_word_frequencies_defaultdict(word, filepath):
	'''
	INPUT:
		word - string
		filepath - string
	OUTPUT: int

	Takes a given word and filepath, and find the frequency of the word in
	the text file designated by the filepath.
	'''
	word_freq = defaultdict(int)
	with open(filepath) as f_in:
		for line in f_in:
			import pdb
			pdb.set_trace()
			for f_word in line.lower().split():
				word_freq[f_word] += 1
	return word_freq[word]

def get_word_frequencies_Counter(word, filepath):
	'''
	INPUT:
		word - string
		filepath - string
	OUTPUT: int

	Takes a given word and filepath, and find the frequency of the word in
	the text file designated by the filepath.
	'''
	word_freq = Counter()
	with open(filepath) as f_in:
		for line in f_in:
			word_freq.update(line.lower().split())
	return word_freq[word]

def get_unique_words_from_string(text):
	unique_words = set(text.lower().split())
	return unique_words


if __name__ == '__main__':
	filepath = sys.argv[1]
	word = sys.argv[2]
	print 'Normal:', get_word_frequencies(word, filepath)
	print 'defaultdict:', get_word_frequencies_defaultdict(word, filepath)
	print 'Counter:', get_word_frequencies_Counter(word, filepath)
	#print get_unique_words_sets(filepath)








