class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        s = ''.join(s.split(' ')).lower()
        s = ''.join(filter(str.isalnum, s))
        L,R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]: return False
            L += 1
            R -= 1
        return True