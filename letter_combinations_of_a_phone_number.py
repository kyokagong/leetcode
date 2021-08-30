# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
# https://medium.com/nerd-for-tech/leetcode-letter-combinations-of-a-phone-number-f711ab47dfb1
# 递归思路每次都遍历。 只有遍历方法
# 递归思路就是每个字数对应的字母表，在一次完整遍历完后才加入到res中。 比如 abc, def 第一次就是 a -> a+d -> 入res

from typing import List


class Solution:
    num_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        for d in digits:
            letters = self.num_map[d]
            t = []
            for l in letters:
                for r in res:
                    t.append(r + l)
            res = t
        return res


class Solution2:
    num_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def __init__(self):
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.generateCombination("", digits, 0)
        return self.res

    def generateCombination(self, current, digits, index):
        if index == len(digits):
            self.res.append(current)
            return
        letters = self.num_map[digits[index]]
        for l in letters:
            self.generateCombination(current+l, digits, index+1)


if __name__ == '__main__':
    print(Solution2().letterCombinations('2'))
