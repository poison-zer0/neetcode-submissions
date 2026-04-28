class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash_table = {}
        for character in s:
            if character in s_hash_table:
                s_hash_table[character]+= 1
            else:
                s_hash_table[character] = 1
        for character in t:
            if character in s_hash_table:
                s_hash_table[character] -= 1
        for character in s_hash_table:
            if s_hash_table[character] != 0:
                return False
        return True