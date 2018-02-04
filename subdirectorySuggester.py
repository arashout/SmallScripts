class Node:

    def __init__(self):

        self.children = {}
        self.count = 0

    def __repr__(self):
        return 'children {} count {}'.format(self.children, self.count)

    def add(self, word):

        self.count += 1

        if not word:
            return

        head, tail = word[0], word[1:]

        self.children.setdefault(head, Node()).add(tail)

    def __iter__(self):

        if self.count:
            yield ('', self.count)

        for (char, node) in self.children.items():
            for (foo, count) in node:
                yield (char + foo, count)

class Trie:

    def __init__(self):

        self.root = Node()

    def add(self, word):

        self.root.add(word)

    def __iter__(self):

        for (word, count) in self.root:
            yield (word, count)


if __name__ == '__main__':

    inp = 'hello'

    trie = Trie()
    trie.add(inp)
    trie.add('foo')
    trie.add('foo')
    trie.add('fooo')
    trie.add('foobar')

    strings = list(x for x in trie)
    print(strings)