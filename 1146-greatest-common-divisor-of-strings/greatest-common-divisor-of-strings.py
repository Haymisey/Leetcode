class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        ans = ""
        shorter = str1 if len(str1) < len(str2) else str2
        
        for i in range(len(shorter), 0, -1):
            candidate = shorter[:i]
            if str1 == candidate * (len(str1) // len(candidate)) and \
               str2 == candidate * (len(str2) // len(candidate)):
                ans = candidate
                break
        
        return ans
