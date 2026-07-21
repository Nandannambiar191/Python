

def hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, helper)
    print("Move disk", n, "from", source, "to", destination)
    hanoi(n - 1, helper, source, destination)



keypad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}



def keypadWords(digits, word):
    if digits == "":
        print(word)
        return

    letters = keypad[digits[0]]

    for letter in letters:
        keypadWords(digits[1:], word + letter)



def trace(digits, word, level):
    print("  " * level + "Word:", word, "Remaining:", digits)

    if digits == "":
        print("  " * level + "Finished:", word)
        return

    letters = keypad[digits[0]]

    for letter in letters:
        trace(digits[1:], word + letter, level + 1)




print("Tower of Hanoi")
hanoi(3, "A", "B", "C")

print("\nKeypad Words")
keypadWords("23", "")

print("\nRecursion Tree")
trace("23", "", 0)