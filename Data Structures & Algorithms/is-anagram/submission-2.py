class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_s = {}
        unique_t = {}
        for char in s:
            if char in unique_s:
                unique_s[char] = ((unique_s.get(char)) + 1)
            else:
                unique_s[char] = 1
        for char in t:
            if char in unique_t:
                unique_t[char] = ((unique_t.get(char)) + 1)
            else:
                unique_t[char] = 1

        for key in unique_s:
            print(unique_s.get(key))
            print(unique_t.get(key))
            if unique_s.get(key) != unique_t.get(key) or unique_s.keys() != unique_t.keys():
                return False
        return True
            

        

        