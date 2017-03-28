def letter_counter(path_to_file, letters_to_count):
    seekingLetters = list(letters_to_count)
    zeroes = [0]*len(letters_to_count)
    counts = dict(zip(seekingLetters, zeroes))

    print "Seeking letters " + str(seekingLetters)

    target = open(path_to_file, 'r')
    fileContents = target.read()
    fileLetters = list(fileContents)
    target.close()

    for sLetter in seekingLetters:
        for fLetter in fileLetters:
            if sLetter == fLetter:
                counts[sLetter] += 1

    print counts
    #print fileLetters

    pass

from sys import argv

script, filename, letters = argv

letter_counter(filename, letters)
