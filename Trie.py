class Trienode():
    def __init__(self):
        self.children=[None]*26
        self.isendofword=False

class Trie():
    def __init__(self):
        self.root=self.getnode()

    def getnode(self):
        return Trienode()

    def insert(self,key):
        pcrawl=self.root
        length=len(key)
        for level in range(length):
            index=ord(key[level])-ord('a')
            if 65<=ord(key[level])<=90:
                index+=32
            if not pcrawl.children[index]:
                pcrawl.children[index]=self.getnode()
            pcrawl=pcrawl.children[index]
        pcrawl.isendofword=True

    def search(self,key):
        pcrawl=self.root
        for level in range(len(key)):
            index=ord(key[level])-ord('a')
            if 65<=ord(key[level])<=90:
                index+=32
            if not pcrawl.children[index]:
                return False
            pcrawl=pcrawl.children[index]
        return pcrawl.isendofword

