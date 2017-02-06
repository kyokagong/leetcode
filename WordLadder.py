class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        def isOneDif(str1, str2):
            dif = 0
            for l1, l2 in zip(list(str1), list(str2)):
                if l1 != l2:
                    dif += 1
            return dif == 1

        map = {}
        tmpwordList = list(wordList)
        tmpwordList.append(endWord)
        print(tmpwordList)
        queue = [Node(beginWord)]
        map[beginWord] = queue[0]
        while queue and len(tmpwordList):
            cur = queue.pop(0)
            for word in tmpwordList:
                if isOneDif(word, cur.word):
                    if word not in map:
                        map[word] = Node(word, cur.depth + 1)
                    cur.next.append(map[word])
                    queue.append(map[word])
                    tmpwordList.remove(word)
                    if word == endWord:
                        return map[word].depth
        return 0


class Node:
    def __init__(self, word, depth=1):
        self.word = word
        self.depth = depth
        self.next = []

class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        queue = [(beginWord, 1)]

        while queue:
            curTuple = queue.pop()
            curWord = curTuple[0]
            curLen = curTuple[1]
            if curWord == endWord:
                return curLen
            for i in range(len(curWord)):
                part1 = curWord[:i]
                part2 = curWord[i + 1:]
                for l in 'qwertyuiopasdfghjklzxcvbnm':
                    tmpWord = part1 + l + part2
                    if tmpWord in wordList:
                        queue.append((tmpWord, curLen + 1))
                        wordList.remove(tmpWord)
        return 0


if __name__ == '__main__':
    s = Solution()
    # print(s.ladderLength("a", "c", ["a","b","c"]))
    print(s.ladderLength("hit",
"cog",
set([u'hit', u'cog', u'dog', u'hot', u'lot', u'dot', u'log'])))
    print(s.ladderLength("cat", "fin", set(["ion","rev","che","ind","lie","wis","oct","ham","jag","ray","nun","ref","wig","jul","ken","mit","eel","paw","per","ola","pat","old","maj","ell","irk","ivy","beg","fan","rap","sun","yak","sat","fit","tom","fin","bug","can","hes","col","pep","tug","ump","arc","fee","lee","ohs","eli","nay","raw","lot","mat","egg","cat","pol","fat","joe","pis","dot","jaw","hat","roe","ada","mac"])))
