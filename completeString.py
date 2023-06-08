#https://www.codingninjas.com/codestudio/problems/complete-string_8230849?challengeSlug=striver-sde-challenge

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_ending = False


def create_new_node():
    new_node = TrieNode()
    new_node.is_ending = False
    return new_node


def insert_word(root, word):
    length = len(word)
    current_node = root

    for level in range(length):
        index = ord(word[level]) - ord('a')
        if not current_node.child[index]:
            current_node.child[index] = create_new_node()
        current_node = current_node.child[index]
    current_node.is_ending = True


def are_all_prefixes_present(root, word):
    current_node = root
    for char in word:
        index = ord(char) - ord('a')
        current_node = current_node.child[index]
        if current_node is None or not current_node.is_ending:
            return False
    return True


def complete_string(n, word_array):
    answer = ""

    root = create_new_node()

    for word in word_array:
        insert_word(root, word)

    for word in word_array:
        if not are_all_prefixes_present(root, word):
            continue

        if len(answer) < len(word):
            answer = word
        elif len(answer) == len(word) and word < answer:
            answer = word

    if len(answer) == 0:
        answer = "None"

    return answer

  
#in TrieNode class represented a node in a trie and i createdan array child of size 26
#to srore child nodes for each character ('a' to 'z'). I also had used a is_ending boolean attribute o indicate if the current node represents the end of a word.
#i created a create_new_node function to create a new instance of the TrieNode class and initialized its attributes.
#i created a insert_node function to insrt a word into the Trie by iterating over each character of the word
#and craeted new nodes as necessary. I started from the  root node and followed the Trie path based on the character indices
#i created are_all_prefixes_present dunction to check if all prefixes of a given word are present in the Trie
#i traversed the trie based on each character of the word 
#i created complete_string function to find the longest word fro the given list of words that contains all of its prefixes


















