def are_anagrams(word1, word2):
	"""Retrn True, if words are anagrams."""
	#2. Sort the characters of the words.
	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)
	
	#3 Check that the sorteed words are identical
	return word1_sorted == word2_sorted
print("Anagram Test")

#1. Input two words.
two_words = input("Enter two space separated words: ")
word1, word2 = two_words.split() #split into a list of words

if are_anagrams(word1, word2):
	print ("The words are anagram.")
else: 
	print ("The words are not anagrams.")
