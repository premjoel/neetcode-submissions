class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cc = {}
        # cc {s: 0}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            cc[s[i]] = cc.get(s[i], 0) + 1
            cc[t[i]] = cc.get(t[i], 0) - 1
        print(cc.values())
        # print(val for val in cc.values() if val>0)
        check = 0
        for val in cc.values():
            if val == 0:
                continue
            else:
                check += 1
        if check == 0:
            return True
        else:
            return False
        # return any(val==0 for val in cc.values())
        