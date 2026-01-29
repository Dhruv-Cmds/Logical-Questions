# Author: Dhruv

# File Word Search Engine
# Create a program that:
# Takes a word from user
# Searches it in document.txt
# Prints:
# total occurrences
# all line numbers
# first position (line + word index)
# Case-insensitive.

def search_word():
    word = input("Enter a word: ").lower()

    total_occurrences = 0
    line_numbers = []
    first_position = None   # (line_no, word_index)

    with open("s_document.txt", "r") as f:
        line_no = 1

        for line in f:
            words = line.lower().split()

            for index, w in enumerate(words):
                if w == word:
                    total_occurrences += 1

                    if line_no not in line_numbers:
                        line_numbers.append(line_no)

                    if first_position is None:
                        first_position = (line_no, index + 1)

            line_no += 1

    if total_occurrences == 0:
        print("Word not found")
    else:
        print("Total occurrences:", total_occurrences)
        print("Line numbers:", line_numbers)
        print("First position: Line", first_position[0], "Word", first_position[1])


search_word()
