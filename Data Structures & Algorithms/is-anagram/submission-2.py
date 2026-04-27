class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return ''.join(sorted(s)) == ''.join(sorted(t))
        dic = {}
        for i in range(len(s)):
            si, ti = s[i], t[i]
            if not dic.get(si):
                dic[si] = 1
            else: dic[si] += 1
            if not dic.get(ti):
                dic[ti] = -1
            else: dic[ti] -= 1
        for key in dic:
            if dic.get(key) != 0:
                return False
        return True
