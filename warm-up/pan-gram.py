def checkIfPangram(s):
    seen_letters = set()
    for char in s:
        if char.isalpha():
            seen_letters.add(char.lower())
    return len(seen_letters) == 26