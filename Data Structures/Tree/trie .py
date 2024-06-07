# Prefix Tree
class TreeNode:
    def __init__(self) -> None:
        self.children = {}
        self.wordEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = TreeNode()

    def insert(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TreeNode()
            cur = cur.children[letter]

        cur.wordEnd = True

    def search(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.wordEnd

    def startsWith(self, prefix) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True

    def firstMatchedPrefix(self, word):
        cur = self.root
        i = 0
        for letter in word:
            if letter not in cur.children:
                return word[:i]
            cur = cur.children[letter]
            i += 1
        return word[:i]


if __name__ == '__main__':
    prefix_tree = Trie()
    prefix_tree.insert("apple")
    prefix_tree.insert("orange")
    prefix_tree.insert("papaya")
    prefix_tree.insert("grapes")
    print(prefix_tree.search('pears'))
    print(prefix_tree.startsWith('app'))
    print(prefix_tree.startsWith('juice'))
    print(prefix_tree.firstMatchedPrefix('applejuice'))
    print(prefix_tree.firstMatchedPrefix('juice'))