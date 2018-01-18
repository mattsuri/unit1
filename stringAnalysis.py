#Matthew Suriawinata
#1/18/18
#stringAnalysis.py - analyzes a string for characters

sentenceInput = input("Enter a sentence: ")
sentence = sentenceInput.lower()
characters = len(sentence)
letters = characters - sentence.count(" ")
words = sentence.count(" ") + 1

print("Your sentence has", words, "words,", letters, "letters, and", characters, "characters")

letter = input("Enter a letter to search for: ")
letterCount = sentence.count(letter)
print("Your sentence has", letterCount, "of the letter", letter)

word = input("Enter a word to search for: ")
wordCount = sentence.count(word)
print("Your sentence has", wordCount, "of the word", word)