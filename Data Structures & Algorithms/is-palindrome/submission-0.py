class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()


        s = list(s)
        # print(s)


        res = []


        for i in s:
            if i.isalpha() or i.isnumeric():
                res.append(i)


        s = ''.join(res)

        # print(s)

        return s == s[::-1]