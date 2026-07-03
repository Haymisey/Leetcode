class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=''
        if len(word1)>len(word2):
            for i in range(len(word2)):
                new+=word1[i]
                new+=word2[i]
            new+=word1[len(word2):]    
        else:
            for i in range(len(word1)):
                new+=word1[i]
                new+=word2[i]
            new+=word2[len(word1):]
        return new    

