import time


def timmer(fun):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        fun(*args, **kwargs)
        endTime = time.time()
        print(endTime - startTime)

    return wrapper


# 树的构建与搜索问题
# root节点是空内容, 意思是每个首节点都与这个节点相连
# 从root 出发,每个点匹配字幕,如果有就继续匹配, 如果是leaf+ 最后一个需要匹配的字母,则返回True, 否则False
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TriNode('root')

    @timmer
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        i = 0
        cur = self.root
        while i < len(word):
            letter = word[i]
            node = cur.getChild(letter)
            if node is None:
                node = TriNode(letter)
                cur.add(node)
            cur = node
            i += 1
        cur.leaf = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.root)


    def _search(self, word, root):

        if len(word) == 0 and root.leaf:
            return True
        elif len(word) == 0 and not root.leaf:
            return False
        if root is None:
            return False

        cur = root
        i = 0
        while i < len(word):
            if word[i] != '.':
                node = cur.getChild(word[i])
                if node is None:
                    return False
                cur = node
                i += 1
            else:
                next = cur.next
                if len(next) == 0:
                    return False
                for node in next:
                    if self._search(word[i+1:], node):
                        return True
                return False
        if node.leaf:
            return True
        return False


class TriNode:
    def __init__(self, letter):
        self.letter = letter
        self.next = set()
        self.leaf = False

    def add(self, node):
        self.next.add(node)

    def getChild(self, letter):
        if len(self.next) == 0: return None
        for node in self.next:
            if node.letter == letter:
                return node
        return None



        # Your WordDictionary object will be instantiated and called as such:
        # wordDictionary = WordDictionary()
        # wordDictionary.addWord("word")
        # wordDictionary.search("pattern")

if __name__ == '__main__':

    w = WordDictionary()
    w.addWord('a')
    w.addWord('a')
    startTime = time.time()
    print(w.search('.'))
    # w.search("aa")
    # w.search("a")
    w.search(".a")
    endTime = time.time()
    print(endTime - startTime)
