# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        matching = []
        for word in list:
            if sorted(self.word) == sorted(word):
                matching.append(word)
        return matching
