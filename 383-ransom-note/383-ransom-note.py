class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lst = [0 for _ in range(ord('z')-ord('a')+1)]
        for letter in magazine:
            lst[ord(letter) - ord('a')] += 1
        for letter in ransomNote:
            i = ord(letter) - ord('a')
            if not lst[i]:
                return False
            lst[i] -= 1
        return True