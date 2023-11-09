sentence = input("Please enter a sentence: ")
sentence_formatted = sentence.upper()
print(sentence_formatted)

paragraph = input("Please enter a paragraph: ")
paragraph_formatted = len(paragraph.split())
print(f"The paragraph has {paragraph_formatted} words")

string = input("Please enter a string: ")
string_formatted = string.isdigit()
print(string_formatted)

string_replace = input("Please enter another string: ")
string_replace_formatted = string_replace.replace("a","o")
print(string_replace_formatted)

name = input("Please enter your full name: ")
words = name.split()
first_letter = [word[0] for word in words]
first_letter_str = "".join(first_letter)
print(f"Your initials are : {first_letter_str}")



string_length = input("Please enter one more string: ")
string_length_formatted = len(string_length)
print(string_length_formatted)