# your code goes here!
class Anagram:
    def __init__(self,word = ''):
        self.word = word
        
    def check_anagram(self, word):
        arr = [letter for letter in word.lower()]
        arr.sort()
        return arr
        # return list([letter for letter in word.lower()]).sort()
        
    def match(self,anagrams):
        # return self.check_anagram(anagram) == self.check_anagram(self.word)
        return [word for word in anagrams if self.check_anagram(word) == self.check_anagram(self.word)]
    
hippo = Anagram('hippo')
print(hippo.check_anagram('hippo'))