import sys

# Read in the data from the input file as characters
char_data = []  # List of characters in input file
input_file = sys.argv[1]  # Input file to get contexts in
for line in open(input_file):
    for char in line:
        if (
            char == "\n"
        ):  # Replace newlines with spaces so there are no newlines in contexts
            char = " "
        char_data.append(char)  # Store data as list so that it is mutable


# Group characters into words
words = []  # List of words in input file
found_word = False
word = ""
i = 0
for char in char_data:
    if not found_word:
        if char.isalnum():  # Found the start of a word
            found_word = True
    if found_word:
        if char == " ":  # Found the end of the word
            words.append(word)
            found_word = False
            word = ""  # Clear word
        elif i == len(char_data) - 1:  # Reached the end of the characters
            word += char
            words.append(word)
            found_word = False
            word = ""
        else:
            word += char
    i += 1


# Gather contexts of first ten occurrences of term
term = sys.argv[2]  # Word to get contexts for
contexts = []  # List of contexts, which are each a list of words
i = 0
for word in words:
    if len(contexts) >= 10:  # Only gather contexts for the first ten occurrences
        break
    if word.lower() == term.lower():  # Ignore casing differences
        context_start = i - 2  # Context starts two words before term
        context_end = i + 2  # Context ends two words after term
        if context_start < 0:  # Constrain start index to first word
            context_start = 0
        if context_end > len(words) - 1:  # Constrain end index to last word
            context_end = len(words) - 1
        context = words[context_start : context_end + 1]
        contexts.append(context)
    i += 1

# Print contexts and input
print(
    f"""Input file: {input_file}
Term: {term}
"""
)
for context in contexts:
    print("- ", end="")
    for word in context:
        if word.lower() == term.lower():
            word = f"_{word}_"
        print(word, end=" ")  # Change end character from newline to space
    print()
