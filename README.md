# WordGame Solution Generator

### Synopsis

Meaningful Words that can be made from given letters and of specific length can be generated with this code.

```
Enter the letters: kates
Enter the required length of word: 5

teaks
skate
skeat
steak
takes
stake
keats
```

### How does it work
##### Loading
The **_dictionary.txt_** file contains **466k** different english words. All these words are loaded in the *Trie* data structure. 

##### Searching
All the permutations of the given letters of provided length are then searched in the Trie and if found it is printed.

For using trie data structure the program runs very fast and efficiently. The time complexity for searching and inserting a word is O(n) where n is the length of the word.

##### Optimization
A better _'dictionary.txt'_ file(with less irrelevant words) can be used for speeding up the loading time and less memory consumption.

### Author
**Mayukh Majhi** and [contributors](https://github.com/mmajhi/WordGame-Solution-Generator/network/members)
