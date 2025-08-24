# Statement
# You are given a string sentence that may contain leading or trailing spaces, as well as multiple spaces between words.
# Your task is to reverse the order of the words in the sentence without changing the order of characters within each word. 
# Return the resulting modified sentence as a single string with words separated by a single space, and no leading or trailing spaces.# 

# Constraints:

# The sentence contains English uppercase and lowercase letters, digits, and spaces.
# There is at least one word in a sentence.
# 1 <= sentence.length <= 10^4
# Algorithm: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)
# Implementation:
# Use two pointers to traverse the string from the end to the beginning, collecting words and ignoring
# extra spaces.

def reverse_words(sentence):
    n = len(sentence)
    result = []
    i = n - 1

    while i >= 0:
        print(f"i: {i}, current char: '{sentence[i] if i >= 0 else ''}'")
        # Skip trailing spaces
        while i >= 0 and sentence[i] == ' ':
            i -= 1
            print(f"Skipping space, i: {i}")
        if i < 0:
            break
        # Find the end of the word
        j = i
        while j >= 0 and sentence[j] != ' ':
            j -= 1
            print(f"Finding word start, j: {j}")
        # Append the word to the result
        word = sentence[j + 1:i + 1]
        print(f"Found word: '{word}'")
        result.append(word)
        # Move to the next word
        i = j - 1

    print(f"Final reversed words: {result}")
    return ' '.join(result)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Reversed sentence:", reverse_words(sentence))

# Enter a sentence: My Name is    Suman   Saurav
# i: 27, current char: 'v'
# Finding word start, j: 26
# Finding word start, j: 25
# Finding word start, j: 24
# Finding word start, j: 23
# Finding word start, j: 22
# Finding word start, j: 21
# Found word: 'Saurav'
# i: 20, current char: ' '
# Skipping space, i: 19
# Skipping space, i: 18
# Finding word start, j: 17
# Finding word start, j: 16
# Finding word start, j: 15
# Finding word start, j: 14
# Finding word start, j: 13
# Found word: 'Suman'
# i: 12, current char: ' '
# Skipping space, i: 11
# Skipping space, i: 10
# Skipping space, i: 9
# Finding word start, j: 8
# Finding word start, j: 7
# Found word: 'is'
# i: 6, current char: 'e'
# Finding word start, j: 5
# Finding word start, j: 4
# Finding word start, j: 3
# Finding word start, j: 2
# Found word: 'Name'
# i: 1, current char: 'y'
# Finding word start, j: 0
# Finding word start, j: -1
# Found word: 'My'
# Final reversed words: ['Saurav', 'Suman', 'is', 'Name', 'My']
# Reversed sentence: Saurav Suman is Name My