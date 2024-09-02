# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase to handle case-insensitive comparisons
    
    def match(self, possible_anagrams):
        # Sort the letters in the original word
        sorted_word = sorted(self.word)
        
        # Find all words in possible_anagrams that are anagrams of the original word
        return [anagram for anagram in possible_anagrams if sorted(anagram.lower()) == sorted_word]

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # Output: ['inlets']
