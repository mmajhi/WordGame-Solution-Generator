from itertools import permutations
import time
import Trie

def extractfile(file_name):
    keys=set()
    with open(file_name,"r") as f:
        for data in f:
            data =''.join(c for c in data if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122)
            keys.add(data)

    return keys

def parse_file(file):
    while True:
        try:
            keys = extractfile(file)
            print('Loading...')
            return keys

        except:
            print("Keep the 'dictionary.txt' in the same folder of this file")
            time.sleep(10)
            continue


def solution(t):
    while True:
        letters = list(i for i in input('Enter the letters: ').strip())

        try:
            length = int(input('Enter the required length of word: '))
        except:
            print('Retry...')
            continue

        a=set()

        for word in permutations(letters,length):
                a.add(''.join(word))

        for i in a:
            if t.search(i):
                print(i)
        print()


def main():

    keys=parse_file('dictionary.txt')

    t=Trie.Trie()
    for key in keys:
        t.insert(key)

    solution(t)

if __name__=='__main__':
    main()
